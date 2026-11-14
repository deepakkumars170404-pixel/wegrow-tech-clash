const http = require('http');
const fs = require('fs');
const path = require('path');
const os = require('os');
const { WebSocketServer } = require('ws');

// Top-level crash guards to ensure 100% server uptime even under unexpected errors
process.on('uncaughtException', (err) => {
  console.error('[CRASH GUARD] Caught uncaughtException:', err.message);
});
process.on('unhandledRejection', (reason) => {
  console.error('[CRASH GUARD] Caught unhandledRejection:', reason);
});

const PORT = process.env.PORT || 3000;
const PUBLIC_DIR = path.join(__dirname, 'public');

// Global Game State
const gameState = {
  currentView: 'lobby', // 'lobby' | 'game' | 'winner'
  currentRoundIdx: 0,
  currentQuestionIdx: 0,
  buzzerState: 'locked', // 'locked' | 'open' | 'buzzing'
  buzzerQueue: [], // [ { playerId, playerName, teamId, teamName, time } ]
  lockedTeamsForQuestion: [], // teamIds that answered wrong for current question
  activeAnsweringTeamId: null, // the team currently answering on their phone
  activeAnsweringPlayerId: null, // the player who buzzed first
  answerCountdown: 10, // 10-second countdown timer for answering team
  lastAnswerResult: null, // { status: 'correct'|'wrong'|'timeout', teamId, teamName, time }
  teams: [
    { id: 1, name: 'Team Alpha', color: '#38bdf8', score: 0, correctCount: 0, wrongCount: 0, members: [] },
    { id: 2, name: 'Team Beta', color: '#a855f7', score: 0, correctCount: 0, wrongCount: 0, members: [] },
    { id: 3, name: 'Team Gamma', color: '#34d399', score: 0, correctCount: 0, wrongCount: 0, members: [] },
    { id: 4, name: 'Team Delta', color: '#f59e0b', score: 0, correctCount: 0, wrongCount: 0, members: [] }
  ],
  players: {}, // playerId -> { id, name, role, teamId, teamName, score, correctCount, wrongCount }
  leaderboard: {
    teams: [],
    players: []
  },
  debateState: {
    activeTeamIdx: 0,
    secondsLeft: 60,
    isRunning: false
  },
  kickedPlayers: new Set()
};

// Seed 12 Realistic Dummy Players for instant testing!
const DUMMY_PLAYERS = [
  { id: 'dummy_1', name: 'Alex Johnson', role: 'dev' },
  { id: 'dummy_2', name: 'Priya Sharma', role: 'dev' },
  { id: 'dummy_3', name: 'Karthik Raja', role: 'dev' },
  { id: 'dummy_4', name: 'Sarah Miller', role: 'dev' },
  { id: 'dummy_5', name: 'Arjun Das', role: 'dev' },
  { id: 'dummy_6', name: 'Elena Rostova', role: 'dev' },
  { id: 'dummy_7', name: 'Venkatesh S', role: 'analyst' },
  { id: 'dummy_8', name: 'Ananya Roy', role: 'analyst' },
  { id: 'dummy_9', name: 'David Chen', role: 'scientist' },
  { id: 'dummy_10', name: 'Sneha Patel', role: 'scientist' },
  { id: 'dummy_11', name: 'Rohan Verma', role: 'dev' },
  { id: 'dummy_12', name: 'Divya Nair', role: 'analyst' }
];

function updateLeaderboard() {
  const sortedTeams = [...gameState.teams].sort((a, b) => b.score - a.score).map((t, idx) => ({
    rank: idx + 1,
    id: t.id,
    name: t.name,
    color: t.color,
    score: t.score,
    correctCount: t.correctCount || 0,
    wrongCount: t.wrongCount || 0,
    members: t.members
  }));

  const playerList = Object.values(gameState.players);
  const sortedPlayers = playerList
    .filter(p => p.name)
    .sort((a, b) => (b.score || 0) - (a.score || 0) || (b.correctCount || 0) - (a.correctCount || 0))
    .map((p, idx) => ({
      rank: idx + 1,
      id: p.id,
      name: p.name,
      role: p.role || 'dev',
      teamId: p.teamId,
      teamName: p.teamName || 'Team',
      score: p.score || 0,
      correctCount: p.correctCount || 0,
      wrongCount: p.wrongCount || 0
    }));

  gameState.leaderboard = {
    teams: sortedTeams,
    players: sortedPlayers
  };
}

function seedDummyPlayers() {
  DUMMY_PLAYERS.forEach(d => {
    gameState.players[d.id] = {
      id: d.id,
      name: d.name,
      role: d.role,
      teamId: null,
      teamName: null,
      score: 0,
      correctCount: 0,
      wrongCount: 0
    };
  });
  autoShuffleTeams();
  updateLeaderboard();
}

// MIME types
const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.svg': 'image/svg+xml'
};

const server = http.createServer((req, res) => {
  let reqUrl = req.url.split('?')[0];
  if (reqUrl === '/') reqUrl = '/smartboard.html';

  const filePath = path.join(PUBLIC_DIR, reqUrl);
  const ext = path.extname(filePath).toLowerCase();
  const contentType = MIME_TYPES[ext] || 'application/octet-stream';

  fs.readFile(filePath, (err, content) => {
    if (err) {
      if (err.code === 'ENOENT') {
        res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
        res.end('404 Not Found');
      } else {
        res.writeHead(500, { 'Content-Type': 'text/plain; charset=utf-8' });
        res.end('500 Server Error: ' + err.code);
      }
    } else {
      res.writeHead(200, {
        'Content-Type': contentType,
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Pragma': 'no-cache',
        'Expires': '0'
      });
      res.end(content, 'utf-8');
    }
  });
});

const wss = new WebSocketServer({ server });

// Keepalive Ping/Pong Heartbeat to keep 50+ mobile 4G/5G connections active without drops
const pingInterval = setInterval(() => {
  wss.clients.forEach(client => {
    if (client.isAlive === false) {
      return client.terminate();
    }
    client.isAlive = false;
    try {
      client.ping();
    } catch (e) {}
  });
}, 25000);

wss.on('close', () => {
  clearInterval(pingInterval);
});

function broadcast(msgObj) {
  const json = JSON.stringify(msgObj);
  wss.clients.forEach(client => {
    if (client.readyState === 1) { // 1 = OPEN
      try {
        client.send(json, (err) => {
          if (err) {
            // Ignore dropped socket error cleanly
          }
        });
      } catch (err) {
        // Safe catch: one disconnected phone will never crash the server
      }
    }
  });
}

function broadcastState() {
  updateLeaderboard();
  broadcast({
    type: 'STATE_UPDATE',
    state: {
      currentView: gameState.currentView,
      currentRoundIdx: gameState.currentRoundIdx,
      currentQuestionIdx: gameState.currentQuestionIdx,
      buzzerState: gameState.buzzerState,
      buzzerQueue: gameState.buzzerQueue,
      lockedTeamsForQuestion: gameState.lockedTeamsForQuestion,
      activeAnsweringTeamId: gameState.activeAnsweringTeamId,
      activeAnsweringPlayerId: gameState.activeAnsweringPlayerId,
      answerCountdown: gameState.answerCountdown,
      lastAnswerResult: gameState.lastAnswerResult,
      teams: gameState.teams,
      players: gameState.players,
      leaderboard: gameState.leaderboard,
      playerCount: Object.keys(gameState.players).length,
      debateState: gameState.debateState,
      networkIp: getLocalIp()
    }
  });
}

function autoShuffleTeams() {
  const playerList = Object.values(gameState.players);
  const count = playerList.length;
  if (count === 0) return;

  const numTeams = 4;
  gameState.teams.forEach(t => t.members = []);

  // General random shuffle across all joined students (no role bias)
  const shuffled = [...playerList].sort(() => Math.random() - 0.5);

  shuffled.forEach((p, idx) => {
    const teamIdx = idx % numTeams;
    const team = gameState.teams[teamIdx];
    p.teamId = team.id;
    p.teamName = team.name;
    team.members.push({ id: p.id, name: p.name, role: p.role || 'player' });
  });

  updateLeaderboard();
  console.log(`General random shuffle: distributed ${count} players across 4 teams.`);
}

function assignNewPlayerToTeam(player) {
  // Balanced Round-Robin Assignment: Always assign to the team with the fewest members!
  // Never reshuffle existing players so their team remains permanent!
  let targetTeam = gameState.teams[0];
  let minMembers = gameState.teams[0].members.length;
  gameState.teams.forEach(t => {
    if (t.members.length < minMembers) {
      minMembers = t.members.length;
      targetTeam = t;
    }
  });

  player.teamId = targetTeam.id;
  player.teamName = targetTeam.name;
  targetTeam.members.push({ id: player.id, name: player.name, role: player.role || 'player' });
  updateLeaderboard();
  console.log(`Player '${player.name}' permanently assigned to ${targetTeam.name} (Team count: ${targetTeam.members.length})`);
}

// Initial seed (Disabled for live student session - students join dynamically!)
// seedDummyPlayers();

let answerTimerInterval = null;

function clearAnswerTimer() {
  if (answerTimerInterval) {
    clearInterval(answerTimerInterval);
    answerTimerInterval = null;
  }
}

function startAnswerTimer() {
  clearAnswerTimer();
  gameState.answerCountdown = 10;

  answerTimerInterval = setInterval(() => {
    if (gameState.buzzerState !== 'buzzing' || !gameState.activeAnsweringTeamId) {
      clearAnswerTimer();
      return;
    }

    gameState.answerCountdown--;
    broadcastState();

    if (gameState.answerCountdown <= 0) {
      clearAnswerTimer();
      handleAnswerTimeout();
    }
  }, 1000);
}

function handleAnswerTimeout() {
  const teamId = gameState.activeAnsweringTeamId;
  const playerId = gameState.activeAnsweringPlayerId;
  const team = gameState.teams.find(t => t.id === teamId);
  const player = playerId ? gameState.players[playerId] : null;

  if (team) {
    team.score = Math.max(0, team.score - 20);
    team.wrongCount = (team.wrongCount || 0) + 1;
    gameState.lockedTeamsForQuestion.push(team.id);
  }
  if (player) {
    player.wrongCount = (player.wrongCount || 0) + 1;
  }

  const currentRound = allRounds[gameState.currentRoundIdx];
  const currentQ = currentRound ? currentRound.questions[gameState.currentQuestionIdx] : null;

  gameState.lastAnswerResult = {
    status: 'timeout',
    teamId: team ? team.id : null,
    teamName: team ? team.name : 'Team',
    playerName: player ? player.name : (team ? team.name : 'Team'),
    correctOptionIndex: currentQ ? currentQ.ans : null,
    ansText: currentQ ? currentQ.ansText : '',
    message: `⏰ TIME'S UP! ${team ? team.name : 'Team'} took >10s! (-20 PTS)`,
    time: Date.now()
  };

  if (team) {
    gameState.buzzerQueue = gameState.buzzerQueue.filter(b => b.teamId !== team.id);
  }

  // Check 2-Chance Rule: If 2 teams have attempted (and failed/timed out)
  if (gameState.lockedTeamsForQuestion.length >= 2) {
    console.log(`Question attempt limit reached (2 teams failed/timed out). Auto-locking question and revealing answer.`);
    gameState.buzzerState = 'locked';
    gameState.buzzerQueue = [];
    gameState.activeAnsweringTeamId = null;
    gameState.activeAnsweringPlayerId = null;
    gameState.lastAnswerResult = {
      status: 'max_attempts_exceeded',
      teamId: team ? team.id : null,
      teamName: team ? team.name : 'Team',
      playerName: player ? player.name : (team ? team.name : 'Team'),
      correctOptionIndex: currentQ ? currentQ.ans : null,
      ansText: currentQ ? currentQ.ansText : '',
      message: `2 Teams failed! Revealing correct answer...`,
      time: Date.now()
    };
  } else if (gameState.buzzerQueue.length > 0) {
    const nextBuzzed = gameState.buzzerQueue[0];
    gameState.activeAnsweringTeamId = nextBuzzed.teamId;
    gameState.activeAnsweringPlayerId = nextBuzzed.playerId;
    gameState.buzzerState = 'buzzing';
    startAnswerTimer();
  } else {
    gameState.activeAnsweringTeamId = null;
    gameState.activeAnsweringPlayerId = null;
    gameState.buzzerState = 'open';
  }

  updateLeaderboard();
  broadcastState();
}

function processAnswerSubmission(teamId, playerId, selectedOptionIndex, textAnswer) {
  clearAnswerTimer();
  const currentRound = allRounds[gameState.currentRoundIdx];
  const currentQ = currentRound ? currentRound.questions[gameState.currentQuestionIdx] : null;
  if (!currentQ) return;

  const team = gameState.teams.find(t => t.id === teamId);
  const player = playerId ? gameState.players[playerId] : null;

  let isCorrect = false;
  if (currentRound.type === 'connections') {
    const userText = (textAnswer || '').trim().toLowerCase();
    const correctText = (currentQ.ansText || '').trim().toLowerCase();
    if (selectedOptionIndex === 'AUTO_CORRECT' || textAnswer === 'AUTO_CORRECT' || (currentQ.ansText && textAnswer === currentQ.ansText)) {
      isCorrect = true;
    } else if (currentQ.ans !== undefined && selectedOptionIndex !== undefined && selectedOptionIndex === currentQ.ans) {
      isCorrect = true;
    } else if (userText && correctText && (correctText.includes(userText) || userText.includes(correctText.split(' ')[0]))) {
      isCorrect = true;
    }
  } else if (currentRound.type === 'fact_fiction' || currentRound.type === 'mcq' || currentRound.type === 'millionaire' || currentRound.type === 'rapid' || currentRound.type === 'imposter') {
    isCorrect = (selectedOptionIndex === currentQ.ans);
  } else {
    const userText = (textAnswer || '').trim().toLowerCase();
    const correctText = (currentQ.ansText || '').trim().toLowerCase();
    isCorrect = userText && (correctText.includes(userText) || userText.includes(correctText.split(' ')[0]));
  }

  if (isCorrect) {
    if (team) {
      team.score += 100;
      team.correctCount = (team.correctCount || 0) + 1;
    }
    if (player) {
      player.score = (player.score || 0) + 100;
      player.correctCount = (player.correctCount || 0) + 1;
    }

    gameState.lastAnswerResult = {
      status: 'correct',
      teamId: team ? team.id : null,
      teamName: team ? team.name : 'Team',
      playerName: player ? player.name : (team ? team.name : 'Team'),
      selectedOptionIndex: selectedOptionIndex,
      correctOptionIndex: currentQ.ans,
      message: `${team ? team.name : 'Team'} answered CORRECTLY! (+100 PTS)`,
      time: Date.now()
    };
    gameState.buzzerState = 'locked';
  } else {
    if (team) {
      team.score = Math.max(0, team.score - 20);
      team.wrongCount = (team.wrongCount || 0) + 1;
      gameState.lockedTeamsForQuestion.push(team.id);
    }
    if (player) {
      player.wrongCount = (player.wrongCount || 0) + 1;
    }

    gameState.lastAnswerResult = {
      status: 'wrong',
      teamId: team ? team.id : null,
      teamName: team ? team.name : 'Team',
      playerName: player ? player.name : (team ? team.name : 'Team'),
      selectedOptionIndex: selectedOptionIndex,
      correctOptionIndex: currentQ.ans,
      message: `${team ? team.name : 'Team'} WRONG! (-20 PTS)`,
      time: Date.now()
    };

    if (team) {
      gameState.buzzerQueue = gameState.buzzerQueue.filter(b => b.teamId !== team.id);
    }

    // 2-CHANCE ATTEMPT RULE: Maximum 2 teams can attempt each question!
    if (gameState.lockedTeamsForQuestion.length >= 2) {
      console.log(`Question attempt limit reached (2 teams failed). Auto-locking question and revealing answer.`);
      gameState.buzzerState = 'locked';
      gameState.buzzerQueue = [];
      gameState.activeAnsweringTeamId = null;
      gameState.activeAnsweringPlayerId = null;
      gameState.lastAnswerResult = {
        status: 'max_attempts_exceeded',
        teamId: team ? team.id : null,
        teamName: team ? team.name : 'Team',
        playerName: player ? player.name : (team ? team.name : 'Team'),
        selectedOptionIndex: selectedOptionIndex,
        correctOptionIndex: currentQ.ans,
        message: `2 Teams answered incorrectly! Revealing correct answer...`,
        time: Date.now()
      };
    } else if (gameState.buzzerQueue.length > 0) {
      const nextBuzzed = gameState.buzzerQueue[0];
      gameState.activeAnsweringTeamId = nextBuzzed.teamId;
      gameState.activeAnsweringPlayerId = nextBuzzed.playerId;
      gameState.buzzerState = 'buzzing';
      startAnswerTimer();
    } else {
      gameState.activeAnsweringTeamId = null;
      gameState.activeAnsweringPlayerId = null;
      gameState.buzzerState = 'open';
    }
  }

  updateLeaderboard();
  broadcastState();
}

wss.on('connection', (ws) => {
  ws.isAlive = true;
  ws.on('pong', () => { ws.isAlive = true; });
  ws.on('error', (err) => {
    // Graceful error handling for mobile drops
  });

  const playerId = 'p_' + Math.random().toString(36).substr(2, 9);
  ws.playerId = playerId;

  updateLeaderboard();
  ws.send(JSON.stringify({
    type: 'INIT',
    playerId: playerId,
    state: {
      currentView: gameState.currentView,
      currentRoundIdx: gameState.currentRoundIdx,
      currentQuestionIdx: gameState.currentQuestionIdx,
      buzzerState: gameState.buzzerState,
      buzzerQueue: gameState.buzzerQueue,
      lockedTeamsForQuestion: gameState.lockedTeamsForQuestion,
      activeAnsweringTeamId: gameState.activeAnsweringTeamId,
      activeAnsweringPlayerId: gameState.activeAnsweringPlayerId,
      answerCountdown: gameState.answerCountdown,
      lastAnswerResult: gameState.lastAnswerResult,
      teams: gameState.teams,
      players: gameState.players,
      leaderboard: gameState.leaderboard,
      playerCount: Object.keys(gameState.players).length,
      debateState: gameState.debateState,
      networkIp: getLocalIp()
    }
  }));

  ws.on('message', (message) => {
    try {
      const data = JSON.parse(message);

      switch (data.type) {
        case 'REGISTER_PLAYER': {
          const rawName = (data.name || 'Player').trim();
          const cleanNameLower = rawName.toLowerCase();

          // Block auto-register if player was kicked by host
          if (gameState.kickedPlayers && (gameState.kickedPlayers.has(ws.playerId) || gameState.kickedPlayers.has(cleanNameLower))) {
            try { ws.send(JSON.stringify({ type: 'YOU_WERE_REMOVED' })); } catch (e) {}
            return;
          }

          // Check if player name already exists to prevent duplicate entries & preserve permanent team
          let existingPlayer = Object.values(gameState.players).find(p => p.name && p.name.trim().toLowerCase() === cleanNameLower);

          if (existingPlayer) {
            // Re-bind current socket to the existing player record
            ws.playerId = existingPlayer.id;
            existingPlayer.role = data.role || existingPlayer.role;
            console.log(`Re-bound socket to existing player profile: ${existingPlayer.name} in ${existingPlayer.teamName}`);
          } else {
            const pid = data.playerId || ws.playerId;
            ws.playerId = pid;
            const newPlayer = {
              id: pid,
              name: rawName,
              role: data.role || 'dev',
              teamId: null,
              teamName: null,
              score: 0,
              correctCount: 0,
              wrongCount: 0
            };
            gameState.players[pid] = newPlayer;
            assignNewPlayerToTeam(newPlayer);
          }
          broadcastState();
          break;
        }

        case 'RECONNECT_PLAYER': {
          const pid = data.playerId || ws.playerId;
          ws.playerId = pid;

          // Block auto-reconnect if player was kicked by host
          if (gameState.kickedPlayers && (gameState.kickedPlayers.has(pid) || (data.name && gameState.kickedPlayers.has(data.name.toLowerCase())))) {
            try { ws.send(JSON.stringify({ type: 'YOU_WERE_REMOVED' })); } catch (e) {}
            return;
          }

          let player = gameState.players[pid];
          if (!player && data.name) {
            player = Object.values(gameState.players).find(p => p.name.toLowerCase() === data.name.toLowerCase());
            if (player) {
              delete gameState.players[player.id];
              player.id = pid;
              gameState.players[pid] = player;
            }
          }

          if (!player) {
            const reconnectedPlayer = {
              id: pid,
              name: data.name || 'Player',
              role: data.role || 'dev',
              teamId: null,
              teamName: null,
              score: 0,
              correctCount: 0,
              wrongCount: 0
            };
            gameState.players[pid] = reconnectedPlayer;
            assignNewPlayerToTeam(reconnectedPlayer);
          } else {
            if (data.name) player.name = data.name;
            if (data.role) player.role = data.role;
          }
          updateLeaderboard();
          broadcastState();
          break;
        }

        case 'SHUFFLE_TEAMS': {
          autoShuffleTeams();
          broadcastState();
          break;
        }

        case 'START_GAME': {
          gameState.currentView = 'game';
          gameState.currentRoundIdx = 0;
          gameState.currentQuestionIdx = 0;
          gameState.buzzerState = 'locked';
          gameState.buzzerQueue = [];
          gameState.lockedTeamsForQuestion = [];
          gameState.activeAnsweringTeamId = null;
          gameState.activeAnsweringPlayerId = null;
          gameState.lastAnswerResult = null;
          broadcastState();
          break;
        }

        case 'KICK_PLAYER': {
          const pid = data.playerId;
          const targetPlayer = gameState.players[pid];
          const targetName = targetPlayer ? targetPlayer.name : null;

          if (gameState.players[pid]) {
            delete gameState.players[pid];
          }
          gameState.teams.forEach(t => {
            t.members = t.members.filter(m => m.id !== pid);
          });
          gameState.buzzerQueue = gameState.buzzerQueue.filter(b => b.playerId !== pid);

          if (!gameState.kickedPlayers) gameState.kickedPlayers = new Set();
          gameState.kickedPlayers.add(pid);
          if (targetName) gameState.kickedPlayers.add(targetName.toLowerCase());

          // Tell the kicked client to clear and disconnect
          wss.clients.forEach(client => {
            if (client.playerId === pid) {
              try {
                client.send(JSON.stringify({ type: 'YOU_WERE_REMOVED' }));
                client.playerId = null;
              } catch (e) {}
            }
          });
          updateLeaderboard();
          broadcastState();
          break;
        }

        case 'CHANGE_QUESTION': {
          clearAnswerTimer();
          gameState.currentRoundIdx = data.roundIdx;
          gameState.currentQuestionIdx = data.questionIdx;
          gameState.buzzerState = 'locked';
          gameState.buzzerQueue = [];
          gameState.lockedTeamsForQuestion = [];
          gameState.activeAnsweringTeamId = null;
          gameState.activeAnsweringPlayerId = null;
          gameState.answerCountdown = 10;
          gameState.lastAnswerResult = null;
          broadcastState();
          break;
        }

        case 'OPEN_BUZZER': {
          clearAnswerTimer();
          gameState.buzzerState = 'open';
          gameState.buzzerQueue = [];
          gameState.activeAnsweringTeamId = null;
          gameState.activeAnsweringPlayerId = null;
          gameState.answerCountdown = 10;
          gameState.lastAnswerResult = null;
          broadcastState();
          break;
        }

        case 'PLAYER_BUZZ': {
          const player = gameState.players[ws.playerId];
          if (!player || !player.teamId) return;

          if (gameState.buzzerState !== 'open') return;
          if (gameState.lockedTeamsForQuestion.includes(player.teamId)) return;

          const teamAlreadyBuzzed = gameState.buzzerQueue.some(b => b.teamId === player.teamId);
          if (teamAlreadyBuzzed) return;

          gameState.buzzerQueue.push({
            playerId: player.id,
            playerName: player.name,
            teamId: player.teamId,
            teamName: player.teamName,
            time: Date.now()
          });

          if (!gameState.activeAnsweringTeamId) {
            gameState.activeAnsweringTeamId = player.teamId;
            gameState.activeAnsweringPlayerId = player.id;
            startAnswerTimer();
          }

          gameState.buzzerState = 'buzzing';
          broadcastState();
          break;
        }

        case 'SUBMIT_STUDENT_ANSWER': {
          const player = gameState.players[ws.playerId];
          if (!player || player.teamId !== gameState.activeAnsweringTeamId) return;
          processAnswerSubmission(player.teamId, player.id, data.selectedOptionIndex, data.textAnswer);
          break;
        }

        case 'SMARTBOARD_SELECT_OPTION': {
          const activeTeamId = gameState.activeAnsweringTeamId || (gameState.buzzerQueue[0] ? gameState.buzzerQueue[0].teamId : (gameState.teams[0] ? gameState.teams[0].id : null));
          processAnswerSubmission(activeTeamId, null, data.selectedOptionIndex, null);
          break;
        }

        case 'SKIP_CURRENT_TURN': {
          clearAnswerTimer();
          if (gameState.activeAnsweringTeamId) {
            gameState.lockedTeamsForQuestion.push(gameState.activeAnsweringTeamId);
            gameState.buzzerQueue = gameState.buzzerQueue.filter(b => b.teamId !== gameState.activeAnsweringTeamId);
            if (gameState.lockedTeamsForQuestion.length >= 2) {
              const curR = allRounds[gameState.currentRoundIdx];
              const curQ = curR ? curR.questions[gameState.currentQuestionIdx] : null;
              gameState.buzzerState = 'locked';
              gameState.buzzerQueue = [];
              gameState.activeAnsweringTeamId = null;
              gameState.activeAnsweringPlayerId = null;
              gameState.lastAnswerResult = {
                status: 'max_attempts_exceeded',
                message: `2 Teams skipped/locked! Revealing correct answer...`,
                correctOptionIndex: curQ ? curQ.ans : null,
                ansText: curQ ? curQ.ansText : '',
                time: Date.now()
              };
            } else if (gameState.buzzerQueue.length > 0) {
              const nextBuzzed = gameState.buzzerQueue[0];
              gameState.activeAnsweringTeamId = nextBuzzed.teamId;
              gameState.activeAnsweringPlayerId = nextBuzzed.playerId;
              gameState.buzzerState = 'buzzing';
              startAnswerTimer();
            } else {
              gameState.activeAnsweringTeamId = null;
              gameState.activeAnsweringPlayerId = null;
              gameState.buzzerState = 'open';
            }
            broadcastState();
          }
          break;
        }

        case 'SIMULATE_AUTO_PLAY': {
          // 1-Click Auto Demo: Unlocks buzzer, picks bot, buzzes, and submits answer automatically
          gameState.buzzerState = 'open';
          const playerList = Object.values(gameState.players);
          const eligible = playerList.filter(p => !gameState.lockedTeamsForQuestion.includes(p.teamId) && !gameState.buzzerQueue.some(b => b.teamId === p.teamId));
          const bot = (eligible.length > 0) ? eligible[Math.floor(Math.random() * eligible.length)] : (playerList[0] || null);

          if (bot) {
            gameState.buzzerQueue.push({
              playerId: bot.id,
              playerName: bot.name,
              teamId: bot.teamId,
              teamName: bot.teamName,
              time: Date.now()
            });
            gameState.activeAnsweringTeamId = bot.teamId;
            gameState.activeAnsweringPlayerId = bot.id;
            gameState.buzzerState = 'buzzing';
            broadcastState();

            // Auto submit correct answer after 1.2 seconds!
            setTimeout(() => {
              const curR = allRounds[gameState.currentRoundIdx];
              const curQ = curR ? curR.questions[gameState.currentQuestionIdx] : null;
              if (curQ && gameState.activeAnsweringTeamId === bot.teamId) {
                const optAns = curQ.ans !== undefined ? curQ.ans : 'AUTO_CORRECT';
                processAnswerSubmission(bot.teamId, bot.id, optAns, curQ.ansText);
              }
            }, 1200);
          }
          break;
        }

        case 'SIMULATE_BOT_BUZZ': {
          gameState.buzzerState = 'open';
          const playerList = Object.values(gameState.players);
          const eligible = playerList.filter(p => !gameState.lockedTeamsForQuestion.includes(p.teamId) && !gameState.buzzerQueue.some(b => b.teamId === p.teamId));
          if (eligible.length > 0) {
            const bot = eligible[Math.floor(Math.random() * eligible.length)];
            gameState.buzzerQueue.push({
              playerId: bot.id,
              playerName: bot.name,
              teamId: bot.teamId,
              teamName: bot.teamName,
              time: Date.now()
            });
            if (!gameState.activeAnsweringTeamId) {
              gameState.activeAnsweringTeamId = bot.teamId;
              gameState.activeAnsweringPlayerId = bot.id;
              startAnswerTimer();
            }
            gameState.buzzerState = 'buzzing';
            broadcastState();
          }
          break;
        }

        case 'HOST_MARK_CORRECT': {
          clearAnswerTimer();
          let awardedTeam = null;
          let awardedPlayer = null;

          if (gameState.activeAnsweringTeamId) {
            awardedTeam = gameState.teams.find(t => t.id === gameState.activeAnsweringTeamId);
            if (gameState.activeAnsweringPlayerId) {
              awardedPlayer = gameState.players[gameState.activeAnsweringPlayerId];
            }
          } else if (gameState.buzzerQueue.length > 0) {
            const first = gameState.buzzerQueue[0];
            awardedTeam = gameState.teams.find(t => t.id === first.teamId);
            awardedPlayer = gameState.players[first.playerId];
          }

          if (awardedTeam) {
            awardedTeam.score += 100;
            awardedTeam.correctCount = (awardedTeam.correctCount || 0) + 1;
          }
          if (awardedPlayer) {
            awardedPlayer.score = (awardedPlayer.score || 0) + 100;
            awardedPlayer.correctCount = (awardedPlayer.correctCount || 0) + 1;
          }

          const curR = allRounds[gameState.currentRoundIdx];
          const curQ = curR ? curR.questions[gameState.currentQuestionIdx] : null;

          gameState.lastAnswerResult = {
            status: 'correct',
            teamId: awardedTeam ? awardedTeam.id : null,
            teamName: awardedTeam ? awardedTeam.name : 'Team',
            playerName: awardedPlayer ? awardedPlayer.name : '',
            message: `${awardedTeam ? awardedTeam.name : 'Team'} answered CORRECTLY! (+100 PTS)`,
            ansText: curQ ? curQ.ansText : '',
            time: Date.now()
          };
          gameState.buzzerState = 'locked';
          updateLeaderboard();
          broadcastState();
          break;
        }

        case 'HOST_MARK_WRONG': {
          clearAnswerTimer();
          if (gameState.activeAnsweringTeamId) {
            const team = gameState.teams.find(t => t.id === gameState.activeAnsweringTeamId);
            if (team) {
              team.score = Math.max(0, team.score - 20);
              team.wrongCount = (team.wrongCount || 0) + 1;
            }

            gameState.lockedTeamsForQuestion.push(gameState.activeAnsweringTeamId);
            gameState.lastAnswerResult = {
              status: 'wrong',
              teamId: gameState.activeAnsweringTeamId,
              teamName: team ? team.name : 'Team',
              message: `${team ? team.name : 'Team'} WRONG! (-20 PTS)`,
              time: Date.now()
            };

            gameState.buzzerQueue = gameState.buzzerQueue.filter(b => b.teamId !== gameState.activeAnsweringTeamId);

            // 2-CHANCE ATTEMPT RULE: Maximum 2 teams can attempt each question!
            if (gameState.lockedTeamsForQuestion.length >= 2) {
              const curR = allRounds[gameState.currentRoundIdx];
              const curQ = curR ? curR.questions[gameState.currentQuestionIdx] : null;
              gameState.buzzerState = 'locked';
              gameState.buzzerQueue = [];
              gameState.activeAnsweringTeamId = null;
              gameState.activeAnsweringPlayerId = null;
              gameState.lastAnswerResult = {
                status: 'max_attempts_exceeded',
                teamId: team ? team.id : null,
                teamName: team ? team.name : 'Team',
                message: `2 Teams answered incorrectly! Revealing correct answer...`,
                correctOptionIndex: curQ ? curQ.ans : null,
                ansText: curQ ? curQ.ansText : '',
                time: Date.now()
              };
            } else if (gameState.buzzerQueue.length > 0) {
              const nextBuzzed = gameState.buzzerQueue[0];
              gameState.activeAnsweringTeamId = nextBuzzed.teamId;
              gameState.activeAnsweringPlayerId = nextBuzzed.playerId;
              gameState.buzzerState = 'buzzing';
              startAnswerTimer();
            } else {
              gameState.activeAnsweringTeamId = null;
              gameState.activeAnsweringPlayerId = null;
              gameState.buzzerState = 'open';
            }
          }
          updateLeaderboard();
          broadcastState();
          break;
        }

        case 'ADJUST_SCORE':
        case 'ADD_SCORE': {
          const team = gameState.teams.find(t => t.id === data.teamId);
          if (team) {
            const delta = (data.points !== undefined) ? data.points : 50;
            team.score = Math.max(0, team.score + delta);
            console.log(`Manual score adjustment for ${team.name}: ${delta >= 0 ? '+' : ''}${delta} (New total: ${team.score})`);
          }
          updateLeaderboard();
          broadcastState();
          break;
        }

        case 'DECLARE_WINNER': {
          clearAnswerTimer();
          gameState.currentView = 'winner';
          broadcastState();
          break;
        }

        case 'RESET_ALL': {
          clearAnswerTimer();
          gameState.currentView = 'lobby';
          gameState.currentRoundIdx = 0;
          gameState.currentQuestionIdx = 0;
          gameState.buzzerState = 'locked';
          gameState.buzzerQueue = [];
          gameState.lockedTeamsForQuestion = [];
          gameState.activeAnsweringTeamId = null;
          gameState.activeAnsweringPlayerId = null;
          gameState.answerCountdown = 10;
          gameState.lastAnswerResult = null;
          gameState.teams.forEach(t => { t.score = 0; t.correctCount = 0; t.wrongCount = 0; t.members = []; });
          gameState.players = {};
          gameState.kickedPlayers = new Set();
          updateLeaderboard();
          broadcastState();
          break;
        }
      }
    } catch (e) {
      console.error('Error handling WS message:', e);
    }
  });

  ws.on('close', () => {
    // Keep player profile in memory so student can reconnect seamlessly after phone calls or tab switch!
  });
});

function getLocalIp() {
  const ifaces = os.networkInterfaces();
  for (const name of Object.keys(ifaces)) {
    for (const iface of ifaces[name]) {
      if (iface.family === 'IPv4' && !iface.internal) {
        return iface.address;
      }
    }
  }
  return '127.0.0.1';
}

server.listen(PORT, '0.0.0.0', () => {
  const ip = getLocalIp();
  console.log('==================================================');
  console.log('⚡ TECH CLASH ARENA PRO IS LIVE & READY!');
  console.log(`🖥️ Smartboard View: http://localhost:${PORT}/smartboard.html`);
  console.log(`📱 Mobile Player View: http://${ip}:${PORT}/player.html`);
  console.log('==================================================');
});

const http = require('http');
const fs = require('fs');
const path = require('path');
const os = require('os');
const { WebSocketServer } = require('ws');

const PORT = 3000;
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
  lastAnswerResult: null, // { status: 'correct'|'wrong', teamId, teamName, time }
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
  }
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
      res.writeHead(200, { 'Content-Type': contentType });
      res.end(content, 'utf-8');
    }
  });
});

const wss = new WebSocketServer({ server });

function broadcast(msgObj) {
  const json = JSON.stringify(msgObj);
  wss.clients.forEach(client => {
    if (client.readyState === 1) {
      client.send(json);
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

  let numTeams = 4;
  if (count <= 5) numTeams = 2;
  else if (count <= 9) numTeams = 3;
  else numTeams = 4;

  gameState.teams.forEach(t => t.members = []);

  const devs = playerList.filter(p => p.role === 'dev');
  const analysts = playerList.filter(p => p.role === 'analyst');
  const scientists = playerList.filter(p => p.role === 'scientist');
  const general = playerList.filter(p => !['dev', 'analyst', 'scientist'].includes(p.role));

  const sortedPool = [...scientists, ...analysts, ...devs, ...general];

  sortedPool.forEach((p, idx) => {
    const teamIdx = idx % numTeams;
    const team = gameState.teams[teamIdx];
    p.teamId = team.id;
    p.teamName = team.name;
    team.members.push({ id: p.id, name: p.name, role: p.role });
  });

  updateLeaderboard();
  console.log(`Auto-shuffled ${count} players into ${numTeams} teams.`);
}

// Initial seed
seedDummyPlayers();

let allRounds = [];
try {
  allRounds = JSON.parse(fs.readFileSync(path.join(PUBLIC_DIR, 'questions.json'), 'utf8'));
} catch (e) {
  console.error('Error loading questions in server.js:', e);
}

function processAnswerSubmission(teamId, playerId, selectedOptionIndex, textAnswer) {
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
  } else if (currentRound.type === 'mcq' || currentRound.type === 'millionaire' || currentRound.type === 'rapid' || currentRound.type === 'imposter') {
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

    if (gameState.buzzerQueue.length > 0) {
      const nextBuzzed = gameState.buzzerQueue[0];
      gameState.activeAnsweringTeamId = nextBuzzed.teamId;
      gameState.activeAnsweringPlayerId = nextBuzzed.playerId;
      gameState.buzzerState = 'buzzing';
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
          gameState.players[ws.playerId] = {
            id: ws.playerId,
            name: data.name || 'Player',
            role: data.role || 'dev',
            teamId: null,
            teamName: null,
            score: 0,
            correctCount: 0,
            wrongCount: 0
          };
          autoShuffleTeams();
          broadcastState();
          break;
        }

        case 'RECONNECT_PLAYER': {
          const pid = data.playerId;
          ws.playerId = pid;
          if (!gameState.players[pid]) {
            gameState.players[pid] = {
              id: pid,
              name: data.name || 'Player',
              role: data.role || 'dev',
              teamId: null,
              teamName: null,
              score: 0,
              correctCount: 0,
              wrongCount: 0
            };
            autoShuffleTeams();
          } else {
            if (data.name) gameState.players[pid].name = data.name;
            if (data.role) gameState.players[pid].role = data.role;
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

        case 'CHANGE_QUESTION': {
          gameState.currentRoundIdx = data.roundIdx;
          gameState.currentQuestionIdx = data.questionIdx;
          gameState.buzzerState = 'locked';
          gameState.buzzerQueue = [];
          gameState.lockedTeamsForQuestion = [];
          gameState.activeAnsweringTeamId = null;
          gameState.activeAnsweringPlayerId = null;
          gameState.lastAnswerResult = null;
          broadcastState();
          break;
        }

        case 'OPEN_BUZZER': {
          gameState.buzzerState = 'open';
          gameState.buzzerQueue = [];
          gameState.activeAnsweringTeamId = null;
          gameState.activeAnsweringPlayerId = null;
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
          if (gameState.activeAnsweringTeamId) {
            gameState.lockedTeamsForQuestion.push(gameState.activeAnsweringTeamId);
            gameState.buzzerQueue = gameState.buzzerQueue.filter(b => b.teamId !== gameState.activeAnsweringTeamId);
            if (gameState.buzzerQueue.length > 0) {
              const nextBuzzed = gameState.buzzerQueue[0];
              gameState.activeAnsweringTeamId = nextBuzzed.teamId;
              gameState.activeAnsweringPlayerId = nextBuzzed.playerId;
              gameState.buzzerState = 'buzzing';
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
            }
            gameState.buzzerState = 'buzzing';
            broadcastState();
          }
          break;
        }

        case 'HOST_MARK_CORRECT': {
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
          if (gameState.activeAnsweringTeamId) {
            const team = gameState.teams.find(t => t.id === gameState.activeAnsweringTeamId);
            if (team) team.score = Math.max(0, team.score - 20);

            gameState.lockedTeamsForQuestion.push(gameState.activeAnsweringTeamId);
            gameState.lastAnswerResult = {
              status: 'wrong',
              teamId: gameState.activeAnsweringTeamId,
              time: Date.now()
            };

            gameState.buzzerQueue = gameState.buzzerQueue.filter(b => b.teamId !== gameState.activeAnsweringTeamId);

            if (gameState.buzzerQueue.length > 0) {
              const nextBuzzed = gameState.buzzerQueue[0];
              gameState.activeAnsweringTeamId = nextBuzzed.teamId;
              gameState.activeAnsweringPlayerId = nextBuzzed.playerId;
              gameState.buzzerState = 'buzzing';
            } else {
              gameState.activeAnsweringTeamId = null;
              gameState.activeAnsweringPlayerId = null;
              gameState.buzzerState = 'open';
            }
          }
          broadcastState();
          break;
        }

        case 'ADD_SCORE': {
          const team = gameState.teams.find(t => t.id === data.teamId);
          if (team) team.score += (data.points || 50);
          broadcastState();
          break;
        }

        case 'DECLARE_WINNER': {
          gameState.currentView = 'winner';
          broadcastState();
          break;
        }

        case 'RESET_ALL': {
          gameState.currentView = 'lobby';
          gameState.currentRoundIdx = 0;
          gameState.currentQuestionIdx = 0;
          gameState.buzzerState = 'locked';
          gameState.buzzerQueue = [];
          gameState.lockedTeamsForQuestion = [];
          gameState.activeAnsweringTeamId = null;
          gameState.activeAnsweringPlayerId = null;
          gameState.lastAnswerResult = null;
          gameState.teams.forEach(t => { t.score = 0; t.correctCount = 0; t.wrongCount = 0; t.members = []; });
          gameState.players = {};
          seedDummyPlayers();
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

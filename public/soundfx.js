// Web Audio Synthesizer for Zero-Asset Instant Sound Effects
class SoundFX {
  constructor() {
    this.ctx = null;
    this.init();
  }

  init() {
    try {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      this.ctx = new AudioContext();
    } catch (e) {
      console.warn('AudioContext not supported');
    }
  }

  ensureContext() {
    if (this.ctx && this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
  }

  // 1. Countdown Tick (3... 2...)
  playTick() {
    this.ensureContext();
    if (!this.ctx) return;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(600, this.ctx.currentTime);
    gain.gain.setValueAtTime(0.15, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.08);
    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start();
    osc.stop(this.ctx.currentTime + 0.08);
  }

  // 2. Buzzer Unlock Go! (1... GO!)
  playUnlock() {
    this.ensureContext();
    if (!this.ctx) return;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(880, this.ctx.currentTime);
    gain.gain.setValueAtTime(0.25, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.25);
    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start();
    osc.stop(this.ctx.currentTime + 0.25);
  }

  // 3. Buzzer Pressed Alert (Ding-Dong / Buzz)
  playBuzzer() {
    this.ensureContext();
    if (!this.ctx) return;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sawtooth';
    osc.frequency.setValueAtTime(450, this.ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(300, this.ctx.currentTime + 0.3);
    gain.gain.setValueAtTime(0.3, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + 0.3);
    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start();
    osc.stop(this.ctx.currentTime + 0.3);
  }

  // 4. Correct Answer Chime (Victory Harmony)
  playCorrect() {
    this.ensureContext();
    if (!this.ctx) return;
    const notes = [523.25, 659.25, 783.99, 1046.50]; // C5, E5, G5, C6
    notes.forEach((freq, idx) => {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, this.ctx.currentTime + idx * 0.08);
      gain.gain.setValueAtTime(0.2, this.ctx.currentTime + idx * 0.08);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + idx * 0.08 + 0.35);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(this.ctx.currentTime + idx * 0.08);
      osc.stop(this.ctx.currentTime + idx * 0.08 + 0.35);
    });
  }

  // 5. Wrong Answer Womp (Low Thud)
  playWrong() {
    this.ensureContext();
    if (!this.ctx) return;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sawtooth';
    osc.frequency.setValueAtTime(220, this.ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(110, this.ctx.currentTime + 0.4);
    gain.gain.setValueAtTime(0.25, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.4);
    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start();
    osc.stop(this.ctx.currentTime + 0.4);
  }

  // 6. Grand Winner Fanfare
  playFanfare() {
    this.ensureContext();
    if (!this.ctx) return;
    const melody = [
      { f: 523.25, t: 0 },
      { f: 523.25, t: 0.15 },
      { f: 523.25, t: 0.3 },
      { f: 659.25, t: 0.45 },
      { f: 783.99, t: 0.65 },
      { f: 1046.50, t: 0.9 }
    ];
    melody.forEach(note => {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(note.f, this.ctx.currentTime + note.t);
      gain.gain.setValueAtTime(0.3, this.ctx.currentTime + note.t);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + note.t + 0.5);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(this.ctx.currentTime + note.t);
      osc.stop(this.ctx.currentTime + note.t + 0.5);
    });
  }
}

window.soundFX = new SoundFX();

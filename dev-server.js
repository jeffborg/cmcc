const { exec } = require('child_process');
const bs = require('browser-sync').create();
const fs = require('fs');
const path = require('path');

const DIST = path.join(__dirname, 'dist');
const WATCH_GLOB = '{assets/**/*,content/**/*,build.py,site_data.py}';

bs.init({
  server: { baseDir: DIST },
  port: 8001,
  open: false,
  ghostMode: false,
});

bs.watch(WATCH_GLOB, (event, file) => {
  console.log(`\n${event}: ${path.relative(__dirname, file)}`);
  exec('python3 build.py', (err) => {
    if (err) {
      console.error('Build failed:', err.message);
      return;
    }
    console.log('Built successfully, reloading...');
    bs.reload();
  });
});

console.log('Live reload server running at http://localhost:8001');
console.log('Press Ctrl+C to stop');

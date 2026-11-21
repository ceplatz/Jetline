// Minimal static file server so the site can run on Firebase App Hosting (Cloud Run).
// No dependencies. Serves ./public. App Hosting provides PORT.
const http = require('http');
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, 'public');
const PORT = process.env.PORT || 8080;
const TYPES = {
  '.html': 'text/html; charset=utf-8', '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8', '.json': 'application/json; charset=utf-8',
  '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png', '.webp': 'image/webp',
  '.svg': 'image/svg+xml', '.ico': 'image/x-icon', '.txt': 'text/plain; charset=utf-8',
};
const SECURITY = {
  'X-Content-Type-Options': 'nosniff',
  'Referrer-Policy': 'strict-origin-when-cross-origin',
  'X-Frame-Options': 'SAMEORIGIN',
};

http.createServer((req, res) => {
  let pathname;
  try { pathname = decodeURIComponent(new URL(req.url, 'http://x').pathname); }
  catch { res.writeHead(400, SECURITY); return res.end('Bad request'); }

  // Lets the contact form find the Firebase web config, as it does on Firebase Hosting.
  // App Hosting sets FIREBASE_WEBAPP_CONFIG when a Firebase web app is linked to the backend.
  if (pathname === '/__/firebase/init.json') {
    if (process.env.FIREBASE_WEBAPP_CONFIG) {
      res.writeHead(200, { ...SECURITY, 'Content-Type': TYPES['.json'], 'Cache-Control': 'no-cache' });
      return res.end(process.env.FIREBASE_WEBAPP_CONFIG);
    }
    res.writeHead(404, SECURITY); return res.end('Not found');
  }

  if (req.method !== 'GET' && req.method !== 'HEAD') { res.writeHead(405, SECURITY); return res.end(); }

  let file = path.normalize(path.join(ROOT, pathname));
  if (!file.startsWith(ROOT + path.sep) && file !== ROOT) { res.writeHead(403, SECURITY); return res.end('Forbidden'); }
  if (pathname.endsWith('/')) file = path.join(file, 'index.html');

  fs.stat(file, (err, st) => {
    if (!err && st.isDirectory()) file = path.join(file, 'index.html');
    fs.readFile(file, (err2, data) => {
      if (err2) { res.writeHead(404, { ...SECURITY, 'Content-Type': TYPES['.txt'] }); return res.end('Not found'); }
      const ext = path.extname(file).toLowerCase();
      const cache = ext === '.html' ? 'no-cache' : 'public, max-age=86400';
      res.writeHead(200, { ...SECURITY, 'Content-Type': TYPES[ext] || 'application/octet-stream', 'Cache-Control': cache, 'Content-Length': data.length });
      res.end(req.method === 'HEAD' ? undefined : data);
    });
  });
}).listen(PORT, () => console.log('Jetline site listening on ' + PORT));

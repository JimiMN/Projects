const http = require('http');
const port = 3000;

http.createServer((req, res) => {
  const headers = {
    'Access-Control-Allow-origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, HEAD',
    'Access-Control-Max-Age': '7200'
  };

  if (!req.headers['origin']) {
    res.writeHead(400);
    res.write('Origin header not in the request');
    res.end();
  } else if (req.method == 'GET' || req.method == 'POST') {
    res.writeHead(200, headers);
    res.write('I was requested using CORS!')
    res.end();
  } else if (req.method == 'HEAD') {
    res.writeHead(200, headers);
    res.end();
  } else {
    res.writeHead(405, headers);
    res.write('Request used a HTTP method which is not allowed.');
    res.end();
  }
}).listen(port);
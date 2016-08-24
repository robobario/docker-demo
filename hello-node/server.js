var http = require('http')

var port = 8000

var server = http.createServer(function (request, response) {
  response.writeHead(200, {'Content-Type': 'text/plain'})
  response.end('Hello, world')
})

server.listen(port)

console.log('Server running at http://localhost:' + port)

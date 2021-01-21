# http.server is not recommended for production.
# It only implements basic security checks.

import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print('serving at port', PORT)
    httpd.serve_forever()

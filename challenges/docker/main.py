import http.server
import socketserver

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", 8080), Handler) as httpd:
    httpd.serve_forever()
import http.server
import socketserver

PORT = 6969

req_hand = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(('', PORT), req_hand) as httpd:
    print("Server at localhost:" + str(PORT))
    httpd.serve_forever()
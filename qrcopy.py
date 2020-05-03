import http.server
import socketserver
import pyqrcode
import socket
import sys

PORT = 6969

req_hand = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(('', PORT), req_hand) as httpd:
    file = ''
    if len(sys.argv)>1: file = sys.argv[1]
    url = f"{socket.gethostbyname(socket.gethostname())}:{PORT}/{file}"
    qr = pyqrcode.create(url)
    print(qr.terminal())
    print("Server at", url)
    httpd.serve_forever()
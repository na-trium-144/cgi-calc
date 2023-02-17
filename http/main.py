#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            path = "./index.html"
            mime = "text/html; charset=utf-8"
        elif self.path == "/main.js":
            path = "./main.js"
            mime = "application/javascript; charset=utf-8"
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'')
            return
        with open(path, "rb") as f:
            self.send_response(200)
            self.send_header('Content-Type', mime)
            self.end_headers()
            self.wfile.write(f.read())

    def do_POST(self):
        content_length = int(self.headers['content-length'])
        body = json.loads(self.rfile.read(content_length).decode('utf-8'))
        
        if body["operator"] == "+":
            ans = body["before"] + body["after"]
        if body["operator"] == "-":
            ans = body["before"] - body["after"]
        if body["operator"] == "*":
            ans = body["before"] * body["after"]
        if body["operator"] == "/":
            ans = body["before"] / body["after"]
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(str(ans).encode())

print("http://localhost:8080/")
with HTTPServer(('localhost', 8080), MyHTTPRequestHandler) as server:
    server.serve_forever()
from http.server import HTTPServer, BaseHTTPRequestHandler

class ServerHandler (BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Access-Control-Allow-Headers', 'X-Request-Width')
        self.end_headers()
        self.wfile.write(b'Hello <b>World!</b>')

if __name__ == '__main__':
    try:
        server = HTTPServer(('localhost', 8000), ServerHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('Server Interrupted...')
    finally:
        server.server_close()

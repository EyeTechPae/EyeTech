from http.server import HTTPServer, BaseHTTPRequestHandler

class ServerHandler (BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Connection', 'close')
        self.end_headers()
        self.wfile.write(b'<i>Hello</i> <b>World</b>')

if __name__ == '__main__':
    try:
        server = HTTPServer(('localhost', 8000), ServerHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('Server Interrupted...')
    finally:
        server.server_close()

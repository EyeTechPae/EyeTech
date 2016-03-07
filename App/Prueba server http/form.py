import cgi
from http.server import HTTPServer, BaseHTTPRequestHandler

class ServerHandler (BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Allow', 'GET, POST')
        self.end_headers()
        self.wfile.write(b'<form method="POST"><input name="data" type="text"/><button>compute</button></form>')

    def do_POST(self):
        post_vars = {}
        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
        if ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers.get('content-length'))
            post_vars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1) 

        self.send_response(200, 'OK')
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.send_header('Allow', 'GET, POST')
        self.end_headers()

        response = 'Form data: {}'.format(str(post_vars))
        self.wfile.write(response.encode())

if __name__ == '__main__':
    try:
        server = HTTPServer(('localhost', 8000), ServerHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('Server Interrupted...')
    finally:
        server.server_close()

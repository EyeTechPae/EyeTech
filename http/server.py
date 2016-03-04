from http.server import HTTPServer, BaseHTTPRequestHandler

class ServerHandler (BaseHTTPRequestHandler):
    
    def do_GET(self):
        # hay que seguir el protocolo y enviar manualmente la cabecera
        # creo que las funciones send_header hacen lo mismo que el wfile.write
        # pero de manera mas conveniente
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Access-Control-Allow-Headers', 'X-Request-Width')
        self.end_headers()
        
        # algo en html para que el navegador lo pinte
        self.wfile.write(b'Hello <b>World!</b>')

if __name__ == '__main__':
    try:
        # crea un servidor HTTP con el ServerHandler
        server = HTTPServer(('localhost', 8000), ServerHandler)
        # escuchar siempre
        server.serve_forever()
    except KeyboardInterrupt:
        print('Server Interrupted...')
    finally:
        # cerrar servidor
        server.server_close()

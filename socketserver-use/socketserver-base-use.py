#! /usr/bin/env python3

# base socketserver , no fork, no multithread
from socketserver import TCPServer, StreamRequestHandler


# compared to socketserver.BaseRequestHandler,
# StreamRequestHandler add wfile, rfile
class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()  # eg: addr = ('127.0.0.1', 57838)
        print('Got connection from', addr)
        self.wfile.write('Thank you for connecting\n'.encode('utf-8'))
        while True:
            print('ok\n')
            pass


server = TCPServer(('', 1234), Handler)
server.serve_forever()
# while(1) {listen(listenfd) --> fd = accept(...) 
# --> Handler.setup() --> Handler.handle() --> Handler.finish() --> close(fd) }
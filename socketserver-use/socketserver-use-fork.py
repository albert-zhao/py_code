# A fork server for test
from socketserver import TCPServer, ForkingMixIn, StreamRequestHandler


# ForkingMixIn overrided process_request method to fork a child process
class Server(ForkingMixIn, TCPServer):
    pass


class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()  # eg: addr = ('127.0.0.1', 57838)
        print('Got connection from', addr)
        self.wfile.write('Thank you for connecting\n'.encode())  # python3 str is unicode, but python2 is bytes, transfering need bytes
        while True:
            print('ok\n')
            pass


server = Server(('', 1234), Handler)
server.serve_forever()  # while(1) {listen(listenfd) --> fd = accept(...)  fork()  --> childprocrss{ Handler.handle() --> close(fd) } close(fd) }
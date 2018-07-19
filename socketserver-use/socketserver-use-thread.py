# A Threading Server for test
from socketserver import TCPServer, ThreadingMixIn, StreamRequestHandler

# ThreadingMinIn overrided process_request method to generate a new subthread
class Server(ThreadingMixIn, TCPServer):
    pass


class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()  # eg: addr = ('127.0.0.1', 57838)
        print('Got connection from', addr)
        self.wfile.write('Thank you for connecting\n'.encode())
        # while True:
        #     print('ok\n')
        #     pass


server = Server(('', 1234), Handler)
server.serve_forever()  # while(1) {listen(listenfd) --> fd = accept(...)  child-thread{ Handler.handle() --> close(fd) } }
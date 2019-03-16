# A Threading Server for test
from SocketServer import TCPServer, ThreadingMixIn, StreamRequestHandler
import time


# ThreadingMinIn overrided process_request method to generate a new subthread
class Server(ThreadingMixIn, TCPServer):
    pass


def getPacket(aSocket):
    # print('in getPacket')
    buf = aSocket.recv(1)  # get the first byte fixed header
    print(str(aSocket))
    if buf == b"":
        print('null')
        return None
    print(str(aSocket))
    if str(aSocket).find("[closed]") != -1: # error, not should use like it, str(aSocket) == '<socket._socketobject object at 0x7f5d6a7b2670>'
        print('closed')
        closed = True
    else:
        closed = False
        # print("not closed")
    if closed:
        return None
    while 1:
        print("before next")
        next = aSocket.recv(1)
        print(len(next))
        while len(next) == 0:
            print("here")
            next = aSocket.recv(1)
            time.sleep(1)


class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()  # eg: addr = ('127.0.0.1', 57838)
        print('Got connection from', addr)
        while True:
            # print('ok\n')
            getPacket(self.request)
            time.sleep(1)

server = Server(('', 1234), Handler)
server.serve_forever()  # while(1) {listen(listenfd) --> fd = accept(...)  child-thread{ Handler.handle() --> close(fd) } }
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory


class SimpleLogger(Protocol):
    def connectionMade(self):  # it will be invoked when new connection comes
        print('Got connection from', self.transport.client)

    def connectionLost(self, reason):
        print(self.transport.client, 'disconnected')  # it will be invoked when conneciton closed

    def dataReceived(self, data):  # when data comes, it will be invoked
        # print(data.decode())  # default 'utf-8'
        print(data)

if __name__ == '__main__':
    factory = Factory()
    factory.protocol = SimpleLogger
    reactor.listenTCP(1234, factory)
    reactor.run()
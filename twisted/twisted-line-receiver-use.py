from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver


class SimpleLogger(LineReceiver):
    def connectionMade(self):
        print('Got connection from', self.transport.client)

    def connectionLost(self, reason):
        print(self.transport.client, 'disconnected')

    def lineReceived(self, line):  #  dataReceived(self, data) call--> lineReceived(when receive data trailing '\r\n'), test use telnet ... or nc -C ...
        print(line) # line has removed trailing '\r\n',


factory = Factory()
factory.protocol = SimpleLogger
reactor.listenTCP(1234, factory)
reactor.run()
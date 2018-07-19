#! /usr/bin/env python3
import socketserver


# class socketserver.BaseRequestHandler

#     This is the superclass of all request handler objects. It defines the interface, given below. A concrete request handler subclass must define a new handle() method, and can override any of the other methods. A new instance of the subclass is created for each request.

#     setup()

#         Called before the handle() method to perform any initialization actions required. The default implementation does nothing.

#     handle()

#         This function must do all the work required to service a request. 
#         The default implementation does nothing. Several instance attributes are available to it; 
#         the request is available as self.request; the client address as self.client_address; and the server instance as self.server, in case it needs access to per-server information.

#         The type of self.request is different for datagram or stream services. For stream services, self.request is a socket object; for datagram services, self.request is a pair of string and socket.

#     finish()

#         Called after the handle() method to perform any clean-up actions required. The default implementation does nothing. If setup() raises an exception, this function will not be called.


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    # self.request --> file objects, self.client_address --> (ip, port)
    # self.server --> server instance
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} {} wrote:".format(self.client_address[0],
                                    self.client_address[1]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
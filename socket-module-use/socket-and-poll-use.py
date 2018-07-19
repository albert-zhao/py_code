import socket
import select

host = socket.gethostname()  # pc_zxl 127.0.1.1
s = socket.socket()
port = 1234
s.bind((host, port))
s.listen(5)
p = select.poll()
# register(fd [, eventmask] ) -> None
# fd -- either an integer, or an object with a fileno() method returning an int.
# p.register(s.fileno())
p.register(s)
fdmap = {s.fileno(): s}

while True:
    events = p.poll()  # list of (fd, event) 2-tuples
    for fd, event in events:
        if fd == s.fileno():
            c, addr = s.accept()  # accept() -> (socket object, address info)
            p.register(c)
            fdmap[c.fileno()] = c
            print('Got new connection from', addr)
        elif event & select.POLLIN:
            data = fdmap[fd].recv(1024)
            if not data:  # recv a closed signal from remote point
                p.unregister(fd)
                print('Disconnect with', fdmap[fd].getpeername())
                fdmap[fd].close()
                del fdmap[fd]
            else:
                print(data.decode())
                
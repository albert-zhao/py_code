import socket
import select


s = socket.socket()
host = socket.gethostname()
print('host is', host)
port = 1234
# s.bind((host, port))
s.bind(('127.0.0.1', port))
s.listen(5)
# s.setsockopt()? how to set when u want to reuse addr
read_seq = [s]
write_seq = []
err_seq = []

while True:
    rfd, wfd, errfd = select.select(read_seq, write_seq, err_seq)
    print(rfd)
    for fd in rfd:
        if fd is s:
            c, addr = fd.accept()
            read_seq.append(c)
            print('new connection is ', addr)
        else:
            try:  # why here need try? what error occured when invoking fd.recv(1024)?
                data = fd.recv(1024)
                disconnected = not data
            except socket.error:
                disconnected = True
            if disconnected:
                print('close connection', fd.getpeername())
                read_seq.remove(fd)
                fd.close()
            else:
                print('data is:', data.decode('utf-8'))


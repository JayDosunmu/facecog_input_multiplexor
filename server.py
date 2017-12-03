# signal mux
import socket

class Device:
    def __init__(self, addr, conn):
        pass

devices = {}

conn, addr = socket.accept()

devices[addr] = Device(addr, conn)




if __name__ == '__main__':
    host = ''
    post = 12345
    s = socket.socket(stream.AF_INET, socket.SOCK_STREAM)
    s.bind((host, post))
    s.listen(1)
    conn, addr = s.accept()

    print('Connected by', addr)

    while 1:
        data = conn.recv(1024)
        if not data:
            break
        else:
            print(repr(data))
    conn.close()

# signal mux
import socket
import sys


class Device:
    def __init__(self, addr, conn):
        pass


# devices = {}

# devices[addr] = Device(addr, conn)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        port = int(sys.argv[1])
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', port))
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
    else:
        print('Error starting server. Invalid arguments used\nreqd: host_name, port_number')

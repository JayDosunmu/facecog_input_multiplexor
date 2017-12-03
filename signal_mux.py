import socket

class Device:
    def __init__(self, addr, conn):
        pass

devices = {}

conn, addr = socket.accept()

devices[addr] = Device(addr, conn)



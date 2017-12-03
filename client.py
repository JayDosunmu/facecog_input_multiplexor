# keyboard simulator
import pyautogui
import socket
import sys


def register_device(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    return s


if __name__ == '__main__':
    if len(sys.argv) == 3:
        host = sys.argv[1]
        port = int(sys.argv[2])
        s = register_device(host, port)
        s.sendall('Connected to Device')

        while 1:
            data = s.recv(1024)
            print("data received: " + repr(data))
    else:
        print('ERROR: Incorrect number of arguments used. ' +
              'You must pass in the HOST and PORT of the endpoint to connect to\n' +
              'Example: python client.py host_name port_number')

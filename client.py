# keyboard simulator
import os
import socket
import sys
import traceback
import webbrowser

from pynput import keyboard

filename = 'index.html'
kb = keyboard.Controller()

def register(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    return s


def calibrate():
    webbrowser.open('file://' + os.path.realpath(filename))


if __name__ == '__main__':
    try:
        if len(sys.argv) == 3:
            control = keyboard.Controller()
            host = sys.argv[1]
            port = int(sys.argv[2])
            s = register(host, port)

            s.sendall('Connected to Device')

            data = s.recv(1024)
            print(repr(data))
            #kb.press(data)
            calibrate()

            while 1:
                print("waiting for data")
                data = s.recv(1024)

                print("data received: " + repr(data))
        else:
            print('ERROR: Incorrect number of arguments used. ' +
                  'You must pass in the HOST and PORT of the endpoint to connect to\n' +
                  'Example: python client.py host_name port_number')
    except:
        traceback.print_exc();
        # s.close()

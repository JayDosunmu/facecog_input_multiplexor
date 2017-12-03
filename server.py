# signal mux
# https://pypi.python.org/pypi/pynput

import socket
import sys
import traceback

from pynput import keyboard

kb = keyboard.Controller()


class Device:
    def __init__(self, addr, conn):
        self.addr = addr
        self.conn = conn

        self.tl = None
        self.bl = None
        self.br = None

    def add_tl():
        pass

    def add_bl():
        pass

    def add_br():
        pass


# devices[addr] = Device(addr, conn)
devices = {}
# save addr of focuesd device here
focused = None


def calibrate(device):
    """
        on each space press, snap an image.
        process the image using gVAPI 
        store the bounds in correct position 
    """
    pass


def on_press(key):
    kb.press(key)
    try:
        print key
        # if focused:
        #     conn = devices[focused]
        # conn.sendall(key.char)
        # print('alphanumeric key {0} pressed'.format(
        #     key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
        if focused:
            conn = devices[focused]
            conn.sendall(key.char)


def on_release(key):
    kb.release(key)
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released

if __name__ == '__main__':
    try:
        if len(sys.argv) == 2:
            port = int(sys.argv[1])
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(('', port))
            s.listen(1)
            listener = keyboard.Listener(
                        on_press=on_press,
                        on_release=on_release)
            listener.start()

            while 1:
                print("In while loop")
                conn, addr = s.accept()
                devices[addr] = conn
                print('Connected by', addr)

                if not focused:
                    focused = addr

                data = conn.recv(1024)
                if data:
                    print(repr(data))
                conn.sendall('Ready to calibrate')

            conn.close()
        else:
            print('Error starting server. Invalid arguments used\nreqd: port_number')
    except KeyboardInterrupt:
        s.close()
    except Exception as e:
        traceback.print_exc();
        s.close()

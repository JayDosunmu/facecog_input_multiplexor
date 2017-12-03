
from detect import detect_faces
from detect import detect_faces_uri

import sys

def oreintation(tilt, pan):
    out = False
    if tilt >= 3 and tilt <= 12:
        if pan <= 7 and pan >= 1:
            out  = 1
        elif pan >= -7 and pan <= -1 :
            out = 2
        else:
            out = out
    elif tilt <= -3 and tilt >= 12:
        if pan <= 7 and pan >= 1:
            out  = 3
        elif pan >= -7 and pan <= -1 :
            out = 4
        else:
            out = out
    else:
        out = out
    return out
    detect_faces(path)



if __name__ == "__main__":
    file = 'image002.jpg'
    if len(sys.argv) == 2:
        file = sys.argv[1]
    response = detect_faces(file)
#
    res = oreintation(response[0],response[1])

    print(res)
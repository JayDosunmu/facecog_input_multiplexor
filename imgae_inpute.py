from detect import detect_faces
from detect import detect_faces_uri





if __name__ == "__main__":
    file = 'image002.jpg'
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            file = sys.argv[i]
            response = detect_faces(file)

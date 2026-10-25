import cv2
import time

kamera = cv2.VideoCapture(0)
time.sleep(1)

def red(b,g,r):
    return (r > 150) & (r > 2*g) & (r > 2*b)

while True:

    ok, bild = kamera.read()
    if not ok:
        exit()
    b = bild[:, :, 0].astype(int)
    g = bild[:, :, 1].astype(int)
    r = bild[:, :, 2].astype(int)
    maske = red(b,g,r)        

    cv2.imshow("bild", bild)
    cv2.imshow("maske", maske.astype("uint8") * 255)

    if cv2.waitKey(1) == ord("q"):
        kamera.release()
        cv2.destroyAllWindows()
        break

   

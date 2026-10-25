import numpy as np
import cv2
import time

kamera = cv2.VideoCapture(0)
time.sleep(1)
last = None

def red(b,g,r):
    return (r > 100) & (r > 3*g) & (r > 2*b)

while True:

    ok, bild = kamera.read()
    bild = bild[::3, ::3].copy()
    if not ok:
        exit()
    b = bild[:, :, 0].astype(int)
    g = bild[:, :, 1].astype(int)
    r = bild[:, :, 2].astype(int)
    
    maske = red(b,g,r)        
    ys, xs = np.nonzero(maske)

    if len(xs) > 100:
        x = xs.mean()
        y = ys.mean()
        last = (int(x), int(y))
    if last is not None:
        cv2.drawMarker(bild,last, (0, 255, 0), cv2.MARKER_CROSS, 30, 2)
    
    cv2.imshow("bild", bild)
    cv2.imshow("maske", maske.astype("uint8") * 255)

    if cv2.waitKey(1) == ord("q"):
        kamera.release()
        cv2.destroyAllWindows()
        break

   

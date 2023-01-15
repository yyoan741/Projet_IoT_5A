from picamera import PiCamera
import datetime
from time import sleep, time

import qrcode
import cv2

debut = time()

camera = PiCamera()
camera.resolution=(1920, 1080)

sleep(2)
camera.capture('/home/admin/Documents/IoT/capt.png')
print("Prise de la capture ...\n")


img = cv2.imread("QR_CODE_PORTE_LOGS.jpg")
detector = cv2.QRCodeDetector()

print("Lancement du décodage ...\n")
data, bbox, straight_qrcode = detector.detectAndDecode(img)

if bbox is not None:
    print(f"QRCode data:{data}\n")
else :
    print("Aucun QR Code détecté\n")

if data is not None:
    f = open("logs.txt", "a")
    f.write(data)
    now = datetime.datetime.now()
    nowprint = now.strftime("%Y-%m-%d %H:%M:%S\n")
    f.write(" // Registered at : " + nowprint)
    f.close()

fin = time()
duree = fin - debut
print(f"Durée d'exécution:{duree}")

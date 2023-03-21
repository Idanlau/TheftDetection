import cv2
import cvzone
import numpy as np
from cvzone.ColorModule import ColorFinder
import picamera
from picamera.array import PiRGBArray

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(640, 480))

totalMoney = 0

myColorFinder = ColorFinder(False)
# Custom Orange Color
hsvVals = {'hmin': 0, 'smin': 0, 'vmin': 145, 'hmax': 63, 'smax': 91, 'vmax': 255}


def empty(a):
    pass


cv2.namedWindow("Settings")
cv2.resizeWindow("Settings", 800, 800)
cv2.createTrackbar("Threshold1", "Settings", 219, 255, empty)
cv2.createTrackbar("Threshold2", "Settings", 233, 255, empty)


def preProcessing(img):
    imgPre = cv2.GaussianBlur(img, (5, 5), 3)
    imgPre = cv2.Canny(imgPre, 0, 70)
    kernel = np.ones((3, 3), np.uint8)
    imgPre = cv2.dilate(imgPre, kernel, iterations=1)
    imgPre = cv2.morphologyEx(imgPre, cv2.MORPH_CLOSE, kernel)

    return imgPre


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    img = frame.array
    imgPre = preProcessing(img)
    imgContours, conFound = cvzone.findContours(img, imgPre, minArea=20)

    totalMoney = 0
    imgCount = np.zeros((480, 640, 3), np.uint8)

    if conFound:
        for count, contour in enumerate(conFound):
            peri = cv2.arcLength(contour['cnt'], True)
            approx = cv2.approxPolyDP(contour['cnt'], 0.02 * peri, True)

            if len(approx) > 8 :
                area = contour['area']
                x, y, w, h = contour['bbox']
                imgCrop = img[y:y + h, x:x + w]
                imgColor, mask = myColorFinder.update(imgCrop, hsvVals)
                whitePixelCount = cv2.countNonZero(mask)

                print(area)

                if 300 < area < 450:
                    totalMoney += 0.01  # penny
                elif 450 < area < 800:
                    totalMoney += 0.05  # nickel,
                elif 800 < area < 2000:
                    totalMoney += 0.10  # dime
                elif area > 2800:
                    totalMoney += 0.25  # quarter

    imgStacked = cvzone.stackImages([img, imgPre, imgContours, imgCount], 2, 1)
    cvzone.putTextRect(imgStacked, f'Dollar.{totalMoney}', (50, 50))

    cv2.imshow("Image", imgStacked)
    # cv2.imshow("imgColor", imgColor)

    rawCapture.truncate(0)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

camera.close()
cv2.destroyAllWindows()

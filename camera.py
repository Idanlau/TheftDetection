import cv2
import cvzone
import numpy as np
from cvzone.ColorModule import ColorFinder

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

totalMoney = 0

myColorFinder = ColorFinder(False)
# Custom Orange Color
hsvVals = {'hmin': 0, 'smin': 0, 'vmin': 145, 'hmax': 63, 'smax': 91, 'vmax': 255}


def empty(a):
    pass


def preProcessing(img):
    imgPre = cv2.GaussianBlur(img, (5, 5), 3)
    imgPre = cv2.Canny(imgPre, 0, 70)
    kernel = np.ones((3, 3), np.uint8)
    imgPre = cv2.dilate(imgPre, kernel, iterations=1)
    imgPre = cv2.morphologyEx(imgPre, cv2.MORPH_CLOSE, kernel)

    return imgPre

def count():
    while True:
        success, img = cap.read()
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
        cv2.waitKey(1)
        return totalMoney

import numpy as np
import cv2 as cv
import pyautogui, time

time.sleep(1)
image = pyautogui.screenshot()
image.save("screenshot.jpg")
img = cv.imread('screenshot.jpg')
output = img.copy()
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 5)
circles = cv.HoughCircles(gray,cv.HOUGH_GRADIENT,0.1,960,
                            param1=50,param2=30,minRadius=0,maxRadius=0)

detected_circles = np.uint16(np.around(circles))
for (x, y, r) in detected_circles[0, :]:
    cv.circle(output, (x, y), 1, (0, 255, 255), 3)
    time.sleep(1)
    print(pyautogui.position(x,y))
    pyautogui.moveTo(x,y,duration=1)







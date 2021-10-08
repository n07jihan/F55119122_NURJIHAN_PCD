import cv2
import numpy as np

img = cv2.imread("kupu-kupu.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Icon1 Original", img)
cv2.imshow("Icon1 Grayscale", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
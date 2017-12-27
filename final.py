import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('D:\img.JPG',0)
img = cv2.medianBlur(img,5)

'''..............................................................*1 mser*.......................................................'''
_,imgMSER = cv2.threshold(img,127,255, cv2.THRESH_BINARY)

cv2.imwrite('mser1.png', imgMSER)

'''..............................................................*2 edges*.......................................................'''
edges = cv2.Canny(img,200,200)
cv2.imwrite('edges2.png', edges)


''''..............................................................*3 fill*......................................................'''
im_in = cv2.imread("D:\edges.png", cv2.IMREAD_GRAYSCALE);
th, im_th = cv2.threshold(im_in, 220, 255, cv2.THRESH_BINARY_INV);

im_floodfill = im_th.copy()

h, w = im_th.shape[:2]
mask = np.zeros((h + 2, w + 2), np.uint8)

cv2.floodFill(im_floodfill, mask, (0, 0), 255);
cv2.imwrite('fill3.png', im_floodfill)
'''..............................................................*4  and 1 , 3*.......................................................'''
res4 = np.bitwise_and(im_floodfill, imgMSER)
cv2.imwrite('and4.png', res4)


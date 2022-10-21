# Programa que detecta los bordes en una imagen
# Program that detects the edges in an image
import cv2
from cv2 import line
import numpy as np

# Carga de imagen /Upload the image
img = cv2.imread('Original.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize = 3)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength = 50, maxLineGap = 10)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1 , y1), (x2 , y2), (0 , 255 , 0), 1, cv2.LINE_AA)

cv2.imshow('Bordes', edges)
cv2.imshow('Lineas sobre la imagen original', img)
cv2.waitKey()
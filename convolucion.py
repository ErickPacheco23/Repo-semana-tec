import numpy as np
import cv2
import sys
import cv2 as cv


ddepth = cv2.CV_16S
kernel_size = 3
window_name = "Laplace"

image = cv2.imread('cuad.jpg')
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
h = np.array([[0, -1, 0],
              [-1, 5, -1],
              [0, -1, 0]])

dst = cv2.Laplacian(img, ddepth, ksize=kernel_size)
forma = np.shape(img)
img2 = np.zeros(forma)
for x in list(range(1, forma[0] - 1)):
    for y in list(range(1, forma[1] - 1)):
        suma = 0
        for i in list(range(-1, 2)):
            for j in list(range(-1, 2)):
                suma = img[x - i, y - j] * h[i + 1, j + 1] + suma
        img2[x, y] = suma
#print(img2)
maxs = np.max(img2)
img2 = img2 * 255 / maxs
img2 = img2.astype(np.uint8)
absimg2 = cv.convertScaleAbs(img2)
abs_dst = cv.convertScaleAbs(dst)
cv2.imshow(window_name, abs_dst)
cv2.imshow("hola",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

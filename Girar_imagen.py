import cv2
import matplotlib.pyplot as plt
from skimage.transform import rotate
import numpy as np
from skimage.io import imread, imshow


image = imread('imagen.jpg')

image_rotated = rotate(image, angle=90, resize=True)
#imshow(image_rotated)

plt.subplot(121), imshow(image)
plt.title('Imagen')
plt.subplot(122), imshow(image_rotated)
plt.title('Imagen rotada')

plt.show()
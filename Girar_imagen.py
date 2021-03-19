import cv2
import matplotlib.pyplot as plt
from skimage.transform import rotate
import numpy as np
from skimage.io import imread, imshow


image = imread('imagen.jpg')

angulo = int(input("¿Cuántos grados quieres girar la imagen? "))
image_rotated = rotate(image, angle=angulo, resize=True)

plt.subplot(121), imshow(image)
plt.title('Imagen')
plt.subplot(122), imshow(image_rotated)
plt.title('Imagen rotada')

plt.show()
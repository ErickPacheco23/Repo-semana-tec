import cv2
import matplotlib.pyplot as plt
from skimage.transform import rotate
import numpy as np
from skimage.io import imread, imshow
from skimage import exposure
from numpy import fliplr, flipud
from skimage.color import rgb2hsv

image = imread('imagen.jpg')

opcion=0
while opcion != 4:
    print("""
            ╔═════════════════════════════╗
            ║             MENU            ║
            ║     1. Rotar imagen         ║
            ║     2. Cambiar brillo       ║
            ║     3. Reflejar imagen      ║
            ║     4. SALIR                ║
            ╚═════════════════════════════╝   """)
    opcion=int(input("¿Qué quieres hacer? "))
    if opcion == 1:
        angulo = int(input("¿Cuántos grados quieres girar la imagen? "))
        new_image = rotate(image, angle=angulo, resize=True)

        plt.subplot(121), imshow(image)
        plt.title('Original')
        plt.subplot(122), imshow(new_image)
        plt.title('Imagen rotada')
    elif opcion==2:
        brillo = float(input("¿Cuánto brillo? (0 a 1) "))
        new_image = exposure.adjust_gamma(image, gamma=0.6,gain=1)

        plt.subplot(121), imshow(image)
        plt.title('Original')

        plt.subplot(122),imshow(new_image)
        plt.title('Iluminada')
    elif opcion==3:
        new_image = fliplr(image)
        plt.subplot(121), imshow(image)
        plt.title('Original')
        plt.subplot(122), imshow(new_image)
        plt.title('Imagen reflejada')
    plt.show()
    image=new_image

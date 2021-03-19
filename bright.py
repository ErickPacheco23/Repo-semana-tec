from skimage.io import imread, imshow
import matplotlib.pyplot as plt
from skimage import exposure

image = imread('noche.jpg')
image_bright = exposure.adjust_gamma(image, gamma=0.4,gain=1)

plt.subplot(121), imshow(image)
plt.title('Original')

plt.subplot(122),imshow(image_bright)
plt.title('Iluminada')

plt.show()
from skimage.io import imread, imshow
from skimage.color import rgb2hsv
import matplotlib.pyplot as plt
from numpy import fliplr, flipud

img2 = imread('tsuru.jpg')
img2_new = fliplr(rgb2hsv(img2))

plt.subplot(121), imshow(img2)
plt.title('Tsuru RGB')
plt.subplot(122), imshow(img2_new)
plt.title('Tsuru HSV')

plt.show()
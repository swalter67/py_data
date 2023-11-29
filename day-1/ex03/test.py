import matplotlib.pyplot as plt
from PIL import Image

im = Image.open("animal.jpeg")

print(im.format, im.size, im.mode)
zoom = im.crop((400, 100, 800, 600))
zoom = zoom.convert("L")
plt.imshow(zoom)
plt.axis("on")
plt.show()

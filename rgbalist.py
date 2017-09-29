# List all RGBA values of an image with PIL
# https://stackoverflow.com/questions/31572425/list-all-rgba-values-of-an-image-with-pil
from PIL import Image
imgobj = Image.open('ghost_tiny.png')
pixels = imgobj.convert('RGBA')
data = imgobj.getdata()
for pixel in data:
    print pixel

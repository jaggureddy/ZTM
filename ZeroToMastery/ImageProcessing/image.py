from PIL import Image, ImageFilter
from pathlib import Path


img = Image.open(str(Path.cwd().parent)+'//pics//raul-varzar-xMoq7nGf1nk-unsplash.jpg')
img1 = Image.open(str(Path.cwd().parent)+'//pics//pic.jpg')

# filterimg = img.filter(ImageFilter.SMOOTH)
# filterimg.save('blur.png', 'png')

print(img1.size)
img1.thumbnail((400, 400))
img1.save('thumb.jpg')
filter_img = img.convert('L')
rotate = filter_img.rotate(180)
resize = filter_img.resize((1000, 1000))
# (left, upper, right, lower) = (200, 200, 1000, 1000)
# im_crop = filter_img.crop((left, upper, right, lower))
resize.save('pic1.png', 'png')
print(resize.size)
resize.show()
img.close()


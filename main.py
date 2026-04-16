from PIL import Image, ImageFilter


img = Image.new("RGB", (200, 200), color="blue")

blurred = img.filter(ImageFilter.BLUR)

img.show()
blurred.show()
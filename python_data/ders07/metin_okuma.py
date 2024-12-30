import pytesseract as pyt # pip install pytesseract
import PIL # pip install pillow

fotograf = PIL.Image.open("./yazi.png")
yazi = pyt.image_to_string(fotograf)

print(yazi)
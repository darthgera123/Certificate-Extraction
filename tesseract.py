import cv2
from PIL import Image
import pytesseract

config = ('-l eng --oem 1 --psm 3')
im = Image.open("Nagrjuna.jpeg")

text = pytesseract.image_to_string(im, lang = 'eng', config=config)

print(text)

#Nearly works for IIT Kanpur
# Only works in case of non cursive straightforward handwriting. In all Other cases its getting really messed up
# Idea is if the name exists in the set of words, ill take it


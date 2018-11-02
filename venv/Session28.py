import cv2
import pytesseract

# Image Processing : Text Extraction from Image

img = cv2.imread("image.png",cv2.IMREAD_COLOR)
print(type(img))

text = pytesseract.image_to_string(img,lang="eng")

print(text)
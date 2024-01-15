import cv2 as cv
from PIL import ImageFont,  ImageDraw , Image , ImageFilter
import numpy as np
from TextProcessing import putText

img = cv.imread("cac8316d2a0ca4bfb72d7d2c78d4c2e7.jpg")
img = cv.resize(img, (1080 , 1920))


text = "Only you can make it through"

img = putText(img , text, ImageFont.truetype("fonts/BungeeSpice-Regular.ttf" , 60) , alignV="bottom" , color=(255 , 0 , 0), glow=False , letterSpacing= 20)


cv.imshow("Display Image" , img)
cv.imwrite("saved.png" , img)

cv.waitKey(0)
cv.destroyAllWindows()
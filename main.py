import cv2 as cv
from PIL import ImageFont,  ImageDraw , Image
import numpy as np

img = cv.imread("img.png")

image = Image.fromarray(cv.cvtColor(img , cv.COLOR_BGR2RGB))

draw = ImageDraw.Draw(image)

# use a truetype font
font = ImageFont.truetype("arial.ttf", 30)

text = "Hello my name is mayuresh Umakant Satam I am here to seek help for this project I know that many of you are doing great"

# Calculate the position to center the text
image_width, image_height = image.size
text_width = font.getlength(text)
position = ((image_width - text_width) // 2, image_height // 1.7)


draw.text(position, text, font=font )

img = cv.cvtColor(np.array(image) , cv.COLOR_RGB2BGR)
cv.imshow("Display Image" , img)

cv.waitKey(0)
cv.destroyAllWindows()
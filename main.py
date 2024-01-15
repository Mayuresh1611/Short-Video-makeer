import cv2 as cv
from PIL import ImageFont,  ImageDraw , Image , ImageFilter
import numpy as np
from TextProcessing import putText

img = cv.imread("img.png")
img = cv.resize(img, (500 , 600))



# img = Image.fromarray(cv.cvtColor(img , cv.COLOR_BGR2RGBA))
# image = Image.new('RGBA' , img.size , (255 , 255 , 255 , 0))

# draw = ImageDraw.Draw(image)

# # use a truetype font
# fontSize  = 60
# font = ImageFont.truetype("arial.ttf", fontSize)

# text = "Some are born happy"


# # Calculate the position to center the text
# image_width, image_height = image.size

# def measureChars(image_width , fontSize) -> int:
#     noChars = 0
#     chars = "="
#     image_width -= 40
#     while font.getlength(chars) < image_width:
#         chars += "="
#         noChars += 1

#     return noChars

# def splitText (text , image_width , fontSize):
#     text_width = font.getlength(text)
#     line = 1
#     splittext = []
#     if text_width > image_width:
#         noChars = measureChars(image_width , fontSize)
#         n = int(len(text) // noChars)
#         print(n)
#         pos = 0        
#         for j in range(n):
#             i = pos + noChars

#             while i > 0:
#                 if text[i] == " ":
#                     splittext.append(text[pos:i])
#                     break
#                 i -= 1
#             pos = i
#         splittext.append(text[pos::])
#     else:
#         splittext.append(text)
#     return splittext

# text = splitText(text , image_width , fontSize)
# print(text)

# def draw_glowing_text(draw, text, position, font, text_color, glow_color, glow_radius):
#     for i in range(1, glow_radius + 1):
#         alpha = int(255 * (1 - i / (glow_radius + 1)))
#         offset = i
#         draw.text((position[0] - offset, position[1]), text, font=font, fill=(glow_color[0], glow_color[1], glow_color[2], alpha))
#         draw.text((position[0] + offset, position[1]), text, font=font, fill=(glow_color[0], glow_color[1], glow_color[2], alpha))
#         draw.text((position[0], position[1] - offset), text, font=font, fill=(glow_color[0], glow_color[1], glow_color[2], alpha))
#         draw.text((position[0], position[1] + offset), text, font=font, fill=(glow_color[0], glow_color[1], glow_color[2], alpha))

#     # Draw the main text on top
#     draw.text(position, text, font=font, fill=text_color)

# def putOnScreen(text , image_width , fontSize):
#     buff = 0
#     for i in range(len(text)):
#         text_width = font.getlength(text[i])
#         position = ((image_width - text_width) // 2, (image_height // 1.2) + buff)

#         draw_glowing_text( draw , text[i] , position , font , (255, 255,255) , (0 , 0, 0) , 6)
#         buff += fontSize + (fontSize // 2)

# putOnScreen(text , image_width , fontSize)
    
# combined = Image.alpha_composite(img, image)

# img = cv.cvtColor(np.array(combined) , cv.COLOR_RGB2BGR)

text = " Mayuresh Satam "
img = putText(img , text, ImageFont.truetype("arial.ttf" , 20) , alignV="top")

cv.imshow("Display Image" , img)
cv.imwrite("saved.png" , img)

cv.waitKey(0)
cv.destroyAllWindows()
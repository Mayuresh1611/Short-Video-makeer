import cv2 as cv
from PIL import ImageFont,  ImageDraw , Image , ImageFilter
import numpy as np

def putText( img , text:str , font:ImageFont , alignV="bottom"  , glow=False ):
    """ 
    img : Matlike cv image
    text: string
    font: ImageFont
    alignV: vertical alignment ( bottom, center , top)
    glow = Glow effect on the text, true or false
    return : matlike (cv format imgage)

    """
    # convert cv image to PIL image
    imgPIL = Image.fromarray(cv.cvtColor(img , cv.COLOR_BGR2RGBA))

    # read the dimesions of the image
    imgWid, imgHeight = imgPIL.size 
    draw = ImageDraw.Draw(imgPIL)
    
    # arrange the text according to screen size 
    splitText = text.split()  
    Lines = []
    line = " " 
    print(len(splitText))
    while len(splitText) > 0:
        word = splitText[0]
        potenLine = line  + word + " "
        if font.getlength(potenLine) < imgWid:
            line = potenLine
            splitText.pop(0) 
        else:
            Lines.append(line)
            line = ""
    if len(line) > 0:
        Lines.append(line)

    # For each text
    if alignV == "center":
        buff =  -(font.size * int(len(Lines) // 2) + ((font.size * int(len(Lines) // 2)) // 2))
    elif alignV == "top":
        buff = 0
    else:
        buff = -(font.size * len(Lines)  + ((font.size * int(len(Lines) // 2)) // 2))

    for line in Lines:
        textWid = font.getlength(line)

        horiP = (imgWid - textWid) // 2
        
        if alignV == "center":
            vertP = ( imgHeight // 2 ) + buff
        elif alignV == "top":
            vertP = ( imgHeight // 10.8) + buff
        else:
            vertP = ( imgHeight // 1.1) + buff
        buff += font.size + (font.size // 2)

        
        if vertP > imgHeight:
            raise ValueError("Text overflows the screen height")
    
        
            

        textPosition = (horiP , vertP)
        print(textPosition)
        draw.text(textPosition, line, font=font, fill=(0 , 0 , 0))


    imgCV = cv.cvtColor(np.array(imgPIL) , cv.COLOR_RGB2BGR)
    return imgCV
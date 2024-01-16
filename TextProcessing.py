import cv2 as cv
from PIL import ImageFont,  ImageDraw , Image , ImageFilter
import numpy as np

def putText( img , text:str , font:ImageFont , alignV="bottom"  , color = (255 , 255 , 255) ,  glow=False , letterSpacing = 0):
    """ 
    img : Matlike cv image
    text: string
    font: ImageFont
    alignV: vertical alignment ( bottom, center , top)
    glow = Glow effect on the text, true or false
    return : matlike (cv format imgage)

    """
    # convert cv image to PIL image
    background = Image.fromarray(cv.cvtColor(img , cv.COLOR_BGR2RGBA))
    imgPIL = Image.new("RGBA" , background.size , (0 , 0 , 0 , 0) )

    # read the dimesions of the image
    imgWid, imgHeight = imgPIL.size 
    draw = ImageDraw.Draw(imgPIL)
    

    # arrange the text according to screen size 
    splitText = text.split()  
    Lines = []
    line = " " 
    while len(splitText) > 0:
        word = splitText[0]
        potenLine = line  + word + " "
        wordlen = font.getlength(word) + len(potenLine) * letterSpacing
        if wordlen > imgWid:
            raise ValueError
        if (font.getlength(potenLine) + len(potenLine) * letterSpacing) < imgWid:
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
    
    rectY = [font.size , font.size * 2]

    for line in Lines:
        textWid = font.getlength(line) + len(line) * letterSpacing

        horiP = (imgWid - textWid) // 2
        
        if alignV == "center":
            vertP = ( imgHeight // 2 ) + buff
        elif alignV == "top":
            vertP = ( imgHeight // 10.8) + buff
        else:
            vertP = ( imgHeight // 1.2) + buff
        buff += font.size + (font.size // 2)

        if Lines.index(line) == 0:
            rectY[0] = vertP - rectY[0]
        if Lines.index(line) == len(Lines)-1:
            rectY[1] += vertP
        
        if vertP > imgHeight:
            raise ValueError("Text overflows the screen height")
    

        textPosition = (horiP , vertP)
        print(textPosition)
        if glow:
            #imgPIL = drawGlow(imgPIL , textPosition , text , font , 6 , (0 , 255 , 0) , letterSpacing )
            pass
        else:
            for char in line:
                draw.text(textPosition, char, color, font )
                width = draw.textlength(char, font) + letterSpacing
                textPosition = (textPosition[0]+width, textPosition[1])
    print(rectY)
    shape = [(0 , rectY[0]) , (imgWid , rectY[1])]
    draw = ImageDraw.Draw(background)

    draw.rectangle(shape, fill =(0, 0, 0, int(255 * 0.10))) 
    #imgPIL.crop((0 , rectY[0] ,imgWid , rectY[1]))
    background.paste(imgPIL, (0, 0), imgPIL )
    
    

    imgCV = cv.cvtColor(np.array(background) , cv.COLOR_RGB2BGR)
    return imgCV
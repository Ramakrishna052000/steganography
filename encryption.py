import math
from PIL import Image, ImageDraw,ImageFont
import numpy as np
file1 = open("crypt.txt","w")
text = textract.process('C:/Users/ramak/Downloads/1.txt')
txt=str(text)
txt=txt[2:len(txt)-1]
n=math.ceil(len(txt)/40)
fnt = ImageFont.truetype("C:/Users/ramak/PycharmProjects/pythonProject/venv/Lib/site-packages/tesseract/fonts/times.ttf", 100)
img = Image.new('RGB', (1920, 1080), color=(0, 0, 0))
d = ImageDraw.Draw(img)
for i in range(n):
    ll=i*40
    smalltxt=txt[ll:ll+40]
    d.text((10,(i*100)+10), smalltxt, font=fnt, fill=(255,255,255,255))
pixels = list(img.getdata())
width, height = img.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
a='i'
for row in pixels:
    c=(0,0,0)
    c1=0
    for i in row:
        if(i==c):
           c1+=1
        elif(i!=c):
            if(c==(0,0,0)):
                a+=' '
                c=(255,255,255)
                a+='a'+str(c1)
                c1=1
            elif(c==(255,255,255)):
                a+=' '
                c = (0, 0, 0)
                a+='b'+str(c1)
                c1=1
    if (c == (0, 0, 0)):
        a +=' '+'a' + str(c1)
    elif (c == (255, 255, 255)):
        a += " "+'b' + str(c1)
    a+="\n"
file1.write(a)
file1.close()
img.save("1.png")

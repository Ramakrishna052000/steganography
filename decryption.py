import textract
from PIL import Image, ImageDraw
import numpy as np
from pytesseract import *
file1 = open("crypt.txt","r")
file2 = open("message.txt","w", encoding="utf-8")
Lines = file1.readlines()
count = 0
oli=[]
for line in Lines:
    count+=1
    li = list(line.strip().split(" "))
    oli.append(li)
line=0
pi=0
bc=0
img = Image.new('RGB', (1920, 1080), color=(255, 255, 255))
for i in oli:
    line+=1
    pi=0
    for j in i:
        for k in j:
            if k=='a':
                num=int(j[1:])
                pi+=num
                break
            if k=='b':
                num=int(j[1:])
                for l in range(pi,pi+num):
                    img.putpixel((l,line),(0,0,0))
                pi+=num
                break
result = image_to_string(img)
a=str(result)
print(result)
file2.write(a)
file1.close()
file2.close()
img.save("2.png")
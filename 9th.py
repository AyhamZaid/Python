# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:15:08 2019

@author: Ayham
"""
import math
import random
import statistics as st

 
print("--------------EX1-------------")  
X = [3,1.5,4.5,6.75,2.25,5.75,2.25]
print(st.mean(X))
print(st.harmonic_mean(X))
print(st.median(X))
print(st.median_low(X))
print(st.median_high(X))
print(st.median_grouped(X))
print(st.mode(X))
print(st.pstdev(X))
print(st.pvariance(X))
print(st.stdev(X))
print(st.variance(X))
 
print("--------------EX2-------------")  

print( random.random() )
print ( random.randrange(10) )
print ( random.choice(['Ali', 'khalid', 'Hussam']) ) 
print ( random.sample(range(1000), 10) )
print ( random.choice('Orange Academy') )
items = [1,5,8,9,2,4]
random.shuffle(items)
print( items ) 
print ( random.randint(20, 30) )
print ( random.randrange(1000, 2111, 6) )
print ( random.uniform(10000, 11000))
print()

print("--------------EX3-------------")  
print (math.pi)
print(math.cos(200))
print(math.sin(200))
print(math.tan(200))
print(math.floor(10.8))
print(math.ceil(10.8))

print("--------------EX4-------------")  
from PIL import Image,ImageFilter,ImageDraw
im = Image.open("deadpool.jpeg")
print(im.format,im.size,im.mode)

im_flip =im.transpose(Image.FLIP_TOP_BOTTOM) 
greyscale_image = im.convert('L')
crop = im.crop((0,0,50,50))

img = Image.open("2.jpeg") 
draw = ImageDraw.Draw(img) 
draw.line((0,0) +img.size , fill=(255,255,255))
draw.line((0 , img.size[1] ,img.size[0],0) , fill=(255,255,255))
draw.text((img.size[0]/2 - img.size[0]/2,img.size[0]/2 + 220) , "AyhamZaid" ,fill=(255,255,0))
EDGE_ENHANCE = img.filter(ImageFilter.EDGE_ENHANCE)
FIND_EDGES = img.filter(ImageFilter.FIND_EDGES)
SMOOTH = img.filter(ImageFilter.SMOOTH)
SHARPEN = img.filter(ImageFilter.SHARPEN)
alpha = 0.5
img1 = Image.open("deadpool.jpeg") 
img2 = Image.open("2.jpeg").resize(img1.size) 
Image.blend(img1,img2,alpha).show()
blurred = im.filter(ImageFilter.BLUR)
img.rotate(90).save('new.png')

import numpy as np
data = np.tril(np.ones((256, 256)) * 255)
mask = Image.new("L", (256, 256))
mask.putdata(data.flatten().tolist())
mask.save("mask_tril_100.jpg")



size = (128,128)
saved = ("deadpool.jpeg")
img_thumbnail = Image.open("the.png")
img.thumbnail(size)
img.save(saved)
img.show()


#blurred.show()
# im.show()
# im_flip.show()
# greyscale_image.show()
# crop.show()
# img.show()
# FIND_EDGES.show()
# FIND_EDGES.show()
# SMOOTH.show()
# SHARPEN.show()
#img.rotate(90).save('new.png').show()




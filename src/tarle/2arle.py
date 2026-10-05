import cv2
import numpy as np
import io

p = str(input('Path'))
img = cv2.imread(p)

img_bw = np.where(img < 127, 0, 255)

print(img_bw)

for i in range(img_bw.__len__()):
    while i < img_bw.shape[0]:
        n = 0
        while img_bw.take == 0:
            n += 1
        Strx = Strx + "0" + str(n)

        n = 0
        while img_bw.any()[i] == 255:
            n += 1
        Strx = Strx + "1" + str(n)
        
    while i < img_bw.shape[1]:
        n = 0
        while img_bw[i] == 0:
            n += 1
        Stry = Stry + "0" + str(n)

        n = 0
        while img_bw[i] == 255:
            n += 1
        Stry = Stry + "1" + str(n)
        
    if Stry.__len__() < Strx.__len__():
        Str = Str + Stry + "0"
        
    else:
        Str = Str + Strx + "1"
        

    
#
#
# p1 row & column find most efficient rle string eg x = b256 y = b140w116. x is added + ref of axis & len, y is iterated.
# pseudocode:
# for len_of_array:
#    while i <= len_of_x:
#         n = 0
#         while pix_black:
#            n += 1
#         Strx = Strx + "0" + n

 #        n = 0
#         while pix_white:
#            n += 1
#        Strx = Strx + "1" + n

#    while i <= len_of_y:
#        while pix_black:
#            Stry = Stry + "0" + n
#            n += 1
#        while pix_white:
#            Stry = Stry + "1" + n
#            n += 1

#    if y.len < x.len:
#        Str = Str + Stry
#        ori = y
#    else:
#        Str = Str + Strx 

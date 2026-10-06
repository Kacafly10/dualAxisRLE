import cv2
import numpy as np


def encode_line(values):
    encoded = []
    n = 0
    while n < len(values):
        pixel = int(values[n])
        end = n + 1
        while end < len(values) and int(values[end]) == pixel:
            end += 1
        encoded.append(f"{pixel}{end - n}")
        n = end
    return "".join(encoded)


p = str(input('Path'))
img = cv2.imread(p, cv2.IMREAD_GRAYSCALE)
if img is None:
    raise ValueError(f"Could not read image: {p}")

img_bw = np.where(img < 127, 0, 255).astype(np.uint8)
Str = ""

for i in range(max(img_bw.shape)):
    Strx = encode_line(img_bw[i, :]) if i < img_bw.shape[0] else ""
    Stry = encode_line(img_bw[:, i]) if i < img_bw.shape[1] else ""

    if not Stry or (Strx and len(Strx) <= len(Stry)):
        Str += Strx + "x"
    else:
        Str += Stry + "y"

print(Str)
        

    
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

from PIL import Image
import io

p = input('Path')

with Image.open(p) as Src:
    b = io.BytesIO(Src)
    byteview = memoryview(b)
    
for byteview.__len__() in byteview:
    
    
#
#
#p1 row & column find most efficient rle string eg x = b256 y = b140w116. x is added + ref of axis & len, y is iterated.
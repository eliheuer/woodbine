# Render with: http://www.drawbot.com/
#
# Run "python3 docs/drawbot-sources/basic-specimen.py"
# from the root directory of the Woodbine repository.

from drawBot import *
import math
import os

# WHMF = (width, height, margin, frames )
W, H, M, F = 1024, 1024, 128, 32

font("fonts/Woodbine-VF.ttf")
for axis, data in listFontVariations().items():
    print((axis, data))

def grid(inc):
    stroke(0.3)
    stpX, stpY = 0, 0
    incX, incY = inc, inc
    for x in range(int(((W-(M*2))/inc)+1)):
        polygon((M+stpX, M), (M+stpX, H-M))
        stpX += incX
    for y in range(int(((H-(M*2))/inc)+1)):
        polygon((M, M+stpY), (H-M, M+stpY))
        stpY += incY


newPage(W, H)
fill(0)
rect(0, 0, W, H)

# Draw the grid (uncomment next line to show)
grid(32)

# Basic Style
stroke(None)
fill(1)
fontSize(80)
tracking(-1)
varWght = 200
lineH = 80
startP = 830
# Draw large text
for i in range(10):
    varWght += 100
    fontVariations(wght=varWght)
    print("varWght=", varWght) 
    fill(1, i*0.1, 0)
    if i <= 5:
        text("Woodbine Variable Font", (M+(161-(i*32)), (startP)-(i*lineH)))
    elif i == 6:
        text("ABCDEFGHIJKLMN", (M+15, (startP)-(i*lineH)))
    elif i == 7:
        text("OPQRSTUVWXY&Z", (M+50, (startP)-(i*lineH)))
    elif i == 8:
        text("abcdefghijklmnopqr", (M+80, (startP)-(i*lineH)))
    elif i == 9:
        text("stuvwxyz .,:;!?@#%$", (M+95, (startP)-(i*lineH)))


# Save GIF
#os.chdir("docs")
#os.chdir("images")
saveImage("~/Desktop/basic-specimen.gif")

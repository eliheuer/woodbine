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
    stroke(0.1)
    stpX, stpY = 0, 0
    incX, incY = inc, inc
    for x in range(int(((W-(M*2))/inc)+1)):
        polygon((M+stpX, M), (M+stpX, H-M))
        stpX += incX
    for y in range(int(((H-(M*2))/inc)+1)):
        polygon((M, M+stpY), (H-M, M+stpY))
        stpY += incY

# Draw basic page and grid
def draw_page():
    newPage(W, H)
    fill(0)
    rect(0, 0, W, H)
    # Draw the grid (uncomment next line to show)
    grid(32)

def set_style():
    stroke(None)
    fill(1)
    fontSize(128)
    tracking(-2)

# Draw specimen
draw_page()
set_style()

# Draw large type
varWght = 300
lineH = 96
startP = 802
for i in range(6):
    varWght += 100
    fontVariations(wght=varWght)
    print("varWght=", varWght) 
    text("Woodbine", (M+138, (startP)-(i*lineH)))

# Draw small type
fontVariations(wght=400)
tracking(4)
fontSize(24)
text("ABCDEFGHIJKLMNOPQRSTUVWXYZ", (M+140, (startP)-(i*lineH+(32*3))))
text("abcdefghijklmnopqrstuvwxyz", (M+200, (startP)-(i*lineH+(32*4))))
#text("0123456789!@#$%^&*", (M+200, (startP)-(i*lineH+(32*5))))

# Save GIF
os.chdir("docs")
os.chdir("images")
saveImage("basic-specimen.gif")
os.chdir("..")
os.chdir("..")

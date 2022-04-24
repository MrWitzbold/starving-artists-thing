import PIL
from PIL import Image
import requests
from io import BytesIO
from PIL import ImageFilter
from PIL import ImageEnhance
import numpy as np
import time

def get_color_list(color):
    color = str(color)
    color_code = color.replace(" ", "")
    color_code = color_code.replace("(", "")
    color_code = color_code.replace(")", "")
    color_code = color_code.split(",")
    color_list = [color_code[0], color_code[1], color_code[2]]
    return color_list

# anime ahegaos
# https://i.imgur.com/Hu6lJyz.png cute red girl orgasming
# https://i.imgur.com/SNjMKGA.png girl with mouth kept open
# https://i.imgur.com/WLGXdUh.png astolfo with fingers in mouth
# https://i.imgur.com/eenKXzo.png cute red girl with more extreme orgasm than the first one
# https://i.imgur.com/8U5bL66.png extreme
# https://i.imgur.com/RZ77eAs.png extreme
# https://i.imgur.com/gyNJdKG.png VERY EXPLICIT

# https://i.imgur.com/LpuOqM6.png real emo girl ahegao
# https://i.imgur.com/77ZMxAI.png coffee ahegao girl
# https://i.imgur.com/AK79vce.png extremely cute emo girl ahegao
# https://i.imgur.com/XWBY2oS.png real vampire teeth girl ahegao
# https://i.imgur.com/13F9rUf.png emo girl opening mouth with finger
# https://i.imgur.com/TkLNxdy.png emo girl with hand thing
# https://i.imgur.com/2Fk1E5w.png ahegao with glasses

URL = "https://i.imgur.com/eenKXzo.png"
response = requests.get(URL)
img = Image.open(BytesIO(response.content))

x_amount = img.width
y_amount = img.height
print(x_amount)
print(y_amount)

image_color_matrix = []
for y in range(0, img.height):
    for x in range(0, img.width):
        current_pixel = img.getpixel((x,y))
        current_color = get_color_list(current_pixel)
        image_color_matrix.append(current_color)

file = open("script.txt", "w")
code = ""
# 'x.Color = Color3.fromRGB(' + str(current_rgb[0]) + ', ' + str(current_rgb[1]) + ', ' + str(current_rgb[2]) + ')\n'
for i in range(1, 32*32+1):
    current_rgb = image_color_matrix[i-1]
    print(current_rgb)
    code += "game.Players.LocalPlayer.PlayerGui.MainGui.PaintFrame.GridHolder.Grid[\"" + str(i) + "\"].BackgroundColor3 = " + 'Color3.fromRGB(' + str(current_rgb[0]) + ', ' + str(current_rgb[1]) + ', ' + str(current_rgb[2]) + ')\n'
    code += "wait(0.001)\n"
    
file.write(code)
file.close()

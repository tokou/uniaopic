#!/usr/local/bin/python3
import numpy as np
from PIL import Image, ImageDraw

# open uniao Image
uniao = Image.open("uniao.png").convert("RGBA")
uniao_h, uniao_w = uniao.size

# Open the input image, convert to RGBA
img = Image.open("ed.jpg").convert("RGBA")

# resize input img to uniao size
img = img.resize((uniao_w, uniao_h), Image.ANTIALIAS)

# paste uniao
img.paste(uniao, (0, 0), uniao)

# Create same size alpha layer with circle
alpha = Image.new("L", img.size, 0)
draw = ImageDraw.Draw(alpha)
draw.pieslice([0, 0, uniao_h, uniao_w], 0, 360, fill=255)

# Convert alpha Image to numpy array
npAlpha = np.array(alpha)
npImage = np.array(img.convert("RGB"))

# Add alpha layer to RGB
npImage = np.dstack((npImage, npAlpha))

# Save with alpha
res = Image.fromarray(npImage)
res.save("result.png")

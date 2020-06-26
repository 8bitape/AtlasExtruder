import json

from PIL import Image

def extrude(image, sprites, padding):
	im = Image.open(image)
	pixels = im.load()
	atlas = json.load(open(sprites, "r"))

	for frame in atlas["frames"]:
		x = atlas["frames"][frame]["frame"]["x"]
		y = atlas["frames"][frame]["frame"]["y"]
		width = atlas["frames"][frame]["sourceSize"]["w"]
		height = atlas["frames"][frame]["sourceSize"]["h"]	

		for i in range(padding):
			for j in range (padding):
				pixels[x - (i + 1), y - (j + 1)] = pixels[x, y]
				pixels[x - (i + 1), y + (height + j)] = pixels[x, y + height - 1]
				pixels[x + (width + i), y - (j + 1)] = pixels[x + width - 1, y]
				pixels[x + (width + i), y + (height + j)] = pixels[x + width - 1, y + height - 1]	

		for y in range(y, y + height):
			for i in range(padding):
				pixels[x - (i + 1), y] = pixels[x, y]
				pixels[x + (width + i), y] = pixels[x + width - 1, y]

		for x in range(x, x + width):
			for i in range(padding):
				pixels[x, y + (i + 1)] = pixels[x, y]
				pixels[x, y - (height + i)] = pixels[x, y - height + 1]

		
			

	im.save(image)

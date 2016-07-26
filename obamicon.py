from PIL import Image
image = Image.open("kanye.jpg")
image.show()

pixels = list(image.getdata())

new_image_pixels = []

DARK_BLUE = (0, 51, 76)
YELLOW = (252, 257, 166)
LIGHT_BLUE = (112, 150, 158)
RED = (217, 26, 33)
PINK = (255, 52, 179)
PURPLE = (205, 0, 205)
BABY_BLUE = (132, 112, 125)

for i in pixels:
	intensity = i[0] + i[1] + i[2]
	if intensity < 182:
		new_image_pixels.append(DARK_BLUE)
	elif intensity >= 182 and intensity < 364: 
		new_image_pixels.append(RED)
	elif intensity >= 364 and intensity < 546:
		new_image_pixels.append(LIGHT_BLUE)
	elif intensity >= 546:
		new_image_pixels.append(YELLOW)	

new_image = Image.new("RGB", image.size)
new_image.putdata(new_image_pixels)
new_image.show()

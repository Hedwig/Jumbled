from PIL import ImageFont, ImageDraw, Image

image = Image.open('lenna.png')
draw = ImageDraw.Draw(image)
txt = "Hello World"
fontsize = 1  # starting font size

# portion of image width you want text width to be
img_fraction = 0.80

font = ImageFont.truetype("arial.ttf", fontsize)
while font.getsize(txt)[0] < img_fraction*image.size[0]:
    # iterate until the text size is just larger than the criteria
    fontsize += 1
    font = ImageFont.truetype("arial.ttf", fontsize)

# optionally de-increment to be sure it is less than criteria
fontsize -= 1
font = ImageFont.truetype("arial.ttf", fontsize)

print ('final font size' + str(fontsize))
draw.text((10, 25), txt, font=font) # put the text on the image
image.save('lenna_txt.png') # save it
from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.SMOOTH)
converted_img = img.convert('L')

# filtered_img.save("blur.png", 'png')

box = (100, 100, 400, 400)
region = converted_img.crop(box)
rotated_img = region.rotate(90)

resized_img = rotated_img.resize((300, 300))

resized_img.save('grey.png', 'png')
resized_img.show()

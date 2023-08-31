from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.SMOOTH)
converted_img = img.convert('L')

# filtered_img.save("blur.png", 'png')
converted_img.save('grey.png', 'png')
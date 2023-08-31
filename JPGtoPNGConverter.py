import sys
import os
from PIL import Image


image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

for image in os.listdir(image_folder):
    filename = os.path.splitext(image)[0]
    img = Image.open(f'./{image_folder}/{image}')
    img.save(f'./{output_folder}/{filename}.png', 'png')

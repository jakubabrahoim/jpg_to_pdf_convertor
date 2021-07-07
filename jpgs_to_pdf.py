import fnmatch
import os
from tqdm import tqdm
from PIL import Image

###
# 1. pip install Pillow
# 2. Enter path to the directory that contains the images to 'path' variable
# 3. The images have to be numbered (1, 2, 3 ... etc.)
# 4. Converted pdf will be saved to the same folder
###
 



path = r'C:\Users\jakub\Downloads' # r - raw string

number_of_files = len(fnmatch.filter(os.listdir(path), '*.jpg'))

image_list = []

print('Converting...')

image1 = Image.open(path + '\\1.jpg')

sequence_number = 2

for i in range(1, number_of_files):
    image_name = '\\' + str(sequence_number) + '.jpg'
    sequence_number += 1
    path_to_image = path + image_name

    image = Image.open(path_to_image)
    image_list.append(image)


image1.save(path + '\\converted_pdf.pdf', save_all = True, append_images = image_list)

print("Converting done...")

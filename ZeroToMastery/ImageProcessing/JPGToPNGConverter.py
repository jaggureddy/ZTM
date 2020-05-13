import sys
import os
from PIL import Image

#  grab first and second argument
path1 = 'C:\\Users\\JR0544\\PycharmProjects\\ZeroToMastery\\pics\\'
path2 = 'C:\\Users\\JR0544\\PycharmProjects\\ZeroToMastery\\pics1\\'

print(path1)
print(path2)

# check is new / exists, if not create
if not os.path.exists(path2):
    os.mkdir(path2)

# loop through folder
#
for file in os.listdir(path1):
    # filename = os.fsdecode(file)
    if file.endswith('.JPG') or file.endswith('.jpg') or file.endswith('.PNG') or file.endswith('.png'):
        img = Image.open(f'{path1}{file}')
        clean_name = os.path.splitext(file)
        # print(cleanname)
        if clean_name[1] == '.JPG' or clean_name[1] == '.jpg':
            img.save(f'{path2}{clean_name[0]}.png', 'png')
    # img.save(filename.split('.[jJpPgG]')[0]+'.png','png')
    # img.save(f'{path2}{file}', 'png')
# convert images to png
# save to new folder

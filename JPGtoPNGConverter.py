import sys
import os
from PIL import Image

source_folder = sys.argv[1]
target_folder = sys.argv[2]

if not os.path.exists(target_folder):
    os.makedirs(target_folder)

for filename in os.listdir(source_folder):
    img = Image.open(f"{source_folder}{filename}")
    clean_name = os.path.splitext(filename)[0]
    img.save(f"{target_folder}{clean_name}.png","png")
    



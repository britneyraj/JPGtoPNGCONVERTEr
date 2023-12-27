import sys
import os
from PIL import Image

image_folder = sys.argv[1]
output_folder = sys.argv[2]

# Ensure output_folder is an absolute path
output_folder = os.path.abspath(output_folder)

print(f"Image folder: {image_folder}")
print(f"Output folder: {output_folder}")

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img_path = os.path.join(image_folder, filename)
    print(f"Processing: {img_path}")
    img = Image.open(img_path)
    clean_name = os.path.splitext(filename)[0]
    output_path = os.path.join(output_folder, f'{clean_name}.png')
    img.save(output_path, 'png')
    print(f'Saved to: {output_path}')

print('All done')

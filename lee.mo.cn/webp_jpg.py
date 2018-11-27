# Python Imaging Library (PIL)
# http://www.pythonware.com/products/pil/
# https://pillow.readthedocs.io/en/latest/about.html#why-a-fork
# pip install pillow
from PIL import Image
files_path = [
    '001.webp',
    '002.webp',
    '003.webp',
]
for file_path in files_path:
    im = Image.open(file_path)
    if im.mode=="RGBA":
        im.load()  # required for png.split()
        background = Image.new("RGB", im.size, (255, 255, 255))
        background.paste(im, mask=im.split()[3])  # 3 is the alpha channel
        im = background
    im.save('{}.jpg'.format(file_path), 'JPEG')

from PIL import Image, ImageFilter

# img = Image.open('pikachu.jpg')
# filtered_img = img.filter(ImageFilter.GaussianBlur)
# filtered_img.save("blur.png", 'png')
# print(img)
# filtered_img = img.convert('L')
# filtered_img.save("grey.png", 'png')

img = Image.open('astro.jpg')
"""
new_img = img.resize((400, 400))
new_img.save('astro_thumbnail.jpg')
"""
# by resizing that way the image loses details as it gets squish up
img.thumbnail((400, 200))
img.save('astro_thumbnail.jpg')




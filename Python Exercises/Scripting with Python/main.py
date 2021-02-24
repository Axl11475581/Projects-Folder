from PIL import Image, ImageFilter

img = Image.open('pikachu.jpg')
filtered_img = img.filter(ImageFilter.GaussianBlur)
filtered_img.save("blur.png", 'png')
print(img)

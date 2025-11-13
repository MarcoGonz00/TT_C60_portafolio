from PIL import Image
im = Image.open('Imágenes\Secta kaiju.jpg')
print(im.size)
rotated = im.rotate(90)
rotated.save('rotated.png')
rotated.show()
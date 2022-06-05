from PIL import Image
im = Image.open('1200px-VGA_palette_with_black_borders.svg.png')
pixels = list(im.getdata())
width, height = im.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

for i in range(0,256):
    p = pixels[((i // 16)*(height//16) + (height//16 // 2))][i * (width//16) % (width) + (width//16 // 2)]
    print('vec3(' + str(p[0]/255) + ', '  + str(p[1]/255) + ', ' + str(p[2]/255) + '), ')


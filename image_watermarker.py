from PIL import Image, ImageDraw, ImageFont


def watermark_image(image_path, text):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    w, h = image.size
    x, y = int(w / 4), int(h / 4)
    if x > y:
        font_size = y
    else:
        font_size = x

    font = ImageFont.truetype("arial.ttf", int(font_size / 6))
    position = ((w/2 + x), (h/2 + y))
    text = "@Sahil" if text == "" else text
    draw.text(position, text=text, fill=(255, 255, 255, 180), font=font, anchor='rb')

    image.save('watermarkedImage.png')
    image.show()

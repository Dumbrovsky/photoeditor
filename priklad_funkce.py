from PIL import Image

def grayscale_filter(image):
    width, height = image.size
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            avg = int((r + g + b) / 3)
            image.putpixel((x, y), (avg, avg, avg))
    return image

def invert_filter(image):
    return image.convert('RGB').point(lambda p: 255 - p)

def red_blue_filter(image):
    width, height = image.size
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            image.putpixel((x, y), (r, b, r))
    return image

def apply_filter(image, choice):
    if choice == 1:
        return grayscale_filter(image)
    elif choice == 2:
        return invert_filter(image)
    elif choice == 3:
        return red_blue_filter(image)
    else:
        print("Invalid choice")
        return image

import PIL.Image

# ASCII characters used to build the output, from darkest to lightest
# You can swap this for a shorter list like "@%#*+=-:. " for higher contrast
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    width, height = image.size
    # We use 0.55 because terminal characters are usually twice as tall as they are wide
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters

def main(image_path, new_width=100):
    try:
        image = PIL.Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image: {e}")
        return

    # Process
    new_image_data = pixels_to_ascii(grayify(resize_image(image, new_width)))
    
    # Format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index + new_width)] for index in range(0, pixel_count, new_width)])
    
    print(ascii_image)

# Run it
main("image.jpg") # Change this to your filename
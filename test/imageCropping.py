import numpy as np
from PIL import Image, ImageDraw


def cropping(image):
    # Open the input image as numpy array, convert to RGB
    img = Image.open(image).convert("RGB")
    np_image = np.array(img)

    # Create same size alpha layer with circle
    alpha = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([200, 200, 800, 800], 0, 360, fill=255)

    # Convert alpha Image to numpy array
    np_alpha = np.array(alpha)

    # Add alpha layer to RGB
    np_image = np.dstack((np_image, np_alpha))

    # Save with alpha
    Image.fromarray(np_image).save('result.png')

    # Show the cropped image
    img2 = Image.open('result.png')
    img2.show()


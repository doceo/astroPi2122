# il seguente link spiega il codice
# https://projects.raspberrypi.org/en/projects/astropi-ndvi
import cv2
from PIL import Image
import numpy as np
# The fastie colour map takes dark pixels and makes them white. Then the brighter the original pixels, the further
# along the spectrum the colours are shifted. So dark grey pixels become blue, while bright white pixels become red.
from fastiecm import fastiecm

# from picamera import PiCamera
# import picamera.array
from pathlib import Path


# these lines to your code, to setup and use the Raspberry Pi camera. Comment out the line that loads the park.png
# image. original = cv2.imread('park.png') #Comment out this line, as no longer used


# le funzioni che seguono servono ad annulare i possibili errori di valutaizone
# di ndvi sull'immagine originale.


def loadImage(filename):
    print(f'try to load image {filename}')
    img = Image.open(filename).copy()
    print(f'{filename} loaded and copied\n')
    return img

def saveImage(filename, img):
    print(f'saving {filename}')
    img.save(filename)
    print(f'{filename} saved. bye\n\n')

def contrast_stretch(im):
    # find the top brightness of pixels in the image in the top 5% and bottom 5% of your image.
    in_min = np.percentile(im, 5)
    in_max = np.percentile(im, 95)
    # set the maximum brightness and minimum brightness on the new image you are going to create. The brightest a
    # pixel’s colour can be is 255, and the lowest is 0.
    out_min = 0.0
    out_max = 255.0
    """some calculations need to be performed to change all the pixels in the image, so that the image has the full 
    range of contrasts from 0 to 255. Add these lines to stretch out the pixel values and return the contrasted 
    image. """
    out = im - in_min
    out *= ((out_min - out_max) / (in_min - in_max))
    out += in_min
    return out


def calc_ndvi(image):
    # To adjust the pixels in the image and only work with red and blue, the image needs splitting into its three
    # seperate channels. r for red, g for green, and b for blue.
    b, g, r = cv2.split(image)
    """Now the red and blue channels need to be added together and stored as bottom. The blue channel can then have 
    the red channel subtracted (remember that red would mean unhealthy plants or no plants), and then divided by the 
    bottom calculation. Because we’re doing a division, we also need to make sure that none of our divisors are 0, 
    or there will be an error. """
    bottom = (r.astype(float) + b.astype(float))
    bottom[bottom == 0] = 0.01
    ndvi = (b.astype(float) - r) / bottom
    return ndvi


def contrast(image):
#    display(image, 'Original')
    # convert your image and display it on the screen.
    contrasted = contrast_stretch(image)
    #display(contrasted, 'Contrasted original')
    # save your high contrast image by adding a single line to the end of your code, so that you can compare the two
    # images in your file browser. It will be called contrasted.png.

    # pass in the contrasted image, display it, and save it.
    return contrasted


def contrastNdvi(contrasted):
    ndvi = calc_ndvi(contrasted)
    #display(ndvi, 'NDVI')
    ndvi_contrasted = contrast_stretch(ndvi)

    #display(ndvi_contrasted, 'NDVI contrasted')
    return ndvi_contrasted


"""
catch patches of brighter pixels. To once again enhance the image, it can be run through the contrast_stretch function.
Now you can see healthy plant life by the brightness of the pixels in the ndvi_contrasted.png image.
"""


def colorMapping(ndvi_contrasted):
    # Now the image can be converted using cv2 colour mapping, and written out as a new file
    color_mapped_prep = ndvi_contrasted.astype(np.uint8)
    # convert the image using the fastie colour map, display it, and write a new file.
    color_mapped_image = cv2.applyColorMap(color_mapped_prep, fastiecm)
    #display(color_mapped_image, 'Color mapped')

    return color_mapped_image

def ndviConversion(image):

    img = cv2.imread(image)
    contrasted = contrast_stretch(img)

    image_contrasted = image[:-4] + "-contrasted.jpg"   
    cv2.imwrite(image_contrasted, contrasted)
    print(image_contrasted)


    ndvi = calc_ndvi(contrasted)
    ndvi_contrasted = contrast_stretch(ndvi)
    
    image_contr_ndvi = image_contrasted[:-4] + "-ndvi.jpg"
    cv2.imwrite(image_contr_ndvi, ndvi_contrasted)
    print(image_contr_ndvi)

    color_mapped_prep = ndvi_contrasted.astype(np.uint8)
    color_mapped_image = cv2.applyColorMap(color_mapped_prep, fastiecm)

    image_color_map = image_contr_ndvi[:-4] + "-color_map.jpg"
    cv2.imwrite(image_color_map, color_mapped_image)

    print("fatto.\n\n")
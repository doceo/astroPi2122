# AstroPi2122

## *Abstract*

### *Objectives at the beginning of the project:*

The idea was to photograph an area with vegetation with the infrared camera. Then get the NDVI (Normalized Difference
Vegetation Index), of that area. Generated these photographs would have been compared with other previous infrared
images. By making this comparison it is possible to understand if over the years there has been a growth or a reduction
in the amount of vegetation present in that area, and then evaluate the environmental impact in that area.

### *Problem with machine learning:*

To obtain a calculation of the NDVI value as precise as possible, several perturbing factors had to be taken into
account, these are: atmospheric effects, soil effects, anisotropic effects, spectral effects, but above all cloud
effects. To solve the problem of clouds it was necessary to train the machine to recognize them. To prepare the machine
you had to give her images and through a machine learning code she had to be able to recognize clouds.

The problem was that the images provided were not suitable for comparison to train the machine. The photos were
incompatible with the intended use, because they were taken with a different raspberry and with different hardware. For
this reason the objectives of the project have varied and abandoned the idea of machine learning.

### *Final objectives of the project:*

The images taken previously were not even suitable for a comparison to compare the amount of vegetation. The final
objective of the project has varied towards two paths:

- *The first possible use of the data obtained would be to create a database of data and images that could benefit
  subsequent projects.*
- *The second possible use of the obtained data would be to compare them with data and images external to Astro Pi.*

## Built with:

- *[picamera 1.13](https://picamera.readthedocs.io/en/release-1.13/)*
- *[random](https://docs.python.org/3/library/random.html)*
- *[csv](https://docs.python.org/3/library/csv.html)*
- *[orbit](https://orbit-ml.readthedocs.io/en/latest/)*
- *[skyfield](https://rhodesmill.org/skyfield/)*
- *[time](https://docs.python.org/3/library/time.html)*
- *[datetime](https://docs.python.org/3/library/datetime.html#module-datetime)*
- *[pillow](https://pillow.readthedocs.io/en/stable/)*


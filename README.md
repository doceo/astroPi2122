# *AstroNet*
## *Abstract*
The aim of the project is to study the variation of biomass on planet Earth. To achieve this goal, it was assumed to photograph the planet with the infrared camera, identifying the areas with the presence of vegetation through NDVI (Normalized Difference Vegetation Index) processing. To obtain the state and the variation of biomass in a given period of time, a comparison with archive photographs was hypothesized.
Substantially, the software verifies that the space station flies over a sunlit area, taking photographs with a cadence compatible with the memory occupation established by Team AstroPi.

The project foresees the study of the collected photographs, comparing the ndvi value of the biomass areas not covered by clouds with the value of the archive photographs, in order to verify the differences and possible contractions of the areas covered by vegetation.

## *Criticality of the objectives*

In relation to the objectives set, a prerequisite for the comparison on NDVI values, as confirmed by the Astropi team, the archive photos provided by the experiences of previous years are not usable, because taken with different tools, unsuitable filters and the earth was mainly obscured by clouds. 
We will then proceed with the collection of the images which in a next phase will be discarded according to the biomass areas detected. Downstream of the selection, they will be properly compared with archive images of other sensors. In order to make this comparison, parametric corrections will be made for the calculation of the NDVI value, as suggested by the Department of Electrical Engineering and Information Technologies (DIETI) of the University of Naples Federico II, contacted to better understand the management and the evaluation of the NDVI value. Another benefit of the massive collection of images, without any selection before saving, is the availability to offer them for future scientific projects. In this way it will be possible to build up an archive of images taken with updated tools, so as to be able, possibly in a future project, to compare photographs with the same tool


### *Final objectives of the project*

The images taken previously were not even suitable for a comparison to compare the amount of vegetation. The final
objective of the project has varied towards two paths:

- *The first possible use of the data obtained would be to create a database of data and images that could benefit
  subsequent projects.*
- *The second possible use of the obtained data would be to compare them with data and images that will be provided by
  the University of Naples Federico II.*

## *Built with*

- *[picamera 1.13](https://picamera.readthedocs.io/en/release-1.13/)*
- *[random](https://docs.python.org/3/library/random.html)*
- *[csv](https://docs.python.org/3/library/csv.html)*
- *[orbit](https://orbit-ml.readthedocs.io/en/latest/)*
- *[skyfield](https://rhodesmill.org/skyfield/)*
- *[time](https://docs.python.org/3/library/time.html)*
- *[datetime](https://docs.python.org/3/library/datetime.html#module-datetime)*
- *[pillow](https://pillow.readthedocs.io/en/stable/)*


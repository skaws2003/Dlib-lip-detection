# Dlib-lip-detection
Developed by [Davis King](https://github.com/davisking), dlib is a cross-platform package for various image processing tasks.
For computer vision purpose, dlib has quite useful implementations, including:

* Facial landmark detection
* Correlation tracking
* Deep metric learning

from those, we'll use Facial landmark detection feature to detect and crop lip images from human face image.

# Installation
The easist way to get dlib and other needed libraries is using pip. open command prompt, and type:
~~~shell
$ pip install numpy
$ pip install cv2
$ pip install imutils
$ pip install cmake dlib
~~~

This will automatically install the required libraries for our project and its dependencies.

# Detecting Lips on given image
## Facial landmarks on dlib
The facial landmark detector for our project produces 68 (x, y)-coordinates that map to the specific facial structures. These are trained by the [iBUG-300W dataset](https://ibug.doc.ic.ac.uk/resources/facial-point-annotations/)

Below, we can see what the 68 facial landmarks are. 
![facial_landmarks](./captures/facial_landmarks.jpg)
from this image, we might see lip is corresponding to the landmark number [48,68].

## Detecting facial landmarks
Now look into our example code. We first import the libraries we need:
~~~python
import dlib
import cv2
import os
~~~
dlib package will be used for facial landmark detection, of course, and cv2 will be used for image processing. os package is for reading our image file list.

Since dlib produces its result in spacial format called 'Shape', we need to write a function to convert it into python list:
~~~python
def shape_to_list(shape):
	coords = []
	for i in range(0, 68):
		coords.append((shape.part(i).x, shape.part(i).y))
	return coords
~~~

# 10945805_LAB_WORKS

# Image Processing Tasks

This repository contains Python scripts for basic image processing operations using OpenCV and Matplotlib.

## Tasks

### Task 1: Image Loading and Grayscale Conversion
File: `task1/image_loading.py`  
Description:
- Loads an image file (`Input image.jpg`)
- Converts the image to grayscale
- Displays both original and grayscale images
- Saves the grayscale version as `photo_gray.jpg`
  

### Task 2: Color Space Conversion and Histogram
File: task2/color_conversion.py
Description:
- Loads a color image (photo.jpg)
- Converts to three color spaces:
  * Grayscale
  * HSV (Hue-Saturation-Value)
  * LAB (Lightness-A-B)
- Displays all converted images
- Saves each version with appropriate filenames:
  * photo_grayscale.jpg
  * photo_hsv.jpg
  * photo_lab.jpg
- Plots and displays the histogram of the grayscale image

  
### Task 3: Binary Thresholding Question
File: `task3/binary_thresholding.md` 
Description:
This task tests understanding of binary thresholding in image processing. Given:
A grayscale pixel value: 180
A threshold value: 150
Binary output convention:
0 (black) for pixels ≤ threshold
255 (white) for pixels > threshold

import cv2
import matplotlib.pyplot as plt

# Load image
image_path = 'Input image.jpg'  # Replace with your image file path
image = cv2.imread('image_path.jpg')

# Convert to different color spaces
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Display images
cv2.imshow('Grayscale', gray)
cv2.imshow('HSV', hsv)
cv2.imshow('LAB', lab)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save images
cv2.imwrite('photo_grayscale.jpg', gray)
cv2.imwrite('photo_hsv.jpg', hsv)
cv2.imwrite('photo_lab.jpg', lab)

# Plot histogram
plt.hist(gray.ravel(), 256, [0,256])
plt.title('Grayscale Histogram')
plt.show()

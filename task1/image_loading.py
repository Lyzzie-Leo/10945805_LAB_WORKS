import cv2

# Load image
image_path = 'Input image.jpg'  # Replace with your image file path
image = cv2.imread('image_path.jpg')

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display images
cv2.imshow('Original', image)
cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save grayscale image
cv2.imwrite('photo_gray.jpg', gray_image)

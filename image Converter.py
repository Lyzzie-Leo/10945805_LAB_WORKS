import cv2
import matplotlib.pyplot as plt
import os

# Step 1: Load a color image
image_path = 'Input image.jpg'  # Replace with your image file path
image = cv2.imread(image_path)

if image is None:
 raise FileNotFoundError(f"Image not found at {image_path}")

# Create output directory
output_dir = 'output_images'
os.makedirs(output_dir, exist_ok=True)

# Step 2: Convert to grayscale, HSV, and LAB
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)

# Step 3: Display and save each version
cv2.imshow('Original (BGR)', image)
cv2.imshow('Grayscale', gray)
cv2.imshow('HSV', hsv)
cv2.imshow('LAB', lab)

cv2.imwrite(os.path.join(output_dir, 'grayscale.jpg'), gray)
cv2.imwrite(os.path.join(output_dir, 'hsv.jpg'), hsv)
cv2.imwrite(os.path.join(output_dir, 'lab.jpg'), lab)

# Wait for key and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 4: Plot histogram of grayscale image
plt.figure(figsize=(8, 4))
plt.title('Histogram of Grayscale Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.hist(gray.ravel(), bins=256, range=[0, 256], color='black')
plt.grid(True)
plt.tight_layout()

# Save and show histogram
histogram_path = os.path.join(output_dir, 'grayscale_histogram.png')
plt.savefig(histogram_path)
plt.show()

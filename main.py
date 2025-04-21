import cv2

# Load image
image = cv2.imread('image.jpg')

# Check if image loaded
if image is None:
    print("Image not found.")
    exit()

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create a copy so we don't modify the original image
no_red = image.copy()
no_red[:, :, 2] = 0  # Remove red channel

# Flip the image vertical=0, horizontal=1, horizontal&vertical=-1
fliped_image = cv2.flip(no_red, 0)

#Image Crop
crop_image = image[0:400,0:600]

# Create windows (optional but useful for resizable display)
cv2.namedWindow('Orignal Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Grayscale Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Image Without Red', cv2.WINDOW_NORMAL)
cv2.namedWindow('Fliped Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Cropped Image', cv2.WINDOW_NORMAL)

# Show all images with unique names
cv2.imshow('Orignal Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('Image Without Red', no_red)
cv2.imshow('Fliped Image', fliped_image)
cv2.imshow('Cropped Image', crop_image)

# Saving Image
cv2.imwrite('Fliped_Image.jpg', fliped_image)

# Wait and close
cv2.waitKey(0)
cv2.destroyAllWindows()
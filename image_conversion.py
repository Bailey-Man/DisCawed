import cv2
import os

input_dir = "images/input"
output_dir = "images/output"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Get the list of image files in the input directory
image_files = os.listdir(input_dir)

for image_file in image_files:
    # Load the image
    image_path = os.path.join(input_dir, image_file)
    image = cv2.imread(image_path)

    # Convert to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Convert to redscale
    redscale_image = image.copy()
    redscale_image[:, :, 0] = 0
    redscale_image[:, :, 1] = 0

    # pixelate the redscale image
    pixelated_image = redscale_image.copy()
    pixelated_image = cv2.resize(pixelated_image, (16, 16), interpolation=cv2.INTER_NEAREST)


    # Save the grayscale image
    grayscale_output_path = os.path.join(output_dir, f"grayscale_{image_file}")
    cv2.imwrite(grayscale_output_path, grayscale_image)

    # Save the redscale image
    redscale_output_path = os.path.join(output_dir, f"redscale_{image_file}")
    cv2.imwrite(redscale_output_path, redscale_image)

    # Save the pixelated image
    pixelated_output_path = os.path.join(output_dir, f"pixelated_{image_file}")
    cv2.imwrite(pixelated_output_path, pixelated_image)

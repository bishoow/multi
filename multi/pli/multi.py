from PIL import Image

def compress_jpg(input_path, output_path, quality=20):
    """
    Compress a JPG image by reducing its quality.

    :param input_path: Path to the input image file.
    :param output_path: Path to save the compressed image.
    :param quality: Quality level for the compressed image (1 to 100).
    """
    # Open an image file
    with Image.open(input_path) as img:
        # Ensure the image is in RGB mode
        img = img.convert("RGB")
        # Save the image with reduced quality
        img.save(output_path, "JPEG", quality=quality)

# Example usage
input_image_path = 'image-snow.jpg'
output_image_path = 'compressed.jpg'

# Compress the image with quality level set to 20
compress_jpg(input_image_path, output_image_path, quality=20)
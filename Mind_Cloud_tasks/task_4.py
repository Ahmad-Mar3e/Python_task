"""
We will crop the left quarter of the image, create a new black square image,
and paste it over the cropped part.
"""
from PIL import Image

img = Image.open("C:\\Users\\Toward The Horizon\\Downloads\\free-nature-images.jpg")
width, height = img.size  # Get image size
left_quarter = img.crop((0, 0, width // 4, height))  # Crop the left quarter
black_box = Image.new("RGB", left_quarter.size, (0, 0, 0))  # Generate the black box
img.paste(black_box, (0, 0))
img.show()

from PIL import Image
import pytesseract

# Load the image
image_path = r"WhatsApp Image 2024-09-30 at 11.20.04_c0e696ce.jpg"
img = Image.open(image_path)

# Use pytesseract to extract text from the image
text = pytesseract.image_to_string(img)

# Display the extracted text
text

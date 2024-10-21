import json
import os
from CODE.inference import generate_response
from PIL import Image

def ask_questions(image, base_name):
    questions = [
        "What is the name of the product?",
        "What is the identification number of the product?",
        "What is the barcode of the product?",
        "What is the quantity size of the product?",
        "What is the weight of the product?",
        "What is the volume of the product?",
        "What is the expiration date of the product?",
        "What is the use before date of the product?",
        "What is the country of origin of the product?",
        "What is the manufacturing date of the product?",
        "What is the contact information for the product?",
        "What is the price of the product?",
        "What is the MRP of the product?",
        "Who is the manufacturer of the product?",
        "Is the product FSSAI certified?",
        "What is the nutritional information of the product?"
    ]

    product_info = generate_response(image, questions)

    output = {
    "image": base_name,
    "product_info": {
        "Product name": product_info.get("Name", ""),
        "Identification number": product_info.get("Identification Number", ""),
        "Barcode": product_info.get("Barcode", ""),
        "Quantity size": product_info.get("Quantity Size", ""),
        "Weight": product_info.get("Weight", ""),
        "Volume": product_info.get("Volume", ""),
        "Expiration date": product_info.get("Expiration Date", ""),
        "Use before date": product_info.get("Use Before Date", ""),
        "Country of origin": product_info.get("Country Of Origin", ""),
        "Manufacturing date": product_info.get("Manufacturing Date", ""),
        "Contact information": product_info.get("Contact Information", ""),
        "Price": product_info.get("Price", ""),
        "MRP": product_info.get("Mrp", ""),
        "Manufacturer": product_info.get("Manufacturer", ""),
        "FSSAI certified": product_info.get("Fssai Certified", ""),
        "Nutritional information": product_info.get("Nutritional Information", "")
        }
    }

    with open("product_info.json", "w") as json_file:
        json.dump(output, json_file, indent=2)

    print("Product information has been saved to product_info.json")





if __name__== "__main__":
    image_path = ""
    product_info = ask_questions(image_path)
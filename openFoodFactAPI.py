import requests
import os

def search_product(barcode):
    url = f"https://world.openfoodfacts.org/api/v2/product/{barcode}.json"
    
    response = requests.get(url)
    
    if response.status_code == 200:  # Valid response
        product_data = response.json()
        
        if product_data.get('status') == 1:  # Product found
            product_info = product_data['product']
            
            # Product details
            print(f"Product Name: {product_info.get('product_name', 'N/A')}")
            print(f"Brand: {product_info.get('brands', 'N/A')}")
            print(f"Nutrition Grade: {product_info.get('nutrition_grades', 'N/A')}")
            print(f"Ingredients: {product_info.get('ingredients_text', 'N/A')}")
            print(f"Categories: {product_info.get('categories', 'N/A')}")
            print(f"URL: {product_info.get('url', 'N/A')}")

            # Check for product price
            price = product_info.get('stores_tags', 'N/A')  # Check for price if available
            print(f"Price: {price}")
            
            # Download and save the product image
            image_url = product_info.get('image_url', None)
            if image_url:
                print(f"Image URL: {image_url}")
                download_image(image_url, barcode)
            else:
                print("No image available.")
        else:
            print("Product not found.")
    else:
        print(f"Failed to fetch product details. Status code: {response.status_code}")

def download_image(image_url, barcode):
    # Get the image response
    image_response = requests.get(image_url, stream=True)

    if image_response.status_code == 200:  # If the image request was successful
        image_name = f"{barcode}.jpg"  # Save the image with the product's barcode as the name
        
        # Save the image to the current directory
        with open(image_name, 'wb') as img_file:
            for chunk in image_response:
                img_file.write(chunk)
        print(f"Image downloaded and saved as {image_name}")
    else:
        print(f"Failed to download image. Status code: {image_response.status_code}")

if __name__ == "__main__":
    barcode = input("Enter the barcode of the product: ")
    search_product(barcode)

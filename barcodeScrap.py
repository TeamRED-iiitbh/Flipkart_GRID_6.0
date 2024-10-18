import requests
from bs4 import BeautifulSoup

# Function to extract product information based on barcode with headers
def extract_barcode_info(barcode):
    url = f'https://www.barcodelookup.com/{barcode}'  # Website URL with barcode
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting product name
        product_name = soup.find('h4', {'class': 'product-name'}).text.strip()

        # Extracting brand (if available)
        brand = soup.find('div', {'class': 'product-details'}).find('h5').text.strip()

        # Extracting other details (category, description, etc.)
        details = soup.find_all('div', {'class': 'product-attribute'})
        product_info = {}

        for detail in details:
            key = detail.find('span', {'class': 'label'}).text.strip()
            value = detail.find('span', {'class': 'value'}).text.strip()
            product_info[key] = value

        return {
            'Product Name': product_name,
            'Brand': brand,
            'Details': product_info
        }
    else:
        return f"Error: Couldn't retrieve data, status code {response.status_code}"

# Example barcode
barcode = '8901764032400'  # Replace with your barcode
product_info = extract_barcode_info(barcode)

# Print extracted product information
print(product_info)

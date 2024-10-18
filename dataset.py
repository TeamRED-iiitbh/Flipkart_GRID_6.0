from simple_image_download import simple_image_download as simp

def download_product_label_images(keywords, limit=100):
    response = simp.simple_image_download()
    
    for keyword in keywords:
        print(f"Downloading images for '{keyword}'...")
        response.download(keyword, limit)

    print("Download completed!")

def main():
    # List of keywords related to product labels
    keywords = [
        "product labels",
        "food product labels",
        "cosmetic product labels",
        "beverage labels",
        "bathroom itenary product labels",
    ]
    
    # Number of images to download per keyword
    images_per_keyword = 10
    
    download_product_label_images(keywords, images_per_keyword)

if __name__ == "__main__":
    main()
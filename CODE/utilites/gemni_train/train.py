import google.generativeai as genai
import os
import json
import PIL.Image
from api import api_keys
import re

# Step 1: Get the API key and configure generative AI
ak = api_keys()
api_key_1 = ak.get_private_vars()
os.environ['GOOGLE_API_KEY'] = api_key_1
genai.configure(api_key=api_key_1)

# Initialize the generative model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Step 2: Load the JSON file containing reference data
def load_reference_data(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to process an image and answer a question
def process_image_and_question(image_path, question, reference_data):
    img = PIL.Image.open(image_path)

    prompt = f"Based on similar product images, here's some reference information:\n"
    for entry in reference_data[:5]:  # Limit to 5 examples to keep the prompt shorter
        prompt += f"For an image like {entry['image']}, "
        prompt += f"the product info is: {json.dumps(entry['product_info'], indent=2)}\n\n"
    
    prompt += f"\nNow, for the current image at {image_path}, please answer this question: {question}"
    prompt += "\nPlease provide a detailed answer based on what you can see in the image and not search from the web to get the answer, just answer the question if you can see in the image and the reference information provided."
    prompt += "\nFormat your response as a JSON object with the same structure as the product_info in the reference data. Do not include any text outside of the JSON object."

    response = model.generate_content([prompt, img])
    return response.text

# Function to clean and parse JSON
def clean_and_parse_json(json_string):
    # Remove any text before the first '{' and after the last '}'
    json_string = re.search(r'\{.*\}', json_string, re.DOTALL)
    if json_string:
        json_string = json_string.group()
    else:
        raise ValueError("No JSON object found in the response")
    
    # Parse the JSON
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        print(f"Problematic JSON string: {json_string}")
        raise

# Function to save the updated data
def save_updated_data(json_file_path, updated_data):
    with open(json_file_path, 'w') as file:
        json.dump(updated_data, indent=2, fp=file)

# Main function
def main():
    json_file_path = 'label_updated.json'
    reference_data = load_reference_data(json_file_path)
    
    image_folder = 'test_images'
    user_question = "What would you like to know about the product in this image? Extract all the attributes of the image"
    
    for i in range(33, 122):  # From 010.png to 032.png
        image_filename = f"{i:03d}.png"
        user_image_path = os.path.join(image_folder, image_filename)
        
        if not os.path.exists(user_image_path):
            print(f"Image {image_filename} not found. Skipping.")
            continue
        
        print(f"Processing image: {image_filename}")
        
        try:
            answer = process_image_and_question(user_image_path, user_question, reference_data)
            print(f"\nGemini's response for {image_filename}:\n{answer}\n")
            
            # Clean and parse the JSON response
            parsed_answer = clean_and_parse_json(answer)
            
            # Create new entry
            new_entry = {
                "image": user_image_path,
                "product_info": parsed_answer
            }
            
            # Add the new entry to the reference data
            reference_data.append(new_entry)
            
            # Save the updated data after each image processing
            save_updated_data(json_file_path, reference_data)
            print(f"Updated data saved to {json_file_path} for image {image_filename}")
            
        except Exception as e:
            print(f"An error occurred while processing {image_filename}: {e}")
        
        print("-" * 50)

    print("All images processed.")

if __name__ == "__main__":
    main()
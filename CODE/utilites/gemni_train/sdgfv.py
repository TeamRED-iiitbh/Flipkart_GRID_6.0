import os
import json

def generate_label_studio_json(image_directory, output_file, question):
    # List to store all tasks
    tasks = []
    
    # Supported image extensions
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
    
    # Iterate through all files in the directory
    for filename in os.listdir(image_directory):
        if filename.lower().endswith(image_extensions):
            # Create a task for each image
            task = {
                "image": f"{filename}",
                "q1": question
            }
            tasks.append(task)
    
    # Write tasks to JSON file
    with open(output_file, 'w') as f:
        json.dump(tasks, f, indent=2)
    
    print(f"Generated JSON file with {len(tasks)} tasks.")

# Usage
image_directory = r"simple_images\product_labels"
output_file = "label_studio_tasks.json"
question = "What is the name of the product?"

generate_label_studio_json(image_directory, output_file, question)
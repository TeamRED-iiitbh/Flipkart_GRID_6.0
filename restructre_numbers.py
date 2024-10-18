import os
import shutil

def renumber_and_move_images(source_dir, dest_dir, start_num):
    # Create destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # Loop through files in source directory
    for filename in os.listdir(source_dir):
        if filename.endswith('.png'):
            # Extract the number from the filename
            file_num = int(filename.split('.')[0])
            
            # Calculate new number
            new_num = file_num + start_num - 1
            
            # Create new filename
            new_filename = f'{new_num:03d}.png'
            
            # Copy and rename file
            shutil.copy2(os.path.join(source_dir, filename), 
                         os.path.join(dest_dir, new_filename))
            
            print(f'Copied and renamed {filename} to {new_filename}')

# Usage
source_directory = 'naya_video'
destination_directory = 'test_images'
start_number = 33

renumber_and_move_images(source_directory, destination_directory, start_number)
import cv2
import numpy as np
import os

def sharpen_img(image):
    kernel = np.array([[0, -1, 0],
                       [-1, 5,-1],
                       [0, -1, 0]])
    image_sharp = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)
    return image_sharp

def process_video(video_path, output_path):
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Error: Could not open video {video_path}")
        return

    W, H = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    column_range = 7
    output_width = frame_count
    output_image = np.zeros((H, (column_range-1)*output_width, 3), dtype=np.uint8)

    i = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        middle_col_start = W // 2 - column_range // 2
        middle_col_end = W // 2 + column_range // 2
        middle_cols = frame[:, middle_col_start:middle_col_end]

        current_frame_end = (column_range-1)*(frame_count - i)
        current_frame_start = (column_range-1)*(frame_count - (i+1))

        if current_frame_start > 0:
            output_image[:, current_frame_start:current_frame_end] = middle_cols

        i += 1

    cap.release()

    output_image = sharpen_img(output_image)
    cv2.imwrite(output_path, output_image)
    print(f"Processed {video_path} and saved to {output_path}")

def main():
    input_folder = "new_data"
    output_folder = "test_images"

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each video in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4"):
            video_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + ".png"
            output_path = os.path.join(output_folder, output_filename)
            process_video(video_path, output_path)

if __name__ == "__main__":
    main()
from email.mime import base
from pdb import run
from CODE.image_stitching import unwrap_image
from CODE.product_info import ask_questions
from CODE.update_ui import run_ui
import os
from PIL import Image


img_dir = "./IMAGE"
video_dir = "./VIDEO"

if len(os.listdir(img_dir))==0:
    unwrap_image(os.path.join(video_dir, "013.mp4"))

img_path = os.path.join(img_dir, "output_image.png")
base_name = os.path.basename(img_path)
img = Image.open(img_path)


ask_questions(img, base_name)
run_ui()

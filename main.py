from email.mime import base
from pdb import run
from CODE.build.image_stitching import unwrap_image
from CODE.build.product_info import ask_questions
from CODE.update_ui import run_ui
import os
from PIL import Image


img_dir = "./IMAGE"
video_dir = "./VIDEO"

"Enter Video Name As: 013.mp4 to see the output"
video_name = "004.mp4" 
img_name = video_name.split(".")[0]+".png"


#Uncomment for testing image unwrapping, pass show = True to see the video
# if img_name not in os.listdir(img_dir):
#     show = False
#     unwrap_image(os.path.join(video_dir, video_name), os.path.join(img_dir, img_name), show)

img_path = os.path.join(img_dir, img_name)
base_name = os.path.basename(img_path)
img = Image.open(img_path)


ask_questions(img, base_name)
run_ui()

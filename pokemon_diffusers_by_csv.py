import torch
from diffusers import StableDiffusionPipeline
from torch import autocast
from PIL import Image, ImageFilter
import csv
device =  "mps" 

# pipe = StableDiffusionPipeline.from_pretrained("lambdalabs/sd-pokemon-diffusers", use_auth_token=True)  
# pipe = pipe.to(device)

scale = 10
n_samples = 1

image_size = (768,512) #横幅と高さ。2の倍数の値で入力。


disable_safety = False

def createImage(prompt:str,output_name:str):

    pipe = StableDiffusionPipeline.from_pretrained(
        "lambdalabs/sd-pokemon-diffusers",
        use_auth_token=True
    ).to(device)

    # init_image =  Image.open(file_path).convert("RGB").resize(image_size)
    images = pipe(prompt=prompt,  guidance_scale=7.5).images
    images[0].save("./images/" + output_name +'.jpg')

with open('pokemon_name_list.csv') as f:
    reader = csv.reader(f)

    for i,row in enumerate(reader):
        if i == 0:
            continue

        createImage(row[1],row[0])

        if i == 30:
            exit()



# createImage(prompt,prompt,3)

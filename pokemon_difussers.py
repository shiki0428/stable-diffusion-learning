import torch
from diffusers import StableDiffusionPipeline
from torch import autocast
from PIL import Image, ImageFilter

device =  "mps" 

pipe = StableDiffusionPipeline.from_pretrained("lambdalabs/sd-pokemon-diffusers", use_auth_token=True)  
pipe = pipe.to(device)

prompt = "Fish"
scale = 10
n_samples = 1

image_size = (768,512) #横幅と高さ。2の倍数の値で入力。

data_len = 100

# Sometimes the nsfw checker is confused by the Pokémon images, you can disable
# it at your own risk here
disable_safety = False

# if disable_safety:
#   def null_safety(images, **kwargs):
#       return images, False
#   pipe.safety_checker = null_safety

# with autocast('cpu'):
#   images = pipe(prompt=prompt, guidance_scale=scale).images

# for idx, im in enumerate(images):
#   im.save(f"{idx:06}.png")

def createImage(output_name:str,count:int):

    pipe = StableDiffusionPipeline.from_pretrained(
        "lambdalabs/sd-pokemon-diffusers",
        use_auth_token=True
    ).to(device)

    # init_image =  Image.open(file_path).convert("RGB").resize(image_size)
    images = pipe(prompt=prompt,  guidance_scale=7.5).images
    images[0].save(output_name + '_' +str(count).zfill(4) +'.jpg')

createImage("output",3)

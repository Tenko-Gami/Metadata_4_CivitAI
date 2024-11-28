from PIL import Image
from PIL.PngImagePlugin import PngInfo

import json

import get_functions as getF

metadata = PngInfo()

filename = 'albedo_emote2.png'
im = Image.open(filename)
print(im.info["prompt"])

for x, y in im.info.items():
    metadata.add_text(x, y)
    print(x, y)

data = json.loads(im.info["prompt"])

height, width = im.size
seed, steps, cfg, sampler_name, scheduler = getF.ksampler_values(data)
positive_prompt, negative_prompt = getF.prompts(data)


# print('width: ', width)
# print('height:', height)
# print(f"Seed: {seed}")
# print(f"Steps: {steps}")
# print(f"CFG: {cfg}")
# print(f"Sampler Name: {sampler_name}")
# print(f"Scheduler: {scheduler}")
#
#
# print("Positive prompt from KSampler:")
# print(positive_prompt)
#
# print("Negative prompt from KSampler:")
# print(negative_prompt)


root = r"C:\Users\mathi\Documents\Comfy_ui\ComfyUI_windows_portable\ComfyUI\models/"

lora_names = getF.lora_names(data)
ckpt_name = getF.model_name(data)

lora_hashes = ""
for lora_name in lora_names:
    hash = getF.hash(root + 'loras/' + lora_name)
    lora_hashes += f"{lora_name.split('.')[0]}: {hash}, "
    print(hash, lora_name)

Model_hash = getF.hash(root + 'checkpoints/' + ckpt_name)
print(Model_hash, ckpt_name.split(".")[0])

final_str= (f"{positive_prompt}\nNegative prompt: {negative_prompt}\nSteps: {steps}, Sampler: {sampler_name}, "
            f"Schedule type: {scheduler}, CFG scale: {cfg}, Seed: {seed}, Size: {width}x{height}, Model hash: {Model_hash},"
            f"Model: {ckpt_name.split(".")[0]}, Lora hashes: \"{lora_hashes}\", "
            f"Version: ComfyUi")

print(final_str)

metadata.add_text("parameters", final_str)

#im.save("test.png", pnginfo=metadata)
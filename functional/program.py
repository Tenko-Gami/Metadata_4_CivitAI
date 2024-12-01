from PIL import Image
import json
from PIL.PngImagePlugin import PngInfo

import functional.get_functions as get


def program(file_paths, model_folder):
    for file_path in file_paths:
        metadata = PngInfo()
        image = Image.open(file_path)
        data = json.loads(image.info["prompt"])
        for x, y in image.info.items():
            if x != "parameters":
                metadata.add_text(x, y)

        extracted_data = data_extraction(data=data, image=image, model_folder=model_folder)
        final_str = make_final_str(extracted_data=extracted_data)

        metadata.add_text("parameters", final_str)
        image.save('.'.join(file_path.split('.')[:-1]) + '_meta.png', pnginfo=metadata)


def data_extraction(data, image, model_folder):
    width, height = image.size
    seed, steps, cfg, sampler_name, scheduler = get.ksampler_values(data=data)
    positive_prompt, negative_prompt = get.prompts(data=data)
    ckpt_name, ckpt_hash, lora_hashes = hashes(model_folder=model_folder, data=data)

    extracted_data = {
        "cfg": cfg,
        "ckpt_hash": ckpt_hash,
        "ckpt_name": ckpt_name,
        "height": height,
        "lora_hashes": lora_hashes,
        "negative_prompt": negative_prompt,
        "positive_prompt": positive_prompt,
        "sampler_name": sampler_name,
        "scheduler": scheduler,
        "seed": seed,
        "steps": steps,
        "width": width,
    }

    return extracted_data


def hashes(model_folder, data):
    ckpt_name = get.model_name(data=data)
    ckpt_hash = get.hash(filename=model_folder + '/checkpoints/' + ckpt_name)

    loras = get.lora_names(data=data)
    lora_hashes = ""
    for lora_name in loras:
        lora_hash = get.hash(filename=model_folder + '/loras/' + lora_name)
        lora_hashes += f"{lora_name.split('.')[0]}: {lora_hash}, "

    return ckpt_name.split('.')[0], ckpt_hash, lora_hashes


def make_final_str(extracted_data):
    x = extracted_data
    final_str = (f"{x["positive_prompt"]}\n"
                 f"Negative prompt: {x["negative_prompt"]}\n"
                 f"Steps: {x["steps"]}, "
                 f"Sampler: {x["sampler_name"]}, "
                 f"Schedule type: {x["scheduler"]}, "
                 f"CFG scale: {x["cfg"]}, "
                 f"Seed: {x["seed"]}, "
                 f"Size: {x["width"]}x{x["height"]}, "
                 f"Model hash: {x["ckpt_hash"]},"
                 f"Model: {x["ckpt_name"]}, "
                 f"Lora hashes: \"{x["lora_hashes"]}\", "
                 f"Version: ComfyUi")

    return final_str

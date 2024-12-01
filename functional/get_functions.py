def ksampler_values(data):
    seed = None
    steps = None
    cfg = None
    sampler_name = None
    scheduler = None

    for key, value in data.items():
        if value.get("class_type") == "KSampler":
            inputs = value["inputs"]
            seed = inputs.get("seed")
            steps = inputs.get("steps")
            cfg = inputs.get("cfg")
            sampler_name = inputs.get("sampler_name")
            scheduler = inputs.get("scheduler")
            break

    return seed, steps, cfg, sampler_name, scheduler


def prompts(data):
    positive_prompt = []
    negative_prompt = []

    for key, value in data.items():
        if value.get("class_type") == "KSampler":
            inputs = value["inputs"]
            if "positive" in inputs:
                positive_key = inputs["positive"][0]
                if positive_key in data and "inputs" in data[positive_key] and "text" in data[positive_key]["inputs"]:
                    positive_prompt.append(data[positive_key]["inputs"]["text"])
            if "negative" in inputs:
                negative_key = inputs["negative"][0]
                if negative_key in data and "inputs" in data[negative_key] and "text" in data[negative_key]["inputs"]:
                    negative_prompt.append(data[negative_key]["inputs"]["text"])

    return positive_prompt[0], negative_prompt[0]


def lora_names(data):
    loras = []

    for key, value in data.items():
        if value.get("class_type") == "LoraLoader":
            inputs = value["inputs"]
            lora_name = inputs.get("lora_name")
            if lora_name:
                loras.append(lora_name)

    return loras


def model_name(data):
    model = None

    for key, value in data.items():
        if value.get("class_type") == "CheckpointLoaderSimple":
            inputs = value["inputs"]
            model = inputs.get("ckpt_name")
            break

    return model


def hash(filename):
    with open(filename, "rb") as file:
        import hashlib as hashlib
        m = hashlib.sha256()
        file.seek(0x100000)
        m.update(file.read(0x10000))
        thehash = m.hexdigest()[0:8]
        return thehash

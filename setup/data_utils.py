def read_jsonl(path):
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                ex = json.loads(line)
                yield ex


def write_jsonl(path, data):
    with open(path, "w") as f:
        for ex in data:
            f.write(json.dumps(ex) + "\n")


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def encode_image_url(image_path):
    if image_path.endswith(".png"):
        image_type = "png"
    elif image_path.endswith(".jpg"):
        image_type = "jpeg"
    else:
        raise ValueError(f"Image type not supported: {image_path}")

    base64_image = encode_image(image_path)
    return f"data:image/{image_type};base64,{base64_image}"

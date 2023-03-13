import os
import subprocess
from fastapi import FastAPI


detect_filename = "model/yolov7/detect.py"
bestpt_filename = "model/yolov7/best_13.pt"

app = FastAPI()

def change_extension_to_txt(file_name):
    """
    First, split the file name into base name and extension. Then adds txt extension.
    """
    base_name, extension = os.path.splitext(file_name.split('/')[-1])
    new_file_name = base_name + '.txt'
    return new_file_name

def change_extension_to_jpg(file_name):
    """
    First, split the file name into base name and extension. Then adds txt extension.
    """
    base_name, extension = os.path.splitext(file_name.split('/')[-1])
    new_file_name = base_name + '.jpg'
    return new_file_name


# http://127.0.0.1:8000/predict?image_filename=/.../applepotato.jpg
# adjust threshold if needed!!!
@app.get("/predict")
def predict(image_filename: str):
    shell_command = [
        "python",
        detect_filename,
        "--weights",
        bestpt_filename,
        "--conf",
        "0.2",
        "--source",
        image_filename,
        "--save-txt",
        "--save-conf",
        "--exist-ok",
        "--no-trace",
    ]
    process = subprocess.run(shell_command, capture_output=True)
    process.check_returncode()

    #define txt and jpg file name
    txt_filename = change_extension_to_txt(image_filename)
    jpg_filename = change_extension_to_jpg(image_filename)

    # Check if txt file exists
    if not os.path.exists(f"runs/detect/exp/labels/{txt_filename}"):
        return {"no txt file": "prob nothing detected"}

    # Get class and confidence out of txt
    ingredients_conf_dict = {}
    with open(f"runs/detect/exp/labels/{txt_filename}") as f:
        for line in f:
            key, *values, value = line.split()
            ingredients_conf_dict[key] = value

    #delete generated files
    subprocess.run(['rm', f"runs/detect/exp/labels/{txt_filename}"])
    #subprocess.run(['rm', f"runs/detect/exp/{jpg_filename}"])

    #return dict where key is class, values is confidence
    return ingredients_conf_dict

@app.get("/")
def root():
    return {
    'greeting': 'Hello World!'
}

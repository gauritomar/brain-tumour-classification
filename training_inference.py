from yolov8 import YoloV8Detection
import torch
from ultralytics import YOLO
from PIL import Image, ImageDraw
from tqdm import tqdm
import os
import json

def return_path(tumour_type, mri_type=None):
    if mri_type is None:
        return os.path.join('dataset', tumour_type)
    return os.path.join('dataset', f"{tumour_type}/{mri_type}")

detector = YoloV8Detection()

dataset_path = 'dataset'
tumour_types = ['Schwannoma', '_NORMAL', 'Glioblastoma', 'Papiloma', 'Germinoma', 'Ganglioglioma', 'Granuloma', 'Meningioma', 'Carcinoma', 'Neurocitoma', 'Ependimoma', 'Astrocitoma', 'Meduloblastoma', 'Oligodendroglioma', 'Tuberculoma']

for tumour_type in tqdm(tumour_types, desc="Tumour Types"):
    tumour_path = return_path(tumour_type)  
    mri_types = os.listdir(tumour_path)
    if '.DS_Store' in mri_types:
        mri_types.remove('.DS_Store')

    for mri_type in tqdm(mri_types, desc="MRI Types"):
        mri_path = return_path(tumour_type, mri_type)  
        images = os.listdir(mri_path)
        if '.DS_Store' in images:
            images.remove('.DS_Store')

        for image in tqdm(images, desc="Processing Images"):
            image_path = os.path.join(mri_path, image)
            output_folder_path = os.path.join('output', tumour_type, mri_type)
            os.makedirs(output_folder_path, exist_ok=True) 
            output_image_path = os.path.join(output_folder_path, image)
            image, detection_results = detector.run(image_path)

            with open('bbox.txt', "a") as f:
                f.write(f"{image_path}\t{json.dumps(detection_results)}\n")


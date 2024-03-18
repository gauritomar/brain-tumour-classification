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

class YoloV8Detection:
    def __init__(self):
        self.weights_path = 'best.pt'
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = YOLO(self.weights_path).to(self.device)

    def detect(self, image):
        results = self.model(image)
        detections = []

        for result in results:
            boxes = result.boxes.xyxy
            class_ids = result.boxes.cls
            confidence_score = result.boxes.conf
            classes = result.names

            for i in range(len(boxes)):
                detection = {
                    'class': classes[int(class_ids[i])],
                    'confidence': float(confidence_score[i]),
                    'box_points': [float(boxes[i][0]), float(boxes[i][1]), float(boxes[i][2]), float(boxes[i][3])]
                }

                detections.append(detection)

        return detections

    def run(self, image_path):
        image = Image.open(image_path)
        detections = self.detect(image)
        return image, detections

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


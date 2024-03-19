import torch
from ultralytics import YOLO
from PIL import Image, ImageDraw
from tqdm import tqdm
import os
import json


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
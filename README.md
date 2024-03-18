# Repository Contents

This repository contains the following files:

1. [brain-tumour-1.html](brain-tumour-1.html): This HTML file contains the output and code from the first training session for the brain tumor classification model. Due to limitations with Colab, the training had to be split into multiple sessions. This one trained resnet18 and resnet 182.

2. [brain-tumour-2.html](brain-tumour-2.html): Similar to [brain-tumour-1.html](brain-tumour-1.html), this HTML file contains the output and code from the second training session for the brain tumor classification model. This one trained  densenet121 and densenet161.

3. [compare.py](compare.py): This Python script is used compare the dataset provided with the dataset from kaggle to figure out the pixel matches.

4. [compare_images.py](compare_images.py): This python script is used to create a test dataset which is basically the files that were not present in the given dataset I assume are the test files.

5. [compare.py](compare.py): Just a simple file to check if the sum of test + given = orginal dataset to make sure I wasn't missing any of the files.

6. [og_dataset_format.py](og_dataset_format.py): Python script to convert the dataset downlaoded from kaggle to the format of the given dataset.

7. [yolov8.py](yolov8.py): This is for inferencing the given dataset on a tumour detection model. I trained the yolov8 on [Brain Tumour Detection Dataset - Roboflow](https://universe.roboflow.com/aabbcceeffgg/brain-tumor-detection-69d9s/dataset/2#) but couldn't get the ultralytics library to run in colab so did the inferencing here and save it to bbox.txt.

8. [flatten.py](flatten.py): This script is to flatten and normalise the detections for each image. A single image can have multiple tumours so I flattened the dataset over detections.
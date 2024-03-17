import os
import cv2
import shutil

og_dataset = "og_dataset2"
dataset = "dataset"
test = "test"

def return_path(folder, tumour_type, mri_type):
    return os.path.join(folder, tumour_type, mri_type)

if os.path.exists(og_dataset):
    og_folders = [f for f in os.listdir(og_dataset)]

if os.path.exists(dataset):
    dataset_folders = [f for f in os.listdir(dataset)]

if os.path.exists(test):
    test_folders = [f for f in os.listdir(dataset)]

for tumour_type in og_folders:
    mri_types = os.listdir(os.path.join(og_dataset, tumour_type))
    for mri_type in mri_types:
        og_images = len(os.listdir(return_path(og_dataset, tumour_type, mri_type)))
        dataset_images = len(os.listdir(return_path(dataset, tumour_type, mri_type)))
        test_images = len(os.listdir(return_path(test, tumour_type, mri_type)))

        if og_images != test_images + dataset_images:
            print(f"The number of images in the original dataset for {tumour_type}/{mri_type} is not equal to the sum of images in the test and dataset folders.")
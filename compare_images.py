import os
import cv2

og_dataset = "og_dataset"
dataset = "dataset"

if os.path.exists(og_dataset):
    og_folders = [f for f in os.listdir(og_dataset)]

if os.path.exists(dataset):
    dataset_folders = [f for f in os.listdir(dataset)]

def return_path(folder_type, tumour_type, mri_type, image_name):
    return os.path.join(folder_type, tumour_type, mri_type, image_name)


def find_closest_image(og_images_path, dataset_images_path):
    for dataset_image_path in dataset_images_path:
        dataset_image_gray = cv2.imread(dataset_image_path, cv2.IMREAD_GRAYSCALE)

        min_difference = float('inf')
        closest_image = None

        for og_image_path in og_images_path:
            og_image_gray = cv2.imread(og_image_path, cv2.IMREAD_GRAYSCALE)
            if dataset_image_gray.shape != og_image_gray.shape:
                continue
            difference = cv2.absdiff(dataset_image_gray, og_image_gray)
            total_difference = difference.sum()

            if total_difference < min_difference:
                min_difference = total_difference
                closest_image = og_image_path

        print(f"Closest image to '{dataset_image_path}' is '{closest_image}' with difference {min_difference}")

for tumour_type in og_folders:
    mri_types = [m for m in os.listdir(os.path.join(og_dataset, tumour_type))]
    for mri_type in mri_types:
        og_images = os.listdir(os.path.join(og_dataset, tumour_type, mri_type))
        dataset_images = os.listdir(os.path.join(dataset, tumour_type, mri_type))

        og_images_path = [return_path(og_dataset, tumour_type, mri_type, image) for image in og_images]
        dataset_images_path = [return_path(dataset, tumour_type, mri_type, image) for image in dataset_images]    
            
        find_closest_image(og_images_path, dataset_images_path)    
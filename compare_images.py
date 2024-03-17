import os
import cv2
import shutil

og_dataset = "og_dataset"
dataset = "dataset"

if os.path.exists(og_dataset):
    og_folders = [f for f in os.listdir(og_dataset)]

if os.path.exists(dataset):
    dataset_folders = [f for f in os.listdir(dataset)]

def return_path(folder_type, tumour_type, mri_type, image_name):
    return os.path.join(folder_type, tumour_type, mri_type, image_name)

def return_test_path(tumour_type, mri_type, image_name):
    return os.path.join("test", tumour_type, mri_type, image_name)

def find_closest_match(dataset_image_path, unmatched_og_images):
    dataset_image_gray = cv2.imread(dataset_image_path, cv2.IMREAD_GRAYSCALE)

    min_difference = float('inf')
    closest_image = None

    for og_image_path in unmatched_og_images:
        og_image_gray = cv2.imread(og_image_path, cv2.IMREAD_GRAYSCALE)
        if dataset_image_gray.shape != og_image_gray.shape:
            continue
        difference = cv2.absdiff(dataset_image_gray, og_image_gray)
        total_difference = difference.sum()

        if total_difference < min_difference:
            min_difference = total_difference
            closest_image = og_image_path

    return closest_image, min_difference

def copy_and_move_unmatched_images(unmatched_og_images):
    for unmatched_og_image in unmatched_og_images:
        destination_path = return_test_path(*unmatched_og_image.split(os.path.sep)[-3:])
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        shutil.copy(unmatched_og_image, destination_path)  # Copy image to the test directory
        print(f"Copied and moved unmatched image '{unmatched_og_image}' to '{destination_path}'")

def find_and_move_unmatched_images(og_images_path, dataset_images_path):
    unmatched_og_images = set(og_images_path)

    for dataset_image_path in dataset_images_path:
        closest_image, min_difference = find_closest_match(dataset_image_path, unmatched_og_images)

        if closest_image is None:
            print(f"No match found for '{dataset_image_path}'")
        else:
            unmatched_og_images.remove(closest_image)

    copy_and_move_unmatched_images(unmatched_og_images)

for tumour_type in og_folders:
    mri_types = [m for m in os.listdir(os.path.join(og_dataset, tumour_type))]
    for mri_type in mri_types:
        og_images = os.listdir(os.path.join(og_dataset, tumour_type, mri_type))
        dataset_images = os.listdir(os.path.join(dataset, tumour_type, mri_type))

        og_images_path = [return_path(og_dataset, tumour_type, mri_type, image) for image in og_images]
        dataset_images_path = [return_path(dataset, tumour_type, mri_type, image) for image in dataset_images]    
            
        find_and_move_unmatched_images(og_images_path, dataset_images_path)
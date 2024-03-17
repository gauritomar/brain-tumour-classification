import os

og_dataset = "og_dataset"
dataset = "dataset"

if os.path.exists(og_dataset):
    og_folders = [f for f in os.listdir(og_dataset)]

if os.path.exists(dataset):
    dataset_folders = [f for f in os.listdir(dataset)]

for tumour_type in og_folders:
    mri_types = [m for m in os.listdir(os.path.join(og_dataset, tumour_type))]
    for mri_type in mri_types:
        og_images_count = len(os.listdir(os.path.join(og_dataset, tumour_type, mri_type)))
        dataset_images_count = len(os.listdir(os.path.join(dataset, tumour_type, mri_type)))
        print(f"og_images_count: {og_images_count}, dataset_images_count: {dataset_images_count}")
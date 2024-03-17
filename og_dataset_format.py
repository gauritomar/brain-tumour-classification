# Script to make the downloaded dataset from kaggle the same format as the
# dataset provided so

import os

og_dataset = "og_dataset"

if os.path.exists(og_dataset):
    folders = [f for f in os.listdir(og_dataset)]
    
    for folder in folders:
        tumour_type, mri_type = folder.split(' ')
        
        new_folder_name = mri_type
        new_folder_path = os.path.join(og_dataset, tumour_type)
        new_folder_destination = os.path.join(new_folder_path, new_folder_name)

        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
    
        os.rename(os.path.join(og_dataset, folder), new_folder_destination)
        


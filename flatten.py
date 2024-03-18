import json

bbox_file_path = 'bbox.txt'

with open(bbox_file_path, 'r') as bbox_file, open('temp_bbox.txt', 'w') as temp_bbox_file:
    for line in bbox_file:
        image_path, detection_results_str = line.strip().split('\t')
        detection_results = json.loads(detection_results_str)
        
        if len(detection_results) > 1:
            for detection_result in detection_results:
                temp_bbox_file.write(f"{image_path}\t{json.dumps([detection_result])}\n")
        else:
            temp_bbox_file.write(line)

import shutil
shutil.move('temp_bbox.txt', bbox_file_path)

print("Processed the bbox.txt file.")

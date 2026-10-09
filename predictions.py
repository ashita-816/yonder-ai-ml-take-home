import argparse
from ultralytics import YOLO
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()
input_folder = args.input
output_folder = args.output
 
model = YOLO("runs/detect/test_run_final/weights/best.pt")
predictions = model.predict(source = input_folder, project = output_folder, save = True, save_txt = True, save_conf= True)

for prediction in predictions:
    # if the model detects 0 objects (0 boxes)
    if len(prediction.boxes) == 0:
        # create a path object and get only the name for the file path
        image = Path(prediction.path).stem
        # get the folder the outputs are being saved into
        txt_file = Path(predictions[0].save_dir)/"labels"/(image+".txt")
        txt_file.touch()

print(f"Total Number of Prediction Files: {len(predictions)}")
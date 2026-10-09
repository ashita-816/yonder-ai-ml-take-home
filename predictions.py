import argparse
from ultralytics import YOLO

parser = argparse. ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()
input_folder = args.input
output_folder = args.output
 
model = YOLO("runs/detect/test_run2/weights/best.pt")
predictions = model.predict(source = input_folder, project = output_folder, save = True, save_txt = True, save_conf= True)
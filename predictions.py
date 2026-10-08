import os
from ultralytics import YOLO

model = YOLO("runs/detect/test_run2/weights/best.pt")
predictions = model.predict(source = "Sampled-YD-Object-Detection-2/valid/images", save = True, save_txt = True, save_conf= True)
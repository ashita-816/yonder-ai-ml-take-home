from ultralytics import YOLO

# in order to accept any input folder and create an output folder
input_folder = input("Please enter folder with images: ")
output_folder = input("Please enter a folder to save output: ")
 
model = YOLO("runs/detect/test_run2/weights/best.pt")
predictions = model.predict(source = input_folder, project = output_folder, save = True, save_txt = True, save_conf= True)
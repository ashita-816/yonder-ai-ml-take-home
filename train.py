from ultralytics import YOLO

# already trained model from YOLO
model = YOLO("yolov8n.pt")
# train model with data (getting from yaml file)
# made epoch, batch size, and image size p low for now so it wont take too much memory and time
results = model.train(data = "Sampled-YD-Object-Detection-2/data.yaml", epochs=50, imgsz = 512, batch = 4, name = "test_run_final", device="mps", scale = 0.7, patience = 10)
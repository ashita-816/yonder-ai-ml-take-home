from roboflow import Roboflow
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("ROBOFLOW_API_KEY")
# keep api key private (put in personal environment)
rf = Roboflow(api_key= api_key)
project = rf.workspace("malletbottle2").project("sampled-yd-object-detection")
version = project.version(2)
dataset = version.download("yolov8")
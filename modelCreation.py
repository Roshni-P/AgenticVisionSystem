from huggingface_hub import hf_hub_download
from ultralytics import YOLO

# Download model and export to ONNX format
model_path = hf_hub_download(repo_id="openvision/yolo26-s", local_dir="./models", filename="model.pt")
model = YOLO(model_path)
success = model.export(format="onnx", imgsz=640)


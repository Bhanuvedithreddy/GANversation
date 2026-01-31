import os
import torch
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GALLERY_DIR = os.path.join(BASE_DIR, "static", "gallery")
MODEL_DIR = os.path.join(BASE_DIR, "models")
os.makedirs(GALLERY_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
IMAGE_SIZE = 1024
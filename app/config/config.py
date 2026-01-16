# app/config.py
import os
import numpy as np
CURRENT_FILE_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.dirname(CURRENT_FILE_DIR)
PROJECT_ROOT_DIR = os.path.dirname(APP_DIR)
MODEL_PATH = os.path.join(PROJECT_ROOT_DIR, "models", "best_model_daging_improved_final.h5")
OOD_THRESHOLD = 0.90
CLASS_NAMES = ['FRESH', 'NOT_FRESH']  
IMAGE_SIZE = (224, 224)
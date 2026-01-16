import albumentations as A
import numpy as np
import cv2 
from fastapi import HTTPException

val_test_transform = A.Compose([
    A.Resize(224, 224),
    A.Normalize(),   
])

async def pre_process(image_data: bytes):
    try:
        np_arr = np.frombuffer(image_data, np.uint8)
        np_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR) 
        if np_image is None:
            raise ValueError("Cannot decode image data. The file may be corrupt or not a supported image format.")
        original_height, original_width, _ = np_image.shape
        np_image_rgb = cv2.cvtColor(np_image, cv2.COLOR_BGR2RGB)
        augmented = val_test_transform(image=np_image_rgb)
        img_array = augmented["image"]
        img_array = np.expand_dims(img_array, axis=0).astype(np.float32)
        processed_image_dimensions = img_array.shape[1:]
        return img_array, original_width, original_height, processed_image_dimensions
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Image processing failed: {e}")
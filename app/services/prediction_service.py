from fastapi import  UploadFile, HTTPException
from datetime import datetime
import numpy as np
from app.lib import (load_model, pre_process)
from app.types import APIResponse
from app.config import (IMAGE_SIZE, CLASS_NAMES, OOD_THRESHOLD)

async def predict_freshness(file: UploadFile) -> APIResponse:
            start_time = datetime.now()
            if not file.content_type or not file.content_type.startswith("image/"):
                raise HTTPException(status_code=400, detail="File must be an image")
            image_bytes = await file.read()
            model = load_model()
            img_array, original_width, original_height, processed_dims = await pre_process(image_bytes)
            raw_predictions = model.predict(img_array)
            raw_probs = raw_predictions[0]
            confidence = float(np.max(raw_probs))
            predicted_index = int(np.argmax(raw_probs))
            is_ood = confidence < OOD_THRESHOLD
            predicted_class = CLASS_NAMES[predicted_index] if not is_ood else "NOT_MEAT"
            raw_probabilities_dict = {CLASS_NAMES[i]: float(raw_probs[i]) for i in range(len(CLASS_NAMES))}
            raw_model_output = raw_probs.tolist()
            end_time = datetime.now()
            processing_time_ms = (end_time - start_time).total_seconds() * 1000
            return {
                "success": True,
                "status": "ok",
                "message": "Prediction successful",
                "data": {
                    "filename": file.filename,
                    "file_content_type": file.content_type,
                    "input_image_info": {
                        "original_dimensions": {"width": original_width, "height": original_height},
                        "processed_dimensions_for_model": {
                            "height": processed_dims[0],
                            "width": processed_dims[1],
                            "channels": processed_dims[2]
                        },
                        "target_image_size_for_model": IMAGE_SIZE
                    },
                    "model_info": {
                        "output_class_names": CLASS_NAMES,
                        "prediction_type": "softmax_with_threshold"
                    },
                    "raw_model_output": raw_model_output,
                    "raw_probabilities_by_class_name": raw_probabilities_dict,
                    "overall_prediction": {
                        "class": predicted_class,
                        "confidence_percentage": f"{confidence:.2%}",
                        "confidence_raw_value": confidence
                    },
                    "processing_time_ms": round(processing_time_ms, 2),
                },
                "meta": {
                    "timestamp": datetime.now().isoformat(),
                }
            }
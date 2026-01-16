from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime
from app.services.prediction_service import predict_freshness
prediction_router = APIRouter()
@prediction_router.post("/predict-freshness", response_model=dict)
async def predict_router(
    file: UploadFile = File(...),
    ):
        try:
            response_data = await predict_freshness( file)
            return JSONResponse(status_code=200, content=response_data)
        except HTTPException as http_ex:
            return JSONResponse(
                status_code=http_ex.status_code,
                content={
                    "success": False,
                    "status": "error",
                    "message": "Image validation failed",
                    "error": {
                        "detail": http_ex.detail,
                        "type": "HTTPException"
                    },
                    "meta": {
                        "timestamp": datetime.now().isoformat(),
                    }
                }
            )

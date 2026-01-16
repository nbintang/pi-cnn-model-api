# main.py
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["OMP_NUM_THREADS"] = "4"
from fastapi import FastAPI
from app.router.prediction_routes import prediction_router
app = FastAPI(
    title="Meat Freshness Classification API",
    description="API untuk mengklasifikasikan kesegaran daging (Segar/Busuk) menggunakan model TensorFlow/Keras.",
)
@app.get("/")
async def root():
    return {"message": "Welcome to the Freshness Classification API!"}
app.include_router(prefix="/api", router=prediction_router)

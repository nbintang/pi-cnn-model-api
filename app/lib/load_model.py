import tensorflow as tf # type: ignore
from functools import lru_cache
from app.config import MODEL_PATH
@lru_cache(maxsize=2) 
def load_model():
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        return model 
    except Exception as e:
        raise RuntimeError(f"❌ Gagal load model: {e}")

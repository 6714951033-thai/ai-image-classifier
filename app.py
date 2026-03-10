from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io
from model import predict

app = FastAPI()

@app.get("/")
def home():
    return {"message":"AI Image Classifier API"}

@app.post("/predict")
async def classify(file: UploadFile = File(...)):

    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    result = predict(image)

    return {"prediction": result}
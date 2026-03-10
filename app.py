from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image
import io
from model import predict

app = FastAPI()

# เปิดโฟลเดอร์ static
app.mount("/static", StaticFiles(directory="static"), name="static")

# หน้าเว็บหลัก
@app.get("/")
def home():
    return FileResponse("static/index.html")

@app.post("/predict")
async def classify(file: UploadFile = File(...)):

    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")

    result = predict(image)

    return {"prediction": result}
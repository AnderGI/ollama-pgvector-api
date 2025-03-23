from fastapi import FastAPI, UploadFile, Response, File
from pydantic import UUID4
import os

app = FastAPI()

@app.get('/status')
def status():
  return Response(status_code=200)


@app.put('/embed/{download_uuid}')
async def embed_text(download_uuid: UUID4, file:UploadFile = File(...)):
  file_location = f"{download_uuid}_{file.filename}"

  with open(file_location, "wb") as f:
    chunk = await file.read(1024)
    while chunk:
      f.write(chunk)
      chunk = await file.read(1024)

  return Response(status_code=202)

from fastapi import FastAPI, UploadFile, Response, File
from pydantic import UUID4
from langchain_ollama import OllamaEmbeddings

app = FastAPI()
nomic = OllamaEmbeddings(model='nomic-embed-text:latest', base_url="http://localhost:11434")


@app.get('/status')
def status():
  return Response(status_code=200)


@app.put('/embed/{download_uuid}')
async def embed_text(download_uuid: UUID4, file: UploadFile = File(...)):
    file_location = f"{download_uuid}_{file.filename}"
    
    # Save the file first
    try:
        with open(file_location, "wb") as f:
            content = await file.read()  # Read the entire file at once
            f.write(content)
    except Exception as e:
        print(f"Error saving file: {str(e)}")
        return Response(status_code=500, content=f"Error saving file: {str(e)}")
    
    # Now read the saved file for processing
    try:
        with open(file_location, "rb") as f:
            content = f.read()
        
        text_content = content.decode('utf-8', errors='replace')
        list_of_embeddings = nomic.embed_documents([text_content])
        embedding = list_of_embeddings[0] 
        print(embedding)

  

        return Response(status_code=202)
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        return Response(status_code=500, content=f"Error processing file: {str(e)}")

import os
import uuid

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from random import randint
from pydantic import Basemodel # data validation

# generate images
from ml import obtain_image

app = FastAPI()

IMAGEDIR = "images/"

'''
TODO: 
    load sample images into FastAPI : done!
    use Pillow to load images
    use some ML libraries to predict those images
'''

@app.get("/")
async def root():
    return {"message": "let's process some images!"}


@app.post("/uploadfile/")
async def create_upload_file_fastapi(file: UploadFile):
    """Standard fastapi function to upload a file.
    This doesn't write out the file content than a success response.

    Return --> 
        {
            "filename": "test.csv"
        }
    """
    return {"filename": file.filename}


@app.post("/files/")
async def create_file_fastapi(file: bytes = File()):
    """Standard fastapi function that allows you to choose a file to create.
    You will need to add code to write out content here too.
    
    Return --> 
        {
            "file_size": 27746
        }
    """
    return {"file_size": len(file)}
 
 
@app.post("/uploadimage/")
async def upload_image(file: UploadFile = File(...)):
    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()
    # save the file
    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)
    return {"filename": file.filename}
 
 
@app.get("/show/")
async def populate_random_image():
    """Gets random images from the directory and show it in the response body."""
    files = os.listdir(IMAGEDIR)
    random_index = randint(0, len(files) - 2)
    path = f"{IMAGEDIR}{files[random_index]}"
    return FileResponse(path)

@app.get("/generate")
def generate_image(prompt: str):
    return {"prompt": prompt}

if __name__ == "__main__":
    uvicorn.run(app, debug=True)

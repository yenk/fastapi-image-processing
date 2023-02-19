import os

from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "let's process some images!"}

'''
TODO: 
    load sample images into FastAPI
    use Pillow to load images
    use some ML libraries to predict those images
    
'''
# @app.post("/files/")
# async def create_file(file: bytes | None = File(default=None)):
#     if not file:
#         return {"message": "No file sent"}
#     else:
#         return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    '''Load the images'''
    return {"filename": file.filename}

# @app.post("/files")
# async def UploadImage(file: bytes = File(...)):
#     with open('image.jpg','wb') as image:
#         image.write(file)
#         # image.close()
#     return 'got it'


@app.get("/images")
def load_images():
    for file in os.listdir("../images"):
        

# @app.get("/static")
# def get_images():
#     output = [o for o in os.listdir("static/")]
#     return out

@app.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


if __name__ == "__main__":
    uvicorn.run(app, debug=True)

import os
# import uvicorn

from fastapi import FastAPI, File, UploadFile
from starlette.responses import RedirectResponse

# from application.components import predict, read_imagefile
# from application.schema import Symptom
# from application.components.prediction import symptom_check

app_desc = """<h2>Try this app by uploading any image with `predict/image`</h2>
<h2>Try Covid symptom checker api - it is just a learning app demo</h2>
<br>by Aniket Maurya"""

app = FastAPI(title='Tensorflow FastAPI Starter Pack', description=app_desc)


@app.post("/static/")
async def predict_api(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    image = read_imagefile(await file.read())
    prediction = predict(image)
    return prediction

@app.get("/static")
def get_images():
    output = [o for o in os.listdir("static/")]
    return out

@app.get


if __name__ == "__main__":
    uvicorn.run(app, debug=True)
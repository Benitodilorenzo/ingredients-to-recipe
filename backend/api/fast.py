from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Optional, good practice for dev purposes. Allow all middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


# http://127.0.0.1:8000/predict?x=1
@app.get("/predict")
def predict(x):
    if x=="1":
        return {"ingredients": ["radieschen","majoran","karotten","olivenol","meersalz","weisser-pfeffer"]}
    elif x=="2":
        return {"ingredients": ["kichererbsenmehl","orange","apfelessig","radieschen","olivenol","senf","ahornsirup"]}
    else:
        return {"ingredients": ["schalotten","knoblauch","olivenol","basilikum","rigatoni"]}


@app.get("/")
def root():
    return {
    'greeting': 'Hello World!'
}

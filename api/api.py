from fastapi import FastAPI
from googletrans import Translator
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

translator = Translator()


@ app.get("/{title}/{ln}")
async def hello(title, ln):
    return translator.translate(str(title.replace("zzz", " ")), dest=str(ln)).text

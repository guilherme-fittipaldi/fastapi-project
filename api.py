from fastapi import FastAPI
from googletrans import Translator

translator = Translator()

app = FastAPI()


@ app.get("/{title}/{ln}")
async def hello(title, ln):
    print(translator.translate(str(title.replace("zzz", " ")), dest=str(ln)))
    return translator.translate(str(title.replace("zzz", " ")), dest=str(ln)).text

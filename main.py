from fastapi import FastAPI, UploadFile, File
from scraper import get_site_data
from ai_formatter import format_answer
from translator import translate_bn
from sites import SITES

app = FastAPI(title="Cyber Security AI Learning API")

@app.get("/")
def home():
    return {
        "message": "Cyber AI Learning API Running",
        "sites": len(SITES)
    }


@app.get("/sites")
def list_sites():
    return SITES


@app.get("/learn/{site}")
def learn(site:str, mode:str="short", bangla_style:str="colloquial"):

    if site not in SITES:
        return {"error":"site not found"}

    data = get_site_data(SITES[site]["url"])

    formatted = format_answer(data,mode)

    bangla = translate_bn(formatted,bangla_style)

    return {
        "site":site,
        "english":formatted,
        "bangla":bangla
    }


@app.post("/image")
async def image_upload(file:UploadFile=File(...)):

    return {
        "message":"Image received",
        "filename":file.filename
    }

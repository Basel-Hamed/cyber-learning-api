from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sites import SITES

app = FastAPI(title="Cyber Security Learning API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def root():
    return {
        "message": "🛡️ Cyber Security Learning API Running",
        "total_sites": len(SITES)
    }


@app.get("/sites")
def list_sites():
    return {
        "total": len(SITES),
        "sites": SITES
    }


@app.get("/site/{site_id}")
def get_site(site_id: str):

    if site_id not in SITES:
        raise HTTPException(status_code=404, detail="Site not found")

    return SITES[site_id]

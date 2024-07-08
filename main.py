from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utils import initialize_crawler, run_crawl, process_results
from storage import Storage

app = FastAPI()

class CrawlConfig(BaseModel):
    url: str
    depth: int

storage = Storage()

@app.post("/start")
async def start_crawl(config: CrawlConfig):
    try:
        crawler = initialize_crawler(config.url, config.depth)
        run_crawl(crawler)
        return {"message": "Crawling started"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/status")
async def get_status():
    try:
        status = storage.get_status()
        return {"status": status}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/results")
async def get_results():
    try:
        results = storage.retrieve_data()
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

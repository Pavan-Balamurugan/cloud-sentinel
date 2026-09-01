from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.opensearch_client import index_log
from app.schemas import LogEvent

app = FastAPI(title="Cloud Sentinel - Log Collector")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/logs")
def receive_log(event: LogEvent):
    try:
        doc = event.model_dump(mode="json")
        index_log(doc)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Failed to index log: {e}")
    return {"status": "indexed"}


@app.post("/logs/batch")
def receive_logs_batch(events: list[LogEvent]):
    failed = 0
    for event in events:
        try:
            index_log(event.model_dump(mode="json"))
        except Exception:
            failed += 1
    return {"status": "processed", "count": len(events), "failed": failed}


@app.get("/health")
def health():
    return {"status": "ok"}
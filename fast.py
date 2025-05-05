from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI()

@app.get("/utc-time")
def get_utc_time():
    utc_now = datetime.now(timezone.utc)
    return {"utc_time": utc_now.isoformat()}

# To run this app, save it as `main.py` and use the following command:
# uvicorn main:app --reload

import datetime
from fastapi import FastAPI # type: ignore

app = FastAPI(root_path="/api/v1")

data : Any = [
    {
     "campaign_id":"1",
     "name":"summer",
     "due_date" : datetime.datetime.now(),
     "created_at": datetime.datetime.now()
    },
    {
     "campaign_id":"1",
     "name":"summer",
     "due_date" : datetime.datetime.now(),
     "created_at": datetime.datetime.now()
    },
    {
     "campaign_id":"2",
     "name":"monsoon",
     "due_date" : datetime.datetime.now(),
     "created_at": datetime.datetime.now()
    },
    {
     "campaign_id":"3",
     "name":"winter",
     "due_date" : datetime.datetime.now(),
     "created_at": datetime.datetime.now()
    }
]

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/campaigns")
async def read_campaign():
    return {"campaigns": data}
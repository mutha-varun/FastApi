import datetime
from typing import Any
from fastapi import FastAPI, HTTPException, Request, Response # type: ignore

app = FastAPI(root_path="/api/v1")

data : Any = [
    {
     "campaign_id":1,
     "name":"summer",
     "due_date" : datetime.datetime.now(),
     "created_at": datetime.datetime.now()
    },
    {
     "campaign_id":2,
     "name":"monsoon",
     "due_date" : datetime.datetime.now(),
     "created_at": datetime.datetime.now()
    },
    {
     "campaign_id":3,
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

@app.get("/campaigns/{id}")
async def read_campaign(id: int):
    for campaign in data:
        if campaign.get("campaign_id")  == id:
            return {"campaign": campaign}
    raise HTTPException(status_code=404)

@app.post("/campaigns")
def create_campaign(body: dict[str, Any]):
    
    new : Any = {
        "campaign_id": 100,
        "name":body.get("name"),
        "created_at":datetime.datetime.now(),
        "due_date": body.get("due_date")
    }
    
    data.append(new)
    return {"campaign": new}

@app.put("/campaigns/{id}")
async def update_campaigns(id:int ,body: dict[str,Any]):
    
    for index, campaign in enumerate(data):
        if campaign.get("campaign_id") == id:
            updated : Any = {
                "camapaign_id": id,
                "name": body.get("name"),
                "due_date": body.get("due_date"),
                "created_at": campaign.get("created_at")
            }
            data[index] = updated
            return {"campaign": updated}
    raise HTTPException(status_code=404)


@app.delete("/campaigns/{id}")
async def update_campaigns(id:int):
    
    for index, campaign in enumerate(data):
        if campaign.get("campaign_id") == id:
            data.pop(index)
            return Response(status_code=204)
    raise HTTPException(status_code=404)
    
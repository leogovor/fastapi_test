#need 2 get FastAPI: pip install fastapi, and ASGI server pip install uvicorn
from typing import Union

from fastapi import FastAPI
import json
from datetime import datetime
app = FastAPI()

@app.get("/")

def read_root():
    return {"Hello": "World", "time": datetime.now().strftime('%d/%h/%y')}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


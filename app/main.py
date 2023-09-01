#need 2 get FastAPI: pip install fastapi, and ASGI server pip install uvicorn
import datetime
from typing import Union
import requests
from fastapi import FastAPI

app = FastAPI()
ip = requests.get('https://api.ipify.org').content.decode('utf8')
print('My public IP address is: {}'.format(ip))

@app.get("/")

def read_root():
    return {"Hello": "Researcher!", "Date": datetime.datetime.now().strftime('%d/%h/%y'), "your public ip is:":(ip)}
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


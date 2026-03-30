from fastapi import FastAPI
from logic import get_price, get_sla

app = FastAPI()

@app.get("/price")
def price(product: str, country: str, user_type: str):
    return {"price": get_price(product, country, user_type)}

@app.get("/sla")
def sla(user_type: str):
    return {"sla": get_sla(user_type)}
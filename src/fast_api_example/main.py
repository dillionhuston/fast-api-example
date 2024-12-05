from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    item_id: int
    query: str | None


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, query: str | None = None) -> Item:
    return Item(item_id=item_id, query=query)

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Worlds"}


@app.get("/items/{item_id}")
def read_item(item_id, q):
    return {"item_id": item_id, "q": q}

# how to run:
# uvicorn src.main:app --reload
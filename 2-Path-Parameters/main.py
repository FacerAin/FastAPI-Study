from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")

async def read_item(item_id: int):
    #https://127.0.0.1/items/3이라 입력해도 Int형 3으로 인식 => Data Conversion
    #https://127.0.0.1/items/foo HTTP Error!! => Data Validation

    return {"item_id": item_id}

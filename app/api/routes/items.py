from fastapi import APIRouter, HTTPException
from app.database.db import db

router = APIRouter()


@router.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    return db[item_id]


@router.post("/items/{item_id}")
async def create_item(item_id: int, item: str):
    if item_id in db:
        raise HTTPException(status_code=400, detail="Item already exists")
    db[item_id] = item
    return {"item": db[item_id], "item_id": item_id}


@router.put("/items/{item_id}")
async def update_item(item_id: int, item: str):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    db[item_id] = item
    return {"item": db[item_id], "item_id": item_id}


@router.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    del db[item_id]
    return {"detail": f"Item {item_id} deleted."}

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from bson import ObjectId
from typing import List

# MongoDB connection
client = MongoClient("mongodb://localhost:27017")
db = client["bookstore"]
collection = db["books"]

app = FastAPI()

# Pydantic model for the book data
class Book(BaseModel):
    id: str
    title: str
    author: str
    description: str
    price: float
    stock: int

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

# API Endpoints
@app.get("/books", response_model=List[Book])
async def get_books():
    books = list(collection.find())
    return [Book(id=str(book["_id"]), **book) for book in books]

@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: str):
    book = collection.find_one({"_id": ObjectId(book_id)})
    if book:
        return Book(id=str(book["_id"]), **book)
    else:
        raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books", response_model=Book)
async def add_book(book: Book):
    try:
        result = collection.insert_one(book.dict())
        book_id = result.inserted_id
        book = collection.find_one({"_id": book_id})
        return book
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail="Failed to add book to the database")

@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: str, book: Book):
    try:
        result = collection.replace_one({"_id": book_id}, book.dict())
        if result.matched_count:
            book = collection.find_one({"_id": book_id})
            return book
        else:
            raise HTTPException(status_code=404, detail="Book not found")
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail="Failed to update book in the database")

@app.delete("/books/{book_id}")
async def delete_book(book_id: str):
    try:
        result = collection.delete_one({"_id": book_id})
        if result.deleted_count:
            return {"message": "Book deleted"}
        else:
            raise HTTPException(status_code=404, detail="Book not found")
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail="Failed to delete book from the database")

@app.get("/search")
async def search_books(title: str = None, author: str = None, min_price: float = None, max_price: float = None):
    query = {}
    if title:
        query["title"] = {"$regex": title, "$options": "i"}
    if author:
        query["author"] = {"$regex": author, "$options": "i"}
    if min_price is not None:
        query["price"] = {"$gte": min_price}
    if max_price is not None:
        query.setdefault("price", {})["$lte"] = max_price
    books = list(collection.find(query))
    return books



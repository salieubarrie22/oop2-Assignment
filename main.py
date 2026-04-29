from fastapi import FastAPI
from  pydantic import BaseModel

app = FastAPI()

# Models
class Book(BaseModel):
    id: int
    title: str
    author: str
    available: bool = True

books = []
@app.post("/books/")
def add_book(book: Book):
    return books

@app.get("/books/")
def get_books():
    return books

@app.put("/books/{book_id}")
def update_book(book_id: int, updated:Book):
    for book in books:
        if book.id == book_id:
            book.title = updated.title
            book.author = updated.author
            return {"message": "Book updated"}
        return {"error": "Book not found"}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book.id == book_id:
            books.remove(book)
            return {"message": "Book deleted"}
        return {"error": "Book not found"}
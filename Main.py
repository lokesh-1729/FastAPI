from fastapi import Body, FastAPI
app=FastAPI()#create a app variable to access fastapi


Books=[
    {"title":"alchemist","author":"paulo coehlo","category":"fiction"},
    {"title":"rich dada poor dad","author":"chinese","category":"self help"},
    {"title":"alchemist","author":"paulo coehlo","category":"fiction"},
    {"title":"psychology of money","author":"jackson","category":"science"}
]

#adding decorators 
@app.get("/")
async def first_api():
    return{"message":"hello Lokesh"}

@app.get("/books")
async def books():
    return Books

@app.get("/books/{dynamic_param}")
async def read_allbooks(dynamic_param : str):
    for book in Books:
        if book.get("title").casefold()==dynamic_param.casefold():
            return book

@app.get("/books/")
async def read_book_by_category(category : str):
    category_books=[]
    for book in Books:
        if book.get("category").casefold()==category:
            category_books.append(book)
    return category_books

@app.get("/books/{book_param}/")
async def get_by_name_catgeory(book_param : str, category : str):
    for book in Books:
        if book.get("title").casefold()==book_param.casefold() and book.get("category").casefold()==category.casefold():
            return book
    return "not found"

@app.post("/books/added_book")
async def add_book(new_book=Body()):
    Books.append(new_book)
    return "Book added"

@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(Books)):
        if Books[i].get("title").casefold()==updated_book.get("title").casefold():
            Books[i]=updated_book
    return "changes made"

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(Books)):
        if Books[i].get("title").casefold()==book_title.casefold():
            Books.pop(i)
            return "Book deleted"
    


        
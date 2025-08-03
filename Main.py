from fastapi import FastAPI
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


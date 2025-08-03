from fastapi import FastAPI
app=FastAPI()#create a app variable to access fastapi


Books=[
    {"title":"alchemist","author":"paulo coehlo"},
    {"title":"rich dada poor dad","author":"chinese"},
    {"title":"alchemist","author":"paulo coehlo"},
    {"title":"psychology of money","author":"jackson"}
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




from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
from time import sleep

app = FastAPI(
    debug=True,
)


@app.get("/")
def main():
    html = open("index.html", "r").read()
    return HTMLResponse(html)


@app.post("/clicked")
def when_clicked():
    return "<b>this button is clicked</b>"


sec = 10


@app.get("/start_timer")
def cntdown():
    global sec
    while sec > 0:
        sec -= 1
        print(sec)
        return f"{sec}"


data = [
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publisher": "Scribner",
        "published_date": "April 10, 1925",
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publisher": "J. B. Lippincott & Co.",
        "published_date": "July 11, 1960",
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "publisher": "Secker & Warburg",
        "published_date": "June 8, 1949",
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "publisher": "T. Egerton, Whitehall",
        "published_date": "January 28, 1813",
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "publisher": "Little, Brown and Company",
        "published_date": "July 16, 1951",
    },
]


@app.get("/tbl")
def tbl():
    global data
    html = ""
    for d in data:
        html += f"<tr><td>{d['title']}</td><td>{d['author']}</tr>"
    print(html)
    return HTMLResponse(html)


@app.get("/search")
def search(title: str):
    global data
    html = ""
    for d in data:
        if not (title and title in d["title"].lower()):
            continue
        html += f"<tr><td>{d['title']}</td><td>{d['author']}</tr>"
    print(html)
    return HTMLResponse(html)


@app.get("/getting")
def getting(x):
    print("!!!!!!!!!!!", x)
    return str(x)


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)

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


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)

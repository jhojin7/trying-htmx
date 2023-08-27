from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

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


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)

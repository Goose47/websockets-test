from fastapi import FastAPI, WebSocket
import time
app = FastAPI()


@app.get("/")
async def get():
    return 'heloe worldo'


@app.websocket("/echo")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")


@app.websocket("/pidor")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        time.sleep(1)
        await websocket.send_text(f"ty pidor")


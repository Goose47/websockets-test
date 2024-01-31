from fastapi import FastAPI, WebSocket
import asyncio

app = FastAPI()


@app.get("/")
async def get():
    return 'heloe worldo'


@app.get("/hehehe")
async def get():
    return 'ha'


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
        await asyncio.sleep(1)
        await websocket.send_text(f"ty pidor")


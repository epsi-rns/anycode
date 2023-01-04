import asyncio
import websockets

async def push_client():
  async with websockets.\
    connect("ws://localhost:8765") as websocket:
    while True:
      data = await websocket.recv()
      print("Received data:", data)

loop = asyncio.new_event_loop()
loop.run_until_complete(push_client())

import asyncio, websockets
from watchfiles import awatch

# Excel to Web, Class Example
class Xl2WebExample:
  def __init__(self, filepath, filename, site, port):
    # save initial parameter
    self.filepath = filepath
    self.filename = filename
    self.site = site
    self.port = port

  # websocket handler
  async def handler(self, websocket, path):
    self.websocket = websocket

    async for changes in awatch(self.filepath):
      for change in changes:
        print(change[0])
        print(change[1])
        await websocket.send(change[1])

  async def main(self):
    # Start the server
    server = await websockets.serve(
      self.handler, self.site, self.port)
    await server.wait_closed()

# Program Entry Point
example = Xl2WebExample(
  '/home/epsi/awatch', 'test-a.xlsx',
  'localhost', 8765)
asyncio.run(example.main())

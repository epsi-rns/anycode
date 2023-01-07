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
  async def __handler(self, websocket, path):
    self.websocket = websocket

    async for changes in awatch(self.filepath):
      xlsx = self.filepath + '/' + self.filename

      for change in changes:
        if change[1] == xlsx:
          print(change[1])
          await websocket.send(change[1])

  async def main(self):
    # Start the server
    server = await websockets.serve(
      self.__handler, self.site, self.port)
    await server.wait_closed()

# Program Entry Point
example = Xl2WebExample(
  '/home/epsi/awatch/code', 'test-a.xlsx',
  'localhost', 8765)
asyncio.run(example.main())

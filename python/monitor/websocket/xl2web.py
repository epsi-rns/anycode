import asyncio, websockets, json, os
# import Xl2WebBase
from watchfiles import awatch

# Excel to Web, Base Class
class Xl2WebBase:
  def __init__(self, filepath, filename, site, port):
    # save initial parameter
    self.filepath = filepath
    self.filename = filename
    self.site = site
    self.port = port

  # websocket related
  async def __send_data(self, fullname):
    event_data = self._pack_data(fullname)
    self._dump_data(event_data)
    await self.websocket.send(
      json.dumps(event_data))

  async def __monitor_localfile(self):
    async for changes in awatch(self.filepath):
      self.xlsx = os.path.join(self.filepath, self.filename)
      for change in changes:
        if change[1] == self.xlsx:
          print(change[0])
          await self.__send_data(change[1])

  async def __monitor_webclient(self):
    while True:
      message = await self.websocket.recv()
      self.xlsx = os.path.join(self.filepath, self.filename)
      await self.__send_data(None)

  # websocket handler
  async def __handler(self, websocket, path):
    self.websocket = websocket

    task_localfile = asyncio.create_task(
      self.__monitor_localfile())

    task_webclient = asyncio.create_task(
      self.__monitor_webclient())

    # run these two coroutines concurrently
    await(task_localfile)
    await(task_webclient)

  async def main(self):
    # Start the server
    server = await websockets.serve(
      self.__handler, self.site, self.port)
    await server.wait_closed()

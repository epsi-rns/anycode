import asyncio
from watchfiles import awatch

# Excel to Web, Class Example
class Xl2WebExample:
  def __init__(self, filepath, filename):
    # save initial parameter
    self.filepath = filepath
    self.filename = filename

  async def main(self):
    async for changes in awatch(self.filepath):
      print(changes)

# Program Entry Point
example = Xl2WebExample(
  '/home/epsi/awatch', 'test-a.xlsx')
asyncio.run(example.main())

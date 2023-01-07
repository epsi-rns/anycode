# Excel to Web, Class Example
class Xl2WebExample:
  def __init__(self, filepath, filename):
    # save initial parameter
    self.filepath = filepath
    self.filename = filename

  def main(self):
    # Running Main Method
    print("Target: %s/%s"
      % (self.filepath, self.filename))

# Program Entry Point
example = Xl2WebExample(
  '/home/epsi/awatch/code', 'test-a.xlsx')
example.main()

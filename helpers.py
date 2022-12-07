def openFile(file="input.txt"):
  f = open(file, "r")
  readedFile = f.read()
  f.close()
  return readedFile

def splitByLine(value):
  return value.split("\n")

def splitTwoLines(value):
  return value.split("\n\n")

def testing(part, inputFile=False):
  return part(inputFile) if inputFile else part()

def getExample(day):
  return f"inputFiles/{day}/example.txt"

def getInput(day):
  return f"inputFiles/{day}/input.txt"

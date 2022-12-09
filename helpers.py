def openFile(inputFile):
  f = open(inputFile, "r") if inputFile else open("input.txt", "r")
  readedFile = f.read()
  f.close()
  return readedFile

def splitLines(value, lines=1):
  splitVal = ""
  for x in range(0,lines):
    splitVal = f"{splitVal}\n"
  return value.split(splitVal)

def getExample(day):
  return f"inputFiles/{day}/example.txt"

def getInput(day):
  return f"inputFiles/{day}/input.txt"

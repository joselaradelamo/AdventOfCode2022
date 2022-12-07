from helpers import openFile

def launch_function(numberOfLetters, inputFile):
  letters = openFile(inputFile)
  finalIndex=0
  actualStartIndex=0
  values=[]
  for letter in letters:
    if len(values) < numberOfLetters:
      repeated = values.index(letter) if letter in values else -1
      if repeated > -1:
        actualStartIndex += repeated + 1
        while repeated > -1:
          values.pop(repeated)
          repeated -= 1
      values.append(letter)
      finalIndex += 1
    else:
      return finalIndex

def part1(inputFile):
  return launch_function(4, inputFile)

def part2(inputFile):
  return launch_function(14, inputFile)
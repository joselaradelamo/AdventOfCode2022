from helpers import openFile,splitByLine,splitTwoLines
import re

def doMovements(cratesArray, inputValue, part):
  orders = splitByLine(inputValue)
  for order in orders:
    x,movements,y,init,z,to = re.split("\s", order)
    positionInit = int(init)-1
    positionTo = int(to)-1
    if part == 1:
      for mov in range(int(movements)):
        valueToInsert = cratesArray[positionInit][0]
        cratesArray[positionTo].insert(0, valueToInsert)
        cratesArray[positionInit].pop(0)
    else:
      intermediateArray = []
      for mov in range(int(movements)):
        valueToInsert = cratesArray[positionInit].pop(0)
        intermediateArray.append(valueToInsert)
      intermediateArray.reverse()
      for i in intermediateArray:
        cratesArray[positionTo].insert(0, i)
  return cratesArray

def createCrates(start):
  cratesArray = []; 
  elements = splitByLine(start)
  values = elements.pop()
  numberOfCrates = int(values.split().pop())
  for i in range(numberOfCrates):
    cratesArray.append([])

  for element in elements:
    res = [element[i:i + 4] for i in range(0, len(element), 4)]
    index = 0
    for r in res:
      if re.search(r'^\[[A-Z]\]*', r):
        cratesArray[index].append(r.replace('[', '').replace(']', '').strip())
      index += 1
  return cratesArray

def launch_function(part, inputFile=False):
  data = openFile(inputFile) if inputFile else openFile()
  start,inputValue = splitTwoLines(data)
  cratesArray = createCrates(start)
  cratesResult = doMovements(cratesArray, inputValue, part)
  cratesValue = ''
  for cratesTop in cratesResult:
    cratesValue += cratesTop.pop(0)

  return cratesValue

def part1(inputFile=False):
  return launch_function(1, inputFile) if inputFile else launch_function(1)

def part2(inputFile=False):
  return launch_function(2, inputFile) if inputFile else launch_function(2)
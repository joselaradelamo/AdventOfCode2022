from helpers import openFile,splitLines
import re

def doMovements(cratesArray, inputValue, part):
  orders = splitLines(inputValue)
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
  elements = splitLines(start)
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

def launch_function(part, inputFile):
  data = openFile(inputFile)
  start,inputValue = splitLines(data,2)
  cratesArray = createCrates(start)
  cratesResult = doMovements(cratesArray, inputValue, part)
  cratesValue = ''
  for cratesTop in cratesResult:
    cratesValue += cratesTop.pop(0)

  return cratesValue

def part1(inputFile):
  return launch_function(1, inputFile)

def part2(inputFile):
  return launch_function(2, inputFile)
import openInput
import re

def doMovements(cratesArray, input):
  orders = input.split('\n')
  for order in orders:
    x,movements,y,init,z,to = re.split("\s", order)
    positionInit = int(init)-1
    positionTo = int(to)-1
    for mov in range(int(movements)):
      valueToInsert = cratesArray[positionInit][0]
      cratesArray[positionTo].insert(0, valueToInsert)
      cratesArray[positionInit].pop(0)
  return cratesArray

def createCrates(start):
  cratesArray = []; 
  values = start.split("\n").pop()
  numberOfCrates = int(values.split().pop())
  for i in range(numberOfCrates):
    cratesArray.append([]);

  elements = start.split("\n")
  elements.pop()

  for element in elements:
    res = [element[i:i + 4] for i in range(0, len(element), 4)]
    index = 0
    for r in res:
      if re.search(r'^\[[A-Z]\]*', r):
        cratesArray[index].append(r.replace('[', '').replace(']', '').strip())
      index += 1
  return cratesArray

data = openInput.openFile()

start,input = data.split("\n\n")
cratesArray = createCrates(start)

cratesResult = doMovements(cratesArray, input)
for cratesTop in cratesResult:
  print(cratesTop.pop(0))
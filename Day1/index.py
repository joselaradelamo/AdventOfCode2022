from helpers import openFile,splitByLine,splitTwoLines

def part1(inputFile=False):
  data = openFile(inputFile) if inputFile else openFile()
  x = splitTwoLines(data)
  total = 0 
  for value in x:
    acc = 0
    for num in splitByLine(value):
      acc += int(num)
      if acc > total: total = acc
  return total

def part2(inputFile=False):
  data = openFile(inputFile) if inputFile else openFile()
  x = splitTwoLines(data)
  acc = []
  for value in x:
    el = splitByLine(value)
    elf = 0
    for num in el:
      elf += int(num)
    acc.append(elf)
  acc.sort(reverse=True)
  valueTotal = acc[0:3]
  return sum(valueTotal)

from helpers import openFile,splitLines

def part1(inputFile):
  data = openFile(inputFile)
  x = splitLines(data, 2)
  total = 0 
  for value in x:
    acc = 0
    for num in splitLines(value):
      acc += int(num)
      if acc > total: total = acc
  return total

def part2(inputFile):
  data = openFile(inputFile)
  x = splitLines(data, 2)
  acc = []
  for value in x:
    el = splitLines(value)
    elf = 0
    for num in el:
      elf += int(num)
    acc.append(elf)
  acc.sort(reverse=True)
  valueTotal = acc[0:3]
  return sum(valueTotal)

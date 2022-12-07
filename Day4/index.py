from helpers import openFile,splitByLine

def part1(inputFile=False):
  data = openFile(inputFile) if inputFile else openFile()
  assignments = splitByLine(data)
  total = 0
  for value in assignments:
    part1, part2 = value.split(',')
    part1Start,part1End = part1.split('-')
    part2Start,part2End = part2.split('-')
    twoInsideOne = int(part1Start) <= int(part2Start) and int(part1End) >= int(part2End)
    oneInsideTwo = int(part1Start) >= int(part2Start) and int(part1End) <= int(part2End)
    if twoInsideOne or oneInsideTwo:
      total += 1
  return total

def part2(inputFile=False):
  data = openFile(inputFile) if inputFile else openFile()
  assignments = splitByLine(data)
  total = 0
  for value in assignments:
    part1, part2 = value.split(',')
    part1Start,part1End = part1.split('-')
    part2Start,part2End = part2.split('-')
    startOneBetweenTwo = int(part1Start) >= int(part2Start) and int(part1Start) <= int(part2End)
    endOneBetweenTwo = int(part1End) >= int(part2Start) and int(part1End) <= int(part2End)
    startTwoBetweenOne = int(part2Start) >= int(part1Start) and int(part2End) <= int(part1End)
    endTwoBetweenOne = int(part2End) >= int(part1Start) and int(part2End) <= int(part1End)
    if startOneBetweenTwo or endOneBetweenTwo or startTwoBetweenOne or endTwoBetweenOne:
      total += 1
  return total

from helpers import openFile,splitLines

def is_visible(positionValue, totalArray, topPosition, bottomPosition, rightPosition, leftPosition,  direction):
  result = True
  if (direction == 'up'):
    for topIndex in range(0, int(topPosition)):
      if positionValue <= int(totalArray[topIndex][rightPosition]):
        result = False
  if (direction == 'down'):
    startPosition = topPosition + 1
    for topIndex in range(startPosition, bottomPosition+1):
      if positionValue <= int(totalArray[topIndex][rightPosition]):
        result = False
  if (direction == 'left'):
    for leftIndex in range(0, int(leftPosition)):
      if positionValue <= int(totalArray[topPosition][leftIndex]):
        result = False
  if (direction == 'right'):
    startPosition = leftPosition + 1
    for rightIndex in range(startPosition, rightPosition+1):
      if positionValue <= int(totalArray[topPosition][rightIndex]):
        result = False

  return result
  
def sum_value(positionValue, totalArray, topPosition, bottomPosition, rightPosition, leftPosition,  direction):
  value = 0
  if (direction == 'up'):
    for topIndex in range(int(topPosition)-1, -1, -1):
      if positionValue > int(totalArray[topIndex][rightPosition]):
        value += 1
      else: 
        value += 1
        return value
  if (direction == 'down'):
    startPosition = topPosition + 1
    for topIndex in range(startPosition, bottomPosition+1):
      if positionValue > int(totalArray[topIndex][rightPosition]):
        value += 1
      else:
        value += 1
        return value
  if (direction == 'left'):
    for leftIndex in range(int(leftPosition)-1, -1, -1):
      if positionValue > int(totalArray[topPosition][leftIndex]):
        value += 1
      else:
        value += 1
        return value
  if (direction == 'right'):
    startPosition = leftPosition + 1
    for rightIndex in range(startPosition, rightPosition+1):
      if positionValue > int(totalArray[topPosition][rightIndex]):
        value += 1
      else:
        value += 1
        return value
  return value

def part1(inputFile):
  result = openFile(inputFile)
  lines = splitLines(result)
  totalArray = []
  for line in lines:
    lineArray = []
    for tree in line:
      lineArray.append(tree)
    totalArray.append(lineArray) 
  rigthBorder = len(lines) - 1
  bottomBorder = len(lines) - 1
  visible = (rigthBorder+1) * 4 - 4
  for topIndex in range(1, bottomBorder):
    for leftIndex in range(1, rigthBorder):
      positionValue = int(totalArray[topIndex][leftIndex])
      positionUp = is_visible(positionValue, totalArray, topIndex, bottomBorder, leftIndex, 0,  'up')
      positionDown = is_visible(positionValue, totalArray, topIndex, bottomBorder, leftIndex, 0, 'down')
      positionLeft = is_visible(positionValue, totalArray, topIndex, 0, rigthBorder, leftIndex,  'left')
      positionRight = is_visible(positionValue, totalArray, topIndex, 0, rigthBorder, leftIndex, 'right')
      if positionUp or positionDown or positionLeft or positionRight:
        visible += 1
  return visible


def part2(inputFile):
  result = openFile(inputFile)
  lines = splitLines(result)
  totalArray = []
  for line in lines:
    lineArray = []
    for tree in line:
      lineArray.append(tree)
    totalArray.append(lineArray) 
  rigthBorder = len(lines) - 1
  bottomBorder = len(lines) - 1
  total = 0
  for topIndex in range(1, bottomBorder):
    for leftIndex in range(1, rigthBorder):
      positionValue = int(totalArray[topIndex][leftIndex])
      positionUp = is_visible(positionValue, totalArray, topIndex, bottomBorder, leftIndex, 0,  'up')
      positionDown = is_visible(positionValue, totalArray, topIndex, bottomBorder, leftIndex, 0, 'down')
      positionLeft = is_visible(positionValue, totalArray, topIndex, 0, rigthBorder, leftIndex,  'left')
      positionRight = is_visible(positionValue, totalArray, topIndex, 0, rigthBorder, leftIndex, 'right')
      if positionUp or positionDown or positionLeft or positionRight:
        valueUp = sum_value(positionValue, totalArray, topIndex, bottomBorder, leftIndex, 0,  'up')
        valueDown = sum_value(positionValue, totalArray, topIndex, bottomBorder, leftIndex, 0, 'down')
        valueLeft = sum_value(positionValue, totalArray, topIndex, 0, rigthBorder, leftIndex,  'left')
        valueRight = sum_value(positionValue, totalArray, topIndex, 0, rigthBorder, leftIndex, 'right')
        value = valueUp * valueDown * valueLeft * valueRight    
        if value > total:
          total = value
  return total
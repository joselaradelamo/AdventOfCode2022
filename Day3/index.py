from helpers import openFile,splitLines

def recoverLetter(arrayData):
  firstBack = arrayData[0]
  secondBack = arrayData[1]
  thirdBack = arrayData[2]
  for lettersArray in firstBack:
    if secondBack.find(lettersArray) > -1 and thirdBack.find(lettersArray) > -1:
      return lettersArray

def part1(inputFile):
  data = openFile(inputFile)
  backpacks = splitLines(data)
  letters = []
  for backpack in backpacks:
    a,b = backpack[:len(backpack)//2], backpack[len(backpack)//2:]
    done = False
    for letter in a:
      exists = b.find(letter)
      if exists > -1 and done == False:
        done = True
        value = ord(letter) - 38 if letter.isupper() else ord(letter) - 96
        letters.append(value)
        
  return sum(letters)

def part2(inputFile):
  data = openFile(inputFile)
  backpacks = splitLines(data)
  letters = []
  lines = 0
  group = []
  for backpack in backpacks:
    lines += 1
    group.append(backpack)
    if lines == 3:
      letter = recoverLetter(group)  
      value = ord(letter) - 38 if letter.isupper() else ord(letter) - 96
      letters.append(value)
      lines = 0
      group = []

  return sum(letters)

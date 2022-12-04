def recoverLetter(arrayData):
  secondBack = arrayData[1]
  thirdBack = arrayData[2]
  for lettersArray in arrayData[0]:
    if (secondBack.find(lettersArray) > -1 and thirdBack.find(lettersArray) > -1):
      return lettersArray

import openInput

data = openInput.openFile()
backpacks = data.split("\n");

letters = [];
lines = 0
group = []
for backpack in backpacks:
  lines = lines + 1;
  group.append(backpack)
  if lines == 3:
    letter = recoverLetter(group)    
    if letter.isupper(): 
        value = ord(letter) - 38
    else:
        value = ord(letter) - 96
    letters.append(value)
    lines = 0;
    group = []

print(sum(letters))
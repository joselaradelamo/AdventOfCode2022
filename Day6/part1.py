import openInput
letters = openInput.openFile()

def resolvePart1(letters): 
  index=0
  actualStartIndex=0
  values=[]

  for letter in letters:
    if len(values) < 4:
      repeated = values.index(letter) if letter in values else -1
      if repeated > -1:
        actualStartIndex += repeated + 1
        while repeated > -1:
          values.pop(repeated)
          repeated -= 1
      values.append(letter)
      index += 1
    else:
      return index

print(resolvePart1(letters))
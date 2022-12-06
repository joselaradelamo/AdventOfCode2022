import openInput
letters = openInput.openFile()


def resolvePart2(letters): 
  index=0
  actualStartIndex=0
  values=[]

  for letter in letters:
    if len(values) < 14:
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

print(resolvePart2(letters))
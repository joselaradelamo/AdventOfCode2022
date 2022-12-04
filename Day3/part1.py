import openInput

data = openInput.openFile()
backpacks = data.split("\n");


letters = [];
for backpack in backpacks:
  a,b = backpack[:len(backpack)//2], backpack[len(backpack)//2:]
  done = False
  for letter in a:
    exists = b.find(letter)
    if exists > -1 and done == False:
      done = True
      if letter.isupper(): 
        value = ord(letter) - 38
      else:
        value = ord(letter) - 96
      letters.append(value)
print(sum(letters))
import openInput

data = openInput.openFile()
x = data.split("\n\n");

total = 0;
for value in x:
  acc = 0
  el = value.split("\n")
  for num in el:
    acc = acc + int(num);
    if acc > total:
      total = acc;

print(total)

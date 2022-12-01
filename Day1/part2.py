
f = open("input.txt", "r")
data = f.read();

x = data.split("\n\n");

acc = [];
for value in x:
  el = value.split("\n")
  elf = 0;
  for num in el:
    elf = elf + int(num);
  acc.append(elf);
  
acc.sort(reverse=True)

valueTotal = acc[0:3];
print(sum(valueTotal))

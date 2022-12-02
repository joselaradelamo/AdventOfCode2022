acc = 0

f = open("input.txt", "r")
data = f.read();
x = data.split("\n");

for turns in x:
  turn = turns.split(' ');
  [opponentChoose, myChoose] = turn;
  if myChoose == 'X':
    acc = acc + 1;
    if opponentChoose == 'A':
      acc = acc + 3
    elif opponentChoose == 'C':
      acc = acc + 6
  elif myChoose == 'Y':
    acc = acc + 2;
    if opponentChoose == 'A':
      acc = acc + 6
    elif opponentChoose == 'B':
      acc = acc + 3
  elif myChoose == 'Z':
    acc = acc + 3;
    if opponentChoose == 'B':
      acc = acc + 6
    elif opponentChoose == 'C':
      acc = acc + 3
  
print(acc)
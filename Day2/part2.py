acc = 0

f = open("input.txt", "r")
#f = open("example.txt", "r")
data = f.read();
x = data.split("\n");

for turns in x:
  turn = turns.split(' ');
  [opponentChoose, result] = turn;
  if result == 'X':
    if opponentChoose == 'A':
      acc = acc + 3
    elif opponentChoose == 'B':
      acc = acc + 1
    elif opponentChoose == 'C':
      acc = acc + 2
  elif result == 'Y':
    acc = acc + 3;
    if opponentChoose == 'A':
      acc = acc + 1
    elif opponentChoose == 'B':
      acc = acc + 2
    elif opponentChoose == 'C':
      acc = acc + 3
  elif result == 'Z':
    acc = acc + 6;
    if opponentChoose == 'A':
      acc = acc + 2
    elif opponentChoose == 'B':
      acc = acc + 3
    elif opponentChoose == 'C':
      acc = acc + 1
  
print(acc)
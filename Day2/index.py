from helpers import openFile,splitLines

def part1(inputFile):
  data = openFile(inputFile)
  x = splitLines(data)
  acc = 0

  win = 6
  tie = 3
  playRock = 1
  playPaper = 2
  playScissor = 3

  for turns in x:
    turn = turns.split(' ')
    [opponentChoose, myChoose] = turn
    if myChoose == 'X':
      acc += playRock
      if opponentChoose == 'A':
        acc += tie
      elif opponentChoose == 'C':
        acc += win
    elif myChoose == 'Y':
      acc += playPaper
      if opponentChoose == 'A':
        acc += win
      elif opponentChoose == 'B':
        acc += tie
    elif myChoose == 'Z':
      acc += playScissor
      if opponentChoose == 'B':
        acc += win
      elif opponentChoose == 'C':
        acc += tie
  return acc

def part2(inputFile):
  data = openFile(inputFile)
  x = splitLines(data)
  acc = 0

  win = 6
  tie = 3
  playRock = 1
  playPaper = 2
  playScissor = 3

  for turns in x:
    turn = turns.split(' ')
    [opponentChoose, result] = turn
    if result == 'X':
      if opponentChoose == 'A':
        acc += playScissor
      elif opponentChoose == 'B':
        acc += playRock
      elif opponentChoose == 'C':
        acc += playPaper
    elif result == 'Y':
      acc += tie
      if opponentChoose == 'A':
        acc += playRock
      elif opponentChoose == 'B':
        acc += playPaper
      elif opponentChoose == 'C':
        acc += playScissor
    elif result == 'Z':
      acc += win
      if opponentChoose == 'A':
        acc += playPaper
      elif opponentChoose == 'B':
        acc += playScissor
      elif opponentChoose == 'C':
        acc += playRock
  return acc
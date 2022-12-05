import openInput

data = openInput.openFile()
assignments = data.split("\n")
total = 0
for value in assignments:
  part1, part2 = value.split(',')
  part1Start,part1End = part1.split('-')
  part2Start,part2End = part2.split('-')
  if int(part1Start) >= int(part2Start) and int(part1Start) <= int(part2End):
    total += 1
  elif int(part1End) >= int(part2Start) and int(part1End) <= int(part2End):
    total += 1
  elif int(part2Start) >= int(part1Start) and int(part2End) <= int(part1End):
    total += 1
  elif int(part2End) >= int(part1Start) and int(part2End) <= int(part1End):
    total += 1
  
print(total)

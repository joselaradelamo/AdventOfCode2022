from helpers import openFile,splitByLine
import re

class Directory:
  def __init__(self, name, size):
    self.name = name
    self.size = size

def get_directories_size(lines):
  previousDirectories = []
  directoriesArray = []

  for line in lines:
    if "$" in line:
      if '$ cd ' in line:
        if '..' in line:
          previousDirectories.pop()
        else:
          directoryName = line.replace("$ cd ", "")
          directoryRoot = ''
          dirValue = ''
          for prev in previousDirectories:
            if prev != '/':
              directoryRoot = f"{directoryRoot}{prev}"
          dirValue = directoryName if directoryName == '/' else f"{directoryRoot}/{directoryName}"
          previousDirectories.append(dirValue)
          directoriesArray.append(Directory(dirValue, 0))
    elif(line.find("dir ") == -1):
      for directory in directoriesArray:
        if directory.name in previousDirectories:
          size,name = line.split(' ')
          directory.size += int(size)
  return directoriesArray

def part1(inputFile=False):
  result = openFile(inputFile) if inputFile else openFile()
  lines = splitByLine(result)
  previousDirectories = []
  directoriesArray = get_directories_size(lines)
  sizeTotal = 0
  for directory in directoriesArray:
    if (directory.size <= 100000):
      sizeTotal += int(directory.size)
  return sizeTotal

def part2(inputFile=False):
  result = openFile(inputFile) if inputFile else openFile()
  lines = splitByLine(result)
  directoriesArray = get_directories_size(lines)
  enoughSize = []
  totalSpace = 70000000
  updateSpace = 30000000
  for directory in directoriesArray:
    if (directory.name == '/'):
      unusedSpace = totalSpace - directory.size
  neededSpace = updateSpace - unusedSpace
  for directory in directoriesArray:
    if (directory.size >= neededSpace):
      enoughSize.append(directory.size)
  return min(enoughSize)
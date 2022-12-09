import unittest
from Day6.index import part1,part2
from helpers import getInput

class TesDay6(unittest.TestCase):
  def test_list_part1_example1(self):
    self.assertEqual(part1("inputFiles/Day6/example_part1_1.txt"), 5)
  def test_list_part1_example2(self):
    self.assertEqual(part1("inputFiles/Day6/example_part1_2.txt"), 6)
  def test_list_part1_example3(self):
    self.assertEqual(part1("inputFiles/Day6/example_part1_3.txt"), 10)
  def test_list_part1_example4(self):
    self.assertEqual(part1("inputFiles/Day6/example_part1_4.txt"), 11)
  def test_list_part1_input(self):
    self.assertEqual(part1(getInput("Day6")), 1965)
  def test_list_part2_example1(self):
    self.assertEqual(part2("inputFiles/Day6/example_part2_1.txt"), 19)
  def test_list_part2_example2(self):
    self.assertEqual(part2("inputFiles/Day6/example_part2_2.txt"), 23)
  def test_list_part2_example3(self):
    self.assertEqual(part2("inputFiles/Day6/example_part2_3.txt"), 23)
  def test_list_part2_example4(self):
    self.assertEqual(part2("inputFiles/Day6/example_part2_4.txt"), 29)
  def test_list_part2_example5(self):
    self.assertEqual(part2("inputFiles/Day6/example_part2_5.txt"), 26)
  def test_list_part2_input(self):
    self.assertEqual(part2(getInput("Day6")), 2773)

if __name__ == '__main__':
  unittest.main()

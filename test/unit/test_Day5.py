import unittest
from Day5.index import part1,part2
from helpers import testing,getExample,getInput

class TesDay5(unittest.TestCase):
  def test_list_part1_example(self):
    self.assertEqual(testing(part1, getExample("Day5")), "CMZ")
  def test_list_part1_input(self):
    self.assertEqual(testing(part1, getInput("Day5")), "DHBJQJCCW")
  def test_list_part2_example(self):
    self.assertEqual(testing(part2, getExample("Day5")), "MCD")
  def test_list_part2_input(self):
    self.assertEqual(testing(part2, getInput("Day5")), "WJVRLSJJT")

if __name__ == '__main__':
  unittest.main()

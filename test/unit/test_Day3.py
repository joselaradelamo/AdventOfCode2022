import unittest
from Day3.index import part1,part2
from helpers import testing,getExample,getInput

class TesDay3(unittest.TestCase):
  def test_list_part1_example(self):
    self.assertEqual(testing(part1, getExample("Day3")), 157)
  def test_list_part1_input(self):
    self.assertEqual(testing(part1, getInput("Day3")), 7742)
  def test_list_part2_example(self):
    self.assertEqual(testing(part2, getExample("Day3")), 70)
  def test_list_part2_input(self):
    self.assertEqual(testing(part2, getInput("Day3")), 2276)

if __name__ == '__main__':
  unittest.main()
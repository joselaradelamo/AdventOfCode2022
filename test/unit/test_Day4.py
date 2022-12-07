import unittest
from Day4.index import part1,part2
from helpers import testing,getExample,getInput

class TesDay4(unittest.TestCase):
  def test_list_part1_example(self):
    self.assertEqual(testing(part1, getExample("Day4")), 2)
  def test_list_part1_input(self):
    self.assertEqual(testing(part1, getInput("Day4")), 605)
  def test_list_part2_example(self):
    self.assertEqual(testing(part2, getExample("Day4")), 4)
  def test_list_part2_input(self):
    self.assertEqual(testing(part2, getInput("Day4")), 914)

if __name__ == '__main__':
  unittest.main()

import unittest
from Day1.index import part1,part2
from helpers import getExample,getInput

class TesDay1(unittest.TestCase):
  def test_list_part1_example(self):
    self.assertEqual(part1(getExample("Day1")), 24000)
  def test_list_part1_input(self):
    self.assertEqual(part1(getInput("Day1")), 72240)
  def test_list_part2_example(self):
    self.assertEqual(part2(getExample("Day1")), 45000)
  def test_list_part2_input(self):
    self.assertEqual(part2(getInput("Day1")), 210957)

if __name__ == '__main__':
  unittest.main()

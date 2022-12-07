import unittest
from Day2.index import part1,part2
from helpers import testing,getExample,getInput

class TesDay2(unittest.TestCase):
  def test_list_part1_example(self):
    self.assertEqual(testing(part1, getExample("Day2")), 15)
  def test_list_part1_input(self):
    self.assertEqual(testing(part1, getInput("Day2")), 13221)
  def test_list_part2_example(self):
    self.assertEqual(testing(part2, getExample("Day2")), 12)
  def test_list_part2_input(self):
    self.assertEqual(testing(part2, getInput("Day2")), 13131)

if __name__ == '__main__':
  unittest.main()


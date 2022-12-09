import unittest
from Day8.index import part1,part2
from helpers import getExample,getInput

class TesDay8(unittest.TestCase):
  def test_list_part1_example(self):
    resExample = 21
    self.assertEqual(part1(getExample("Day8")), resExample)
  def test_list_part1_input(self):
    resInput = 1684
    self.assertEqual(part1(getInput("Day8")), resInput)
  def test_list_part2_example(self):
    resExample = 8
    self.assertEqual(part2(getExample("Day8")), resExample)
  def test_list_part2_input(self):
    resInput = 486540
    self.assertEqual(part2(getInput("Day8")), resInput)

if __name__ == '__main__':
  unittest.main()

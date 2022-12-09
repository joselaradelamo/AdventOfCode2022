import unittest
from Day7.index import part1,part2
from helpers import getExample,getInput

class TesDay7(unittest.TestCase):
  def test_list_part1_example(self):
    resExample = 95437
    self.assertEqual(part1(getExample("Day7")), resExample)
  def test_list_part1_input(self):
    resInput = 2031851
    self.assertEqual(part1(getInput("Day7")), resInput)
  def test_list_part2_example(self):
    resExample = 24933642
    self.assertEqual(part2(getExample("Day7")), resExample)
  def test_list_part2_input(self):
    resInput = 2568781
    self.assertEqual(part2(getInput("Day7")), resInput)

if __name__ == '__main__':
  unittest.main()

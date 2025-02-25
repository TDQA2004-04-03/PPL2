import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test_1(self):
        input = """var m int = arr[1][2];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,1001))



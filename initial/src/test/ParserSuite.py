import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_lower_identifier(self):
        input = """func main() {
            a := b.c.d;
        };\n"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1000))    
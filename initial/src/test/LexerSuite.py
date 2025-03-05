import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        input = """func main() {
            return;
        };\n"""
        expect = """"""
        self.assertTrue(TestLexer.checkLexeme(input, expect,1000))
    
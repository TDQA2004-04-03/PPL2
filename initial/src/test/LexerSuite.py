import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_1(self):
        input = """var abc int;"""
        expect = """var,abc,int,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 1))

    def test_2(self):
        input = """var x float;"""
        expect = """var,x,float,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 2))

    def test_3(self):
        input = """var y boolean;"""
        expect = """var,y,boolean,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 3))

    def test_4(self):
        input = """var str string;"""
        expect = """var,str,string,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 4))

    def test_5(self):
        input = """var check boolean = true;"""
        expect = """var,check,boolean,=,true,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 5))

    def test_6(self):
        input = """var val int = 2;"""
        expect = """var,val,int,=,2,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 6))

    def test_7(self):
        input = """var val int = 0b11011;"""
        expect = """var,val,int,=,0b11011,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 7))

    def test_8(self):
        input = """var m int = 0O7213;"""
        expect = """var,m,int,=,0O7213,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 8))

    def test_9(self):
        input = """var n int = 0XABCD1234;"""
        expect = """var,n,int,=,0XABCD1234,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 9))

    def test_10(self):
        input = """var e float = 2.78;"""
        expect = """var,e,float,=,2.78,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 10))

    def test_11(self):
        input = """var pi float = 3.14e1;"""
        expect = """var,pi,float,=,3.14e1,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 11))

    def test_12(self):
        input = """var c float = 1.;"""
        expect = """var,c,float,=,1.,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 12))

    def test_13(self):
        input = """var str string = "Hello";"""
        expect = """var,str,string,=,"Hello",;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 13))

    def test_14(self):
        input = """var year = 2025;"""
        expect = """var,year,=,2025,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 14))

    def test_15(self):
        input = """var manic = 6.11;"""
        expect = """var,manic,=,6.11,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 15))

    def test_16(self):
        input = """var stri = "This is a string";"""
        expect = """var,stri,=,"This is a string",;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 16))
    
    def test_17(self):
        input = """const YEAR = 1000;"""
        expect = """const,YEAR,=,1000,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 17))

    def test_18(self):
        input = """const VAL = 2.e-3;"""
        expect = """const,VAL,=,2.e-3,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 18))

    def test_19(self):
        input = """b := a;"""
        expect = """b,:=,a,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 19))

    def test_20(self):
        input = """add(1, 2);"""
        expect = """add,(,1,,,2,),;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 20))

    def test_21(self):
        input = """my_func(1, "Hello, World", true);"""
        expect = """my_func,(,1,,,"Hello, World",,,true,),;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 21))

    def test_22(self):
        input = """hello();"""
        expect = """hello,(,),;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 22))

    def test_23(self):
        input = """comp.mul(4,7);"""
        expect = """comp,.,mul,(,4,,,7,),;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 23))

    def test_24(self):
        input = """calc.reset();"""
        expect = """calc,.,reset,(,),;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 24))

    def test_25(self):
        input = """break;"""
        expect = """break,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 25))

    def test_26(self):
        input = """continue;"""
        expect = """continue,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 26))

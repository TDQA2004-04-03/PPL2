import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        input = """var x int;"""
        expect = str(Program([VarDecl("x",IntType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,1))

    def test_2(self):
        input = """var a float;"""
        expect = str(Program([VarDecl("a",FloatType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,2))

    def test_3(self):
        input = """var str string;"""
        expect = str(Program([VarDecl("str",StringType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,3))

    def test_4(self):
        input = """var turn boolean;"""
        expect = str(Program([VarDecl("turn",BoolType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,4))

    def test_5(self):
        input = """var p Person;"""
        expect = str(Program([VarDecl("p",Id("Person"),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,5))

    def test_6(self):
        input = """var arr [5][5]int;"""
        expect = str(Program([VarDecl("arr",ArrayType(eleType=IntType(),dimens=[IntLiteral(5),IntLiteral(5)]),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,6))

    def test_7(self):
        input = """var m [a]float;"""
        expect = str(Program([VarDecl("m",ArrayType(eleType=FloatType(),dimens=[Id("a")]),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,7))

    def test_8(self):
        input = """var a = 5;"""
        expect = str(Program([VarDecl("a",None,IntLiteral(5))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,8))

    def test_9(self):
        input = """var b = 0b1101;"""
        expect = str(Program([VarDecl("b",None,IntLiteral("0b1101"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,9))

    def test_10(self):
        input = """var c = 0O2357;"""
        expect = str(Program([VarDecl("c",None,IntLiteral("0O2357"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,10))

    def test_11(self):
        input = """var d int = 0xABCD2;"""
        expect = str(Program([VarDecl("d",IntType(),IntLiteral("0xABCD2"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,11))

    def test_12(self):
        input = """var x = 0.1;"""
        expect = str(Program([VarDecl("x",None,FloatLiteral(0.1))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,12))

    def test_13(self):
        input = """var y = 1.2e-2;"""
        expect = str(Program([VarDecl("y",None,FloatLiteral("1.2e-2"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,13))

    def test_14(self):
        input = """var z float = 2.e1;"""
        expect = str(Program([VarDecl("z",FloatType(),FloatLiteral("2.e1"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,14))

    def test_15(self):
        input = """var check = true;"""
        expect = str(Program([VarDecl("check",None,BooleanLiteral("true"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,15))

    def test_16(self):
        input = """var text string = "Hello";"""
        expect = str(Program([VarDecl("text",StringType(),StringLiteral("\"Hello\""))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,16))

    def test_17(self):
        input = """var m = 1 + 2;"""
        expect = str(Program([VarDecl("m",None,BinaryOp(op='+',left=IntLiteral(1),right=IntLiteral(2)))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,17))

    def test_18(self):
        input = """var n float = -6.2 - 3 * 2.5;"""
        expect = str(Program([VarDecl("n",FloatType(),BinaryOp(right=BinaryOp(op='*',left=IntLiteral(3),right=FloatLiteral(2.5)),op='-',left=UnaryOp(op='-',body=FloatLiteral(6.2))))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,18))

    def test_19(self):
        input = """var p = (1.52 + 3.2e1) / (67.e-1 - 2.5 * q) >= 3;"""
        expect = str(Program([VarDecl("p",None,BinaryOp(op='>=',left=BinaryOp('/',left=BinaryOp('+',left=FloatLiteral(1.52),right=FloatLiteral("3.2e1")),right=BinaryOp(op='-',left=FloatLiteral("67.e-1"),right=BinaryOp('*',left=FloatLiteral(2.5),right=Id("q")))),right=IntLiteral(3)))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,19))

    def test_20(self):
        input = """var check = !a && b || (m == n);"""
        expect = str(Program([VarDecl("check",None,BinaryOp(op='||',left=BinaryOp(op='&&',left=UnaryOp('!',Id("a")),right=Id("b")),right=BinaryOp(op='==',left=Id("m"),right=Id("n"))))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,20))

    def test_21(self):
        input = """const delta = b * b - 4 * a * c;"""
        expect = str(Program([ConstDecl("delta",None,BinaryOp(op='-',left=BinaryOp('*',Id("b"),Id("b")),right=BinaryOp('*',left=BinaryOp('*',left=IntLiteral(4),right=Id("a")),right=Id('c'))))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,21))

    def test_22(self):
        input = """var a = b[1];"""
        expect = str(Program([VarDecl("a",None,ArrayCell("b",[IntLiteral(1)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,22))

    def test_23(self):
        input = """var a = John.age;"""
        expect = str(Program([VarDecl("a",None,FieldAccess("John","age"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,23))

    def test_24(self):
        input = """var a = m[1][1];"""
        expect = str(Program([VarDecl("a",None,ArrayCell("m",[IntLiteral(1),IntLiteral(1)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,24))

    def test_25(self):
        input = """var lname = Mike.fullname.lastname;"""
        expect = str(Program([VarDecl("lname",None,FieldAccess(FieldAccess("Mike","fullname"),"lastname"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,25))

    def test_26(self):
        input = """var x = m[5].value;"""
        expect = str(Program([VarDecl("x",None,FieldAccess(ArrayCell("m",[IntLiteral(5)]),"value"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,26))

    def test_27(self):
        input = """var y = n.arr[2];"""
        expect = str(Program([VarDecl("y",None,ArrayCell(FieldAccess("n","arr"),[IntLiteral(2)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,27))

    def test_28(self):
        input = """var z = matrix.row[7].real;"""
        expect = str(Program([VarDecl("z",None,FieldAccess(ArrayCell(FieldAccess("matrix","row"),[IntLiteral(7)]),"real"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,28))

    def test_29(self):
        input = """var name = a[2][5].dec.mat;"""
        expect = str(Program([VarDecl("name",None,FieldAccess(FieldAccess(ArrayCell("a",[IntLiteral(2),IntLiteral(5)]),"dec"),"mat"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,29))

    def test_30(self):
        input = """var x = main();"""
        expect = str(Program([VarDecl("x",None,FuncCall("main",[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,30))

    def test_31(self):
        input = """var result int = Fibonacci(input);"""
        expect = str(Program([VarDecl("result",IntType(),FuncCall("Fibonacci",[Id("input")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,31))

    def test_32(self):
        input = """var f = Fibonacci(i - 1) + Fibonacci(i);"""
        expect = str(Program([VarDecl("f",None,BinaryOp(op='+',left=FuncCall("Fibonacci",[BinaryOp(op='-',left=Id("i"),right=IntLiteral(1))]),right=FuncCall("Fibonacci",[Id("i")])))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,32))

    def test_33(self):
        input = """var result = "Hello" + getText("dogma");"""
        expect = str(Program([VarDecl("result",None,BinaryOp(op='+',left=StringLiteral("\"Hello\""),right=FuncCall("getText",[StringLiteral("\"dogma\"")])))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,33))

    def test_34(self):
        input = """var result = calculator.calc(27 % 5);"""
        expect = str(Program([VarDecl("result",None,MethCall(receiver=Id("calculator"),metName="calc",args=[BinaryOp(op='%',left=IntLiteral(27),right=IntLiteral(5))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,34))

    def test_35(self):
        input = """var m = stu[5].avg(Math, Lit, Eng);"""
        expect = str(Program([VarDecl("m",None,MethCall(receiver=ArrayCell("stu",[IntLiteral(5)]),metName="avg",args=[Id("Math"),Id("Lit"),Id("Eng")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,35))

    def test_36(self):
        input = """var x [5]int;"""
        expect = str(Program([VarDecl("x",ArrayType(eleType=IntType(),dimens=[IntLiteral(5)]),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,36))

    def test_37(self):
        input = """var y [10][10]matrix;"""
        expect = str(Program([VarDecl("y",ArrayType(eleType=Id("matrix"),dimens=[IntLiteral(10),IntLiteral(10)]),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,37))

    def test_38(self):
        input = """var m = [2]int{4, 6};"""
        expect = str(Program([VarDecl("m",None,ArrayLiteral(dimens=[IntLiteral(2)],eleType=IntType(),value=[IntLiteral(4),IntLiteral(6)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,38))

    def test_39(self):
        input = """var names = [4]string{"John", "Mike", "Henry", "Edward"};"""
        expect = str(Program([VarDecl("names",None,ArrayLiteral(dimens=[IntLiteral(4)],eleType=StringType(),value=[StringLiteral("\"John\""),StringLiteral("\"Mike\""),StringLiteral("\"Henry\""),StringLiteral("\"Edward\"")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,39))

    def test_40(self):
        input = """var matrix = [2][2]float{{1.2, 3.4}, {5.6, 7.8}};"""
        expect = str(Program([VarDecl("matrix",None,ArrayLiteral([IntLiteral(2),IntLiteral(2)],FloatType(),[ArrayLiteral([],None,[FloatLiteral(1.2),FloatLiteral(3.4)]),ArrayLiteral([],None,[FloatLiteral(5.6),FloatLiteral(7.8)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,40))

    def test_41(self):
        input = """var lst = [2]int{a, b};"""
        expect = str(Program([VarDecl("lst",None,ArrayLiteral(dimens=[IntLiteral(2)],eleType=IntType(),value=[Id("a"),Id("b")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,41))

    def test_42(self):
        input = """var c = Complex{real: 5, imag: 2};"""
        expect = str(Program([VarDecl("c",None,StructLiteral(name="Complex",elements=[("real",IntLiteral(5)),("imag",IntLiteral(2))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,42))

    def test_43(self):
        input = """var p = Person{};"""
        expect = str(Program([VarDecl("p",None,StructLiteral(name="Person",elements=[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,43))

    def test_44(self):
        input = """var MT22KHT = Class{name: [4]string{"Bao","Anh","Tram","Tuan"}, number: 4};"""
        expect = str(Program([VarDecl("MT22KHT",None,StructLiteral(name="Class",elements=[("name",ArrayLiteral(dimens=[IntLiteral(4)],eleType=StringType(),value=[StringLiteral("\"Bao\""),StringLiteral("\"Anh\""),StringLiteral("\"Tram\""),StringLiteral("\"Tuan\"")])),("number",IntLiteral(4))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,44))

    def test_45(self):
        input = """type Calculator struct {
            value int;
        };"""
        expect = str(Program([StructType(name="Calculator",elements=[("value",IntType())],methods=[])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,45))

    def test_46(self):
        input = """type What struct {
            value int;
            names [10]string;
            check Now;
        };"""
        expect = str(Program([StructType(name="What",elements=[("value",IntType()),("names",ArrayType(eleType=StringType(),dimens=[IntLiteral(10)])),("check", Id("Now"))],methods=[])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,46))

    def test_47(self):
        input = """type Calculator interface {
            Add(x, y int) int;
        };"""
        expect = str(Program([InterfaceType(name="Calculator",methods=[Prototype(name="Add",params=[IntType(),IntType()],retType=IntType())])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,47))

    def test_48(self):
        input = """type Calculator interface {
            Add(x, y int) int;
            Div(x float, y int) float;
            Reset();
        };"""
        expect = str(Program([InterfaceType(name="Calculator",methods=[Prototype(name="Add",params=[IntType(),IntType()],retType=IntType()),Prototype(name="Div",params=[FloatType(),IntType()],retType=FloatType()),Prototype(name="Reset",params=[],retType=VoidType())])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,48))

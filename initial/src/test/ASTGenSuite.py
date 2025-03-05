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
        expect = str(Program([VarDecl("m",None,
            BinaryOp(op='+',left=IntLiteral(1),right=IntLiteral(2)))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,17))

    def test_18(self):
        input = """var n float = -6.2 - 3 * 2.5;"""
        expect = str(Program([VarDecl("n",FloatType(),
            BinaryOp(right=BinaryOp(op='*',left=IntLiteral(3),right=FloatLiteral(2.5)),
                     op='-',
                     left=UnaryOp(op='-',body=FloatLiteral(6.2))))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,18))

    def test_19(self):
        input = """var p = (1.52 + 3.2e1) / (67.e-1 - 2.5 * q) >= 3;"""
        expect = str(Program([VarDecl("p",None,
            BinaryOp(op='>=',
                left=BinaryOp('/',
                    left=BinaryOp('+',
                        left=FloatLiteral(1.52),
                        right=FloatLiteral("3.2e1")),
                    right=BinaryOp(op='-',
                        left=FloatLiteral("67.e-1"),
                        right=BinaryOp('*',
                            left=FloatLiteral(2.5),
                            right=Id("q")))),
                right=IntLiteral(3)))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,19))

    def test_20(self):
        input = """var check = !a && b || (m == n);"""
        expect = str(Program([VarDecl("check",None,
            BinaryOp(op='||',
                     left=BinaryOp(op='&&',
                        left=UnaryOp('!',Id("a")),
                        right=Id("b")),
                    right=BinaryOp(op='==',
                        left=Id("m"),
                        right=Id("n"))))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,20))

    def test_21(self):
        input = """const delta = b * b - 4 * a * c;"""
        expect = str(Program([ConstDecl("delta",None,
            BinaryOp(op='-',
                left=BinaryOp('*',Id("b"),Id("b")),
                right=BinaryOp('*',
                    left=BinaryOp('*',left=IntLiteral(4),right=Id("a")),
                    right=Id('c'))))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,21))

    def test_22(self):
        input = """var a = b[1];"""
        expect = str(Program([VarDecl("a",None,ArrayCell(Id("b"),[IntLiteral(1)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,22))

    def test_23(self):
        input = """var a = John.age;"""
        expect = str(Program([VarDecl("a",None,FieldAccess(Id("John"),"age"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,23))

    def test_24(self):
        input = """var a = m[1][1];"""
        expect = str(Program([VarDecl("a",None,ArrayCell(Id("m"),[IntLiteral(1),IntLiteral(1)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,24))

    def test_25(self):
        input = """var lname = Mike.fullname.lastname;"""
        expect = str(Program([VarDecl("lname",None,FieldAccess(FieldAccess(Id("Mike"),"fullname"),"lastname"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,25))

    def test_26(self):
        input = """var x = m[5].value;"""
        expect = str(Program([VarDecl("x",None,FieldAccess(ArrayCell(Id("m"),[IntLiteral(5)]),"value"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,26))

    def test_27(self):
        input = """var y = n.arr[2];"""
        expect = str(Program([VarDecl("y",None,ArrayCell(FieldAccess(Id("n"),"arr"),[IntLiteral(2)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,27))

    def test_28(self):
        input = """var z = matrix.row[7].real;"""
        expect = str(Program([VarDecl("z",None,FieldAccess(ArrayCell(FieldAccess(Id("matrix"),"row"),[IntLiteral(7)]),"real"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,28))

    def test_29(self):
        input = """var name = a[2][5].dec.mat;"""
        expect = str(Program([VarDecl("name",None,FieldAccess(FieldAccess(ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(5)]),"dec"),"mat"))]))
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
        expect = str(Program([VarDecl("f",None,
            BinaryOp(op='+',
                left=FuncCall("Fibonacci",[BinaryOp(op='-',left=Id("i"),right=IntLiteral(1))]),
                right=FuncCall("Fibonacci",[Id("i")])))]))
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
        expect = str(Program([VarDecl("m",None,MethCall(receiver=ArrayCell(Id("stu"),[IntLiteral(5)]),metName="avg",args=[Id("Math"),Id("Lit"),Id("Eng")]))]))
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
        expect = str(Program([StructType(name="What",elements=[
            ("value",IntType()),
            ("names",ArrayType(eleType=StringType(),dimens=[IntLiteral(10)])),
            ("check", Id("Now"))],
            methods=[])]))
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
        expect = str(Program([InterfaceType(name="Calculator",methods=[
            Prototype(name="Add",params=[IntType(),IntType()],retType=IntType()),
            Prototype(name="Div",params=[FloatType(),IntType()],retType=FloatType()),
            Prototype(name="Reset",params=[],retType=VoidType())])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,48))

    def test_49(self):
        input = """var lst = [2]Complex{Complex{real: 2, imag: 3},Complex{real:1, imag:4}};"""
        expect = str(Program([VarDecl("lst",None,ArrayLiteral([IntLiteral(2)],Id("Complex"),[
            StructLiteral("Complex",elements=[("real",IntLiteral(2)),("imag",IntLiteral(3))]),
            StructLiteral("Complex",elements=[("real",IntLiteral(1)),("imag",IntLiteral(4))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,49))

    def test_50(self):
        input = """var stru = Strut{arr1: [2]int{1,2}, arr2: [2]float{1.0, 2.0}};"""
        expect = str(Program([VarDecl("stru",None,StructLiteral(name="Strut",elements=[
            ("arr1",ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])),
            ("arr2",ArrayLiteral([IntLiteral(2)],FloatType(),[FloatLiteral(1.0),FloatLiteral(2.0)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,50))

    def test_51(self):
        input = """func main() {
            var x int;
        };"""
        expect = str(Program([FuncDecl(name="main",params=[],retType=VoidType(),body=Block([VarDecl("x",IntType(),None)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,51))

    def test_52(self):
        input = """func main() {
            break;
        };"""
        expect = str(Program([FuncDecl(name="main",params=[],retType=VoidType(),body=Block([Break()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,52))

    def test_53(self):
        input = """func main() {
            continue;
        };"""
        expect = str(Program([FuncDecl(name="main",params=[],retType=VoidType(),body=Block([Continue()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,53))

    def test_54(self):
        input = """func area_square(a float) float {
            return a * a;
        };"""
        expect = str(Program([FuncDecl(name="area_square",params=[ParamDecl("a", FloatType())],retType=FloatType(),
            body=Block([Return(BinaryOp(left=Id("a"),op='*',right=Id("a")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,54))

    def test_55(self):
        input = """func foo(a, b float) float {
            var result float = a * b;
            return result;
        };"""
        expect = str(Program([FuncDecl(name="foo",params=[ParamDecl("a",FloatType()),ParamDecl("b",FloatType())],retType=FloatType(),body=Block([
            VarDecl("result",FloatType(),BinaryOp(left=Id("a"),op='*',right=Id("b"))),
            Return(Id("result"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,55))

    def test_56(self):
        input = """func foo(a int) int {
            a := a + 1;
            return a;
        };"""
        expect = str(Program([FuncDecl(name="foo",params=[ParamDecl("a",IntType())],retType=IntType(),body=Block([
            Assign(Id("a"),BinaryOp(left=Id("a"),op='+',right=IntLiteral(1))),
            Return(Id("a"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,56))

    def test_57(self):
        input = """func foo(a int) int {
            a *= 2;
            do_something();
            return a;
        };"""
        expect = str(Program([FuncDecl(name="foo",params=[ParamDecl("a",IntType())],retType=IntType(),body=Block([
            Assign(Id("a"),BinaryOp(left=Id("a"),op='*',right=IntLiteral(2))),
            FuncCall("do_something",[]),
            Return(Id("a"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,57))

    def test_58(self):
        input = """func foo(a int) int {
            if (a > 5) {
                return 1;
            };
        };"""
        expect = str(Program([FuncDecl(name="foo",params=[ParamDecl("a",IntType())],retType=IntType(),body=Block([If(BinaryOp(op='>',left=Id("a"),right=IntLiteral(5)),Block([Return(IntLiteral(1))]),None)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,58))

    def test_59(self):
        input = """func foo(a int) int {
            if (a > 5) {
                return 1;
            } else {
                return 0;
            };
        };"""
        expect = str(Program([FuncDecl(name="foo",params=[ParamDecl("a",IntType())],retType=IntType(),body=Block([
            If(BinaryOp(op='>',left=Id("a"),right=IntLiteral(5)),
               Block([Return(IntLiteral(1))]),
               Block([Return(IntLiteral(0))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,59))

    def test_60(self):
        input = """func foo(a int) int {
            if (a > 5) {
                return 1;
            } else if (a > 0) {
                return 0;
            } else {
                return -1;
            };
        };"""
        expect = str(Program([FuncDecl(name="foo",params=[ParamDecl("a",IntType())],retType=IntType(),body=Block([
            If(BinaryOp(op='>',left=Id("a"),right=IntLiteral(5)),
               Block([Return(IntLiteral(1))]),
               If(BinaryOp(op='>',left=Id("a"),right=IntLiteral(0)),
                  Block([Return(IntLiteral(0))]),
                  Block([Return(UnaryOp(op='-',body=IntLiteral(1)))])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,60))

    def test_61(self):
        input = """func main() int {
            a := 0;
            S := 0;
            for a < 10 {
                a += 1;
                S += a;
            };
        };"""
        expect = str(Program([FuncDecl(name="main",params=[],retType=IntType(),body=Block([
            Assign(Id("a"),IntLiteral(0)),
            Assign(Id("S"),IntLiteral(0)),
            ForBasic(BinaryOp(op='<',left=Id("a"),right=IntLiteral(10)),Block([
                Assign(Id("a"),BinaryOp(left=Id("a"),op='+',right=IntLiteral(1))),
                Assign(Id("S"),BinaryOp(left=Id("S"),op='+',right=Id("a")))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,61))

    def test_62(self):
        input = """func main() int {
            S := 0;
            for a := 0; a < 20; a += 2 {
                S += a;
            };
        };
        """
        expect = str(Program([FuncDecl(name="main",params=[],retType=IntType(),
            body=Block([Assign(Id("S"),IntLiteral(0)),
                        ForStep(Assign(Id("a"),IntLiteral(0)),
                                BinaryOp(op='<',left=Id("a"),right=IntLiteral(20)),
                                Assign(Id("a"),BinaryOp(left=Id("a"),op='+',right=IntLiteral(2))),
                            Block([Assign(Id("S"),BinaryOp(left=Id("S"),op='+',right=Id("a")))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,62))

    def test_63(self):
        input = """func main() {
            for index, value := range array {
                continue;
            };
        };
        """
        expect = str(Program([FuncDecl(name="main",params=[],retType=VoidType(),body=Block([ForEach(idx=Id("index"),value=Id("value"),arr=Id("array"),loop=Block([Continue()]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,63))

    def test_64(self):
        input = """func (p Person) Greet() {
            putStringLn("Hello");
        };"""
        expect = str(Program([MethodDecl(receiver="p",recType=Id("Person"),fun=FuncDecl(name="Greet",params=[],retType=VoidType(),body=Block([FuncCall("putStringLn",[StringLiteral("\"Hello\"")])])))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,64))

    def test_65(self):
        input = """
        func main() {
            if (delta > 0) {
                putIntLn(2);
            } else if (delta == 0) {
                putIntLn(1);
            } else {
                putIntLn(0);
            };
        };"""
        expect = str(Program([FuncDecl(name="main",params=[],retType=VoidType(),body=Block([
            If(BinaryOp(op='>',left=Id("delta"),right=IntLiteral(0)),
               Block([FuncCall("putIntLn",[IntLiteral(2)])]),
               If(BinaryOp(op='==',left=Id("delta"),right=IntLiteral(0)),
                  Block([FuncCall("putIntLn",[IntLiteral(1)])]),
                  Block([FuncCall("putIntLn",[IntLiteral(0)])])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,65))

    def test_66(self):
        input = """
        func main() {
            for var i int = 0; i <= 100; i += 1 {
                S += i % 29;
            }
        };"""
        expect = str(Program([FuncDecl(name="main",params=[],retType=VoidType(),body=Block([
            ForStep(init=VarDecl("i",IntType(),IntLiteral(0)),
                    cond=BinaryOp(op="<=",left=Id("i"),right=IntLiteral(100)),
                    upda=Assign(lhs=Id("i"),rhs=BinaryOp(op='+',left=Id("i"),right=IntLiteral(1))),
                    loop=Block([Assign(lhs=Id("S"),rhs=BinaryOp(op='+',left=Id("S"),right=BinaryOp(op='%',left=Id("i"),right=IntLiteral(29))))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,66))

    def test_67(self):
        input = """var arr = [x]int {5, 7, 9, a, b};"""
        expect = str(Program([VarDecl("arr",None,ArrayLiteral(dimens=[Id("x")],eleType=IntType(),value=[IntLiteral(5),IntLiteral(7),IntLiteral(9),Id("a"),Id("b")]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,67))

    def test_68(self):
        input = """var q float = c + (2 * a * a * a - 9 * a * b) / 27;"""
        expect = str(Program([VarDecl("q",FloatType(),
            BinaryOp(op='+',
                     left=Id("c"),
                     right=BinaryOp(op='/',
                                    left=BinaryOp(op='-',
                                                  left=BinaryOp(op='*',
                                                                left=BinaryOp(op='*',
                                                                              left=BinaryOp(op='*',left=IntLiteral(2),right=Id("a")),
                                                                              right=Id("a")),
                                                                right=Id("a")),
                                                   right=BinaryOp(op='*',
                                                                  left=BinaryOp(op='*',
                                                                                left=IntLiteral(9),
                                                                                right=Id("a")),
                                                                  right=Id("b"))),
                                    right=IntLiteral(27))))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,68))

    def test_69(self):
        input = """var str string = "Elimination\tChamber";"""
        expect = str(Program([VarDecl("str",StringType(),StringLiteral("\"Elimination\tChamber\""))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,69))

    def test_70(self):
        input = """type Person struct {
            name string;
            age int;
        };"""
        expect = str(Program([StructType("Person",elements=[
            ("name",StringType()),
            ("age",IntType())],
            methods=[])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,70))

    def test_71(self):
        input = """var x = foo()[5];"""
        expect = str(Program([VarDecl("x",None,ArrayCell(FuncCall("foo",[]),[IntLiteral(5)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,71))

    def test_72(self):
        input = """var y = foo().value;"""
        expect = str(Program([VarDecl("y",None,FieldAccess(FuncCall("foo",[]),"value"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,72))

    def test_73(self):
        input = """var z = calculator.calc().value[0];"""
        expect = str(Program([VarDecl("z",None,ArrayCell(FieldAccess(MethCall(Id("calculator"),"calc",[]),"value"),[IntLiteral(0)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,73))

    def test_74(self):
        input = """func Fibonacci(n int) int {
            if (n == 1 || n == 2) {
                return 1;
            };
            return Fibonacci(n - 1) + Fibonacci(n - 2);
        };"""
        expect = str(Program([FuncDecl("Fibonacci",[ParamDecl("n",IntType())],IntType(),Block([
            If(BinaryOp("||",
                        BinaryOp("==",Id("n"),IntLiteral(1)),
                        BinaryOp("==",Id("n"),IntLiteral(2))),
               Block([Return(IntLiteral(1))]),None),
               Return(BinaryOp("+",FuncCall("Fibonacci",[BinaryOp("-",Id("n"),IntLiteral(1))]),FuncCall("Fibonacci",[BinaryOp("-",Id("n"),IntLiteral(2))])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,74))

    def test_75(self):
        input = """
            var arr = [2]Person {Person{name: "John", age: 20}, Person{name: "Mike", age: 21}};
            func main() {
                for _, value := range arr {
                    putIntLn(value.name);
            };
        };"""
        expect = str(Program([
            VarDecl("arr",None,ArrayLiteral([IntLiteral(2)],Id("Person"),[StructLiteral("Person",[("name",StringLiteral("\"John\"")),("age",IntLiteral(20))]),StructLiteral("Person",[("name",StringLiteral("\"Mike\"")),("age",IntLiteral(21))])])),
            FuncDecl("main",[],VoidType(),Block([
                ForEach(idx=None,value=Id("value"),arr=Id("arr"),loop=Block([
                    FuncCall("putIntLn",[FieldAccess(Id("value"),"name")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,75))

    def test_76(self):
        input = """var str boolean = "Hello" > "World" + " Life\";"""
        expect = str(Program([VarDecl("str",BoolType(),
            BinaryOp(">",StringLiteral("\"Hello\""),
                BinaryOp("+",StringLiteral("\"World\""),StringLiteral("\" Life\""))))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,76))

    def test_77(self):
        input = """const value = !(a[5] * -24 - 16) && b.now || c > -19 && !(c == 5);"""
        expect = str(Program([ConstDecl("value",None,
            BinaryOp(op="||",
                     left=BinaryOp(op='&&',
                                   left=UnaryOp(op='!',
                                                body=BinaryOp(op='-',
                                                              left=BinaryOp(op='*',left=ArrayCell(Id("a"),[IntLiteral(5)]),right=UnaryOp(op='-',body=IntLiteral(24))),
                                                              right=IntLiteral(16))),
                                   right=FieldAccess(Id("b"),"now")),
                    right=BinaryOp(op='&&',
                                   left=BinaryOp(op='>',left=Id("c"),right=UnaryOp(op='-',body=IntLiteral(19))),
                                   right=UnaryOp(op='!', body=BinaryOp(op='==',left=Id("c"),right=IntLiteral(5))))))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,77))
    
    def test_78(self):
        input = """var KHT = Class{list: [2] string {"Mike", "Johnson"}, location: Location{country: "USA", state: "Oregon"}};"""
        expect = str(Program([VarDecl("KHT",None,
                                      StructLiteral("Class",[
                                          ("list",ArrayLiteral([IntLiteral(2)],StringType(),[StringLiteral("\"Mike\""),StringLiteral("\"Johnson\"")])),
                                          ("location",StructLiteral("Location",[("country",StringLiteral("\"USA\"")),("state",StringLiteral("\"Oregon\""))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,78))

    def test_79(self):
        input = """func main() {
            putStringLn(dude.hello[2][3].name);
        };"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([
            FuncCall("putStringLn",[FieldAccess(ArrayCell(FieldAccess(Id("dude"),"hello"),[IntLiteral(2),IntLiteral(3)]),"name")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,79))

    def test_80(self):
        input = """func main() {
            if (a > b) {
                putIntLn(a);
            } else {
                if (a == b) {
                    putIntLn("Equal");
                };
                putIntLn(b);
            }
        };"""
        expect = str(Program([FuncDecl("main",[],VoidType(),
            Block([If(BinaryOp(">",Id("a"),Id("b")),
                      Block([FuncCall("putIntLn",[Id("a")])]),
                      Block([If(BinaryOp("==",Id("a"),Id("b")),
                                Block([FuncCall("putIntLn",[StringLiteral("\"Equal\"")])]),None),
                            FuncCall("putIntLn",[Id("b")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,80))

    def test_80(self):
        input = """func check(result float) string {
            if (result > 4.) {
                return "A";
            } else if (result > 3.) {
                return "B";
            } else if (result > 2.) {
                return "C";
            } else {
                return "F";
            }
        };"""
        expect = str(Program([FuncDecl("check",[ParamDecl("result",FloatType())],StringType(),Block([
            If(expr=BinaryOp(op='>',left=Id("result"),right=FloatLiteral("4.")),
               thenStmt=Block([Return(StringLiteral("\"A\""))]),
               elseStmt=If(expr=BinaryOp(op='>',left=Id("result"),right=FloatLiteral("3.")),
                            thenStmt=Block([Return(StringLiteral("\"B\""))]),
                            elseStmt=If(expr=BinaryOp(op='>',left=Id("result"),right=FloatLiteral("2.")),
                                        thenStmt=Block([Return(StringLiteral("\"C\""))]),
                                        elseStmt=Block([Return(StringLiteral("\"F\""))]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,80))

    def test_81(self):
        input = """var val int = Mike.name.fname.fletter.ascii.dopamine;"""
        expect = str(Program([VarDecl("val",IntType(),FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("Mike"),"name"),"fname"),"fletter"),"ascii"),"dopamine"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,81))

    def test_82(self):
        input = """func main() {
            x := matrix[1][2][3][4][5];
            y := matrix[5][4][3][2][1];
            putIntLn(x + y);
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([
            Assign(Id("x"),ArrayCell(Id("matrix"),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])),
            Assign(Id("y"),ArrayCell(Id("matrix"),[IntLiteral(5),IntLiteral(4),IntLiteral(3),IntLiteral(2),IntLiteral(1)])),
            FuncCall("putIntLn",[BinaryOp(op='+',left=Id("x"),right=Id("y"))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,82))

    def test_83(self):
        input = """const x = night[1][2][3][4].dork.node[5][6][7][8].rightnow.forever;"""
        expect = str(Program([ConstDecl("x",None,FieldAccess(FieldAccess(ArrayCell(FieldAccess(FieldAccess(ArrayCell(Id("night"),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]),"dork"),"node"),[IntLiteral(5),IntLiteral(6),IntLiteral(7),IntLiteral(8)]),"rightnow"),"forever"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,83))

    def test_84(self):
        input = """var S float = 0.e-1;
        func main() {
            for _, value := range arr {
                for _, elem := range value {
                    if (elem != 0) {
                        S *= elem;
                    } else {
                        S += 1.0e0;
                    };
                };
            };
        };"""
        expect = str(Program([
            VarDecl("S",FloatType(),FloatLiteral("0.e-1")),
            FuncDecl("main",[],VoidType(),Block(
                [ForEach(idx=None,value=Id("value"),arr=Id("arr"),
                        loop=Block([ForEach(idx=None,value=Id("elem"),arr=Id("value"),
                            loop=Block([
                                If(BinaryOp("!=",Id("elem"),IntLiteral(0)),
                                   Block([Assign(Id("S"),BinaryOp(op="*",left=Id("S"),right=Id("elem")))]),
                                   Block([Assign(Id("S"),BinaryOp(op='+',left=Id("S"),right=FloatLiteral("1.0e0")))]))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,84))

    def test_85(self):
        input = """var x float = 0b10 * 0.314e+1 - 0O3 / 27.8e-1 + AI % 4;"""
        expect = str(Program([VarDecl("x",FloatType(),
            BinaryOp(op = '+',
                left=BinaryOp(op='-',
                    left=BinaryOp(op='*',left=IntLiteral("0b10"),right=FloatLiteral("0.314e+1")),
                    right=BinaryOp(op='/',left=IntLiteral("0O3"),right=FloatLiteral("27.8e-1"))),
                right=BinaryOp(op='%',left=Id("AI"),right=IntLiteral("4"))))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,85))

    def test_86(self):
        input = """var x boolean = (true || false) && !a || b;"""
        expect = str(Program([VarDecl("x",BoolType(),
            BinaryOp(op='||',
                left=BinaryOp(op='&&',
                    left=BinaryOp(op='||',left=BooleanLiteral("true"),right=BooleanLiteral("false")),
                    right=UnaryOp(op='!',body=Id("a"))),
                right=Id("b")))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,86))

    def test_87(self):
        input = """type Student interface{
            Read(b Book, t Time) Conclusion;
            Study(s Subject) string;
            Speak() string;
            Sleep();
        };"""
        expect = str(Program([InterfaceType("Student",[
            Prototype("Read",[Id("Book"),Id("Time")],Id("Conclusion")),
            Prototype("Study",[Id("Subject")],StringType()),
            Prototype("Speak",[],StringType()),
            Prototype("Sleep",[],VoidType())])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,87))

    def test_88(self):
        input = """
        func (m Matrix) Add(n Matrix) Matrix {
            for i := 0; i < len(m); i += 1 {
                for j := 0; j < len(m[0]); j += 1 {
                    m[i][j] += n[i][j];
                };
            };
        }
        """
        expect = str(Program([MethodDecl("m",Id("Matrix"),FuncDecl("Add",[ParamDecl("n",Id("Matrix"))],Id("Matrix"),
            Block([
                ForStep(init=Assign(Id("i"),IntLiteral(0)),
                        cond=BinaryOp(op="<",left=Id("i"),right=FuncCall("len",[Id("m")])),
                        upda=Assign(Id("i"),BinaryOp(op='+',left=Id("i"),right=IntLiteral(1))),
                        loop=Block([
                            ForStep(init=Assign(Id("j"),IntLiteral(0)),
                                    cond=BinaryOp(op='<',left=Id("j"),right=FuncCall("len",[ArrayCell(Id("m"),[IntLiteral(0)])])),
                                    upda=Assign(Id("j"),BinaryOp(op='+',left=Id("j"),right=IntLiteral(1))),
                                    loop=Block([
                                        Assign(ArrayCell(Id("m"),[Id("i"),Id("j")]),
                                               BinaryOp(op='+',left=ArrayCell(Id("m"),[Id("i"),Id("j")]),right=ArrayCell(Id("n"),[Id("i"),Id("j")])))
                                    ])
                            )
                        ])
                    )
            ])))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,88))

    def test_89(self):
        input = """var str = "Hello\\r" + "\\\\Life";"""
        expect = str(Program([VarDecl("str",None,BinaryOp(op='+',left=StringLiteral("\"Hello\\r\""),right=StringLiteral("\"\\\\Life\"")))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,89))

    def test_90(self):
        input = """var str1 string = "The USA is a stupid country\\n";
        var str2 string =  "How the hell did they manage to elect DONALD TRUMP again?\"
        var str = str1 + str2;
        func main() {
            if (str1 > str2) {
                putStringLn(str);
            } else {
                putStringLn(str1);
            };
        };"""
        expect = str(Program([
            VarDecl("str1",StringType(),StringLiteral("\"The USA is a stupid country\\n\"")),
            VarDecl("str2",StringType(),StringLiteral("\"How the hell did they manage to elect DONALD TRUMP again?\"")),
            VarDecl("str",None,BinaryOp(op='+',left=Id("str1"),right=Id("str2"))),
            FuncDecl("main",[],VoidType(),Block([
                If(BinaryOp('>',Id("str1"),Id("str2")),
                   Block([FuncCall("putStringLn",[Id("str")])]),
                   Block([FuncCall("putStringLn",[Id("str1")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,90))

    def test_91(self):
        input = """var arr1 = [5]string {"Tanjirou", "Zenitsu", "Inosuke", "Genya", "Kanao"};
        var arr2 = [9]string {"Mitsuri", "Muichirou", "Gyomei", "Sanemi", "Shinobu", "Kanae", "Tengen", "Kokushibou", "Yoriichi"};
        var arr = arr1 + arr2;"""
        expect = str(Program([
            VarDecl("arr1",None,ArrayLiteral([IntLiteral(5)],StringType(),[StringLiteral("\"Tanjirou\""),StringLiteral("\"Zenitsu\""),StringLiteral("\"Inosuke\""),StringLiteral("\"Genya\""),StringLiteral("\"Kanao\"")])),
            VarDecl("arr2",None,ArrayLiteral([IntLiteral(9)],StringType(),[StringLiteral("\"Mitsuri\""),StringLiteral("\"Muichirou\""),StringLiteral("\"Gyomei\""),StringLiteral("\"Sanemi\""),StringLiteral("\"Shinobu\""),StringLiteral("\"Kanae\""),StringLiteral("\"Tengen\""),StringLiteral("\"Kokushibou\""),StringLiteral("\"Yoriichi\"")])),
            VarDecl("arr",None,BinaryOp(op='+',left=Id("arr1"),right=Id("arr2")))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,91))

    def test_92(self):
        input = """var res = !a[b] && (c + d) || e.f.g * 0x36A5;"""
        expect = str(Program([VarDecl("res",None,
            BinaryOp(op='||',
                     left=BinaryOp(op='&&',
                                   left=UnaryOp(op='!',
                                                body=ArrayCell(Id("a"),[Id("b")])),
                                    right=BinaryOp(op='+',left=Id("c"),right=Id("d"))),
                     right=BinaryOp(op='*',
                                    left=FieldAccess(FieldAccess(Id("e"),"f"),"g"),
                                    right=IntLiteral("0x36A5"))))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,92))

    def test_93(self):
        input = """func main() {
            a := true;
            for a {
                a := false;
                putStringLn("Stop the loop");
                break;
            };
        };"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([
            Assign(Id("a"),BooleanLiteral("true")),
            ForBasic(Id("a"),Block([
                Assign(Id("a"),BooleanLiteral("false")),
                FuncCall("putStringLn",[StringLiteral("\"Stop the loop\"")]),
                Break()
            ]))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,93))

    def test_94(self):
        input = """var arr = [3][3]int{{1,4,9}, {16,25,36}, {49,64,81}};
        func main() {
            x := arr[0][1] + arr[1][2] + arr[2][3]
        };"""
        expect = str(Program([
            VarDecl("arr",None,ArrayLiteral([IntLiteral(3),IntLiteral(3)],IntType(),[
                ArrayLiteral([],None,[IntLiteral(1),IntLiteral(4),IntLiteral(9)]),
                ArrayLiteral([],None,[IntLiteral(16),IntLiteral(25),IntLiteral(36)]),
                ArrayLiteral([],None,[IntLiteral(49),IntLiteral(64),IntLiteral(81)])
            ])),
            FuncDecl("main",[],VoidType(),Block([
                Assign(Id("x"),BinaryOp(op='+',
                                        left=BinaryOp(op='+',
                                                      left=ArrayCell(Id("arr"),[IntLiteral(0),IntLiteral(1)]),
                                                      right=ArrayCell(Id("arr"),[IntLiteral(1),IntLiteral(2)])),
                                        right=ArrayCell(Id("arr"),[IntLiteral(2),IntLiteral(3)])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,94))

    def test_95(self):
        input = """func main() {
            var x int = 0;
            for x < 10 {
                x += 1;
                if (x % 2 == 0) {
                    continue;
                };
                putIntLn(x);
            };
        };
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([
            VarDecl("x",IntType(),IntLiteral(0)),
            ForBasic(cond=BinaryOp(op='<',left=Id("x"),right=IntLiteral(10)),
                     loop=Block([
                         Assign(Id("x"),BinaryOp(op='+',left=Id("x"),right=IntLiteral(1))),
                         If(BinaryOp(op='==',left=BinaryOp(op='%',left=Id("x"),right=IntLiteral(2)),right=IntLiteral(0)),
                            Block([Continue()]),
                            None),
                        FuncCall("putIntLn",[Id("x")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,95))

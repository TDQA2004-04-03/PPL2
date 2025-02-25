# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u01ee\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3")
        buf.write("\5\3\5\6\5\u0087\n\5\r\5\16\5\u0088\3\6\3\6\3\6\6\6\u008e")
        buf.write("\n\6\r\6\16\6\u008f\3\7\3\7\3\7\6\7\u0095\n\7\r\7\16\7")
        buf.write("\u0096\3\b\3\b\3\b\7\b\u009c\n\b\f\b\16\b\u009f\13\b\5")
        buf.write("\b\u00a1\n\b\3\t\3\t\3\t\3\t\5\t\u00a7\n\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\5\n\u00be\n\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\7\13\u00c6\n\13\f\13\16\13\u00c9\13\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\7\f\u00d1\n\f\f\f\16\f\u00d4\13\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33")
        buf.write("\u0145\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\5\34\u0151\n\34\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\7\36\u015b\n\36\f\36\16\36\u015e\13\36\3\36")
        buf.write("\3\36\7\36\u0162\n\36\f\36\16\36\u0165\13\36\3\36\3\36")
        buf.write("\5\36\u0169\n\36\3\36\7\36\u016c\n\36\f\36\16\36\u016f")
        buf.write("\13\36\5\36\u0171\n\36\3\37\3\37\3\37\3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \5 \u0180\n \3!\3!\3!\3\"\3\"\3\"\3#\3#\3")
        buf.write("$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3+\3")
        buf.write(",\3,\3,\3-\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u01b1\n\61\3")
        buf.write("\62\3\62\7\62\u01b5\n\62\f\62\16\62\u01b8\13\62\3\63\3")
        buf.write("\63\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67")
        buf.write("\38\38\38\58\u01c9\n8\39\39\39\79\u01ce\n9\f9\169\u01d1")
        buf.write("\139\39\39\3:\6:\u01d6\n:\r:\16:\u01d7\3:\3:\3;\3;\3;")
        buf.write("\3<\3<\3<\3<\3<\3<\3=\3=\3=\3=\5=\u01e9\n=\3=\3=\3>\3")
        buf.write(">\2\2?\3\3\5\4\7\5\t\2\13\2\r\2\17\2\21\6\23\7\25\b\27")
        buf.write("\t\31\n\33\13\35\f\37\r!\16#\17%\20\'\21)\22+\23-\24/")
        buf.write("\25\61\26\63\27\65\30\67\319\32;\33=\34?\35A\36C\37E ")
        buf.write("G!I\"K#M$O%Q&S\'U(W)Y*[+],_-a.c\2e/g\2i\2k\2m\2o\2q\60")
        buf.write("s\61u\62w\63y\64{\65\3\2\21\4\2DDdd\3\2\62\63\4\2QQqq")
        buf.write("\3\2\629\4\2ZZzz\5\2\62;CHch\4\2\f\f\17\17\4\2GGgg\4\2")
        buf.write("--//\4\2$$^^\3\2C\\\3\2c|\3\2\62;\3\2\63;\5\2\13\13\17")
        buf.write("\17\"\"\2\u020b\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2e\3\2\2")
        buf.write("\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2")
        buf.write("\2\2\2{\3\2\2\2\3}\3\2\2\2\5\177\3\2\2\2\7\u0081\3\2\2")
        buf.write("\2\t\u0083\3\2\2\2\13\u008a\3\2\2\2\r\u0091\3\2\2\2\17")
        buf.write("\u00a0\3\2\2\2\21\u00a6\3\2\2\2\23\u00bd\3\2\2\2\25\u00c1")
        buf.write("\3\2\2\2\27\u00cc\3\2\2\2\31\u00da\3\2\2\2\33\u00de\3")
        buf.write("\2\2\2\35\u00e4\3\2\2\2\37\u00ec\3\2\2\2!\u00f1\3\2\2")
        buf.write("\2#\u00fa\3\2\2\2%\u0104\3\2\2\2\'\u0109\3\2\2\2)\u0112")
        buf.write("\3\2\2\2+\u0117\3\2\2\2-\u011c\3\2\2\2/\u0122\3\2\2\2")
        buf.write("\61\u0128\3\2\2\2\63\u0130\3\2\2\2\65\u0144\3\2\2\2\67")
        buf.write("\u0150\3\2\2\29\u0154\3\2\2\2;\u015c\3\2\2\2=\u0172\3")
        buf.write("\2\2\2?\u017f\3\2\2\2A\u0181\3\2\2\2C\u0184\3\2\2\2E\u0187")
        buf.write("\3\2\2\2G\u0189\3\2\2\2I\u018b\3\2\2\2K\u018d\3\2\2\2")
        buf.write("M\u018f\3\2\2\2O\u0191\3\2\2\2Q\u0193\3\2\2\2S\u0195\3")
        buf.write("\2\2\2U\u0197\3\2\2\2W\u019a\3\2\2\2Y\u019d\3\2\2\2[\u01a0")
        buf.write("\3\2\2\2]\u01a2\3\2\2\2_\u01a4\3\2\2\2a\u01b0\3\2\2\2")
        buf.write("c\u01b6\3\2\2\2e\u01b9\3\2\2\2g\u01bd\3\2\2\2i\u01bf\3")
        buf.write("\2\2\2k\u01c1\3\2\2\2m\u01c3\3\2\2\2o\u01c8\3\2\2\2q\u01ca")
        buf.write("\3\2\2\2s\u01d5\3\2\2\2u\u01db\3\2\2\2w\u01de\3\2\2\2")
        buf.write("y\u01e4\3\2\2\2{\u01ec\3\2\2\2}~\7<\2\2~\4\3\2\2\2\177")
        buf.write("\u0080\7\60\2\2\u0080\6\3\2\2\2\u0081\u0082\7a\2\2\u0082")
        buf.write("\b\3\2\2\2\u0083\u0084\7\62\2\2\u0084\u0086\t\2\2\2\u0085")
        buf.write("\u0087\t\3\2\2\u0086\u0085\3\2\2\2\u0087\u0088\3\2\2\2")
        buf.write("\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\n\3\2\2")
        buf.write("\2\u008a\u008b\7\62\2\2\u008b\u008d\t\4\2\2\u008c\u008e")
        buf.write("\t\5\2\2\u008d\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f")
        buf.write("\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\f\3\2\2\2\u0091")
        buf.write("\u0092\7\62\2\2\u0092\u0094\t\6\2\2\u0093\u0095\t\7\2")
        buf.write("\2\u0094\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0094")
        buf.write("\3\2\2\2\u0096\u0097\3\2\2\2\u0097\16\3\2\2\2\u0098\u00a1")
        buf.write("\7\62\2\2\u0099\u009d\5m\67\2\u009a\u009c\5k\66\2\u009b")
        buf.write("\u009a\3\2\2\2\u009c\u009f\3\2\2\2\u009d\u009b\3\2\2\2")
        buf.write("\u009d\u009e\3\2\2\2\u009e\u00a1\3\2\2\2\u009f\u009d\3")
        buf.write("\2\2\2\u00a0\u0098\3\2\2\2\u00a0\u0099\3\2\2\2\u00a1\20")
        buf.write("\3\2\2\2\u00a2\u00a7\5\17\b\2\u00a3\u00a7\5\t\5\2\u00a4")
        buf.write("\u00a7\5\13\6\2\u00a5\u00a7\5\r\7\2\u00a6\u00a2\3\2\2")
        buf.write("\2\u00a6\u00a3\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a5")
        buf.write("\3\2\2\2\u00a7\22\3\2\2\2\u00a8\u00a9\7u\2\2\u00a9\u00aa")
        buf.write("\7v\2\2\u00aa\u00ab\7t\2\2\u00ab\u00ac\7k\2\2\u00ac\u00ad")
        buf.write("\7p\2\2\u00ad\u00be\7i\2\2\u00ae\u00af\7k\2\2\u00af\u00b0")
        buf.write("\7p\2\2\u00b0\u00be\7v\2\2\u00b1\u00b2\7h\2\2\u00b2\u00b3")
        buf.write("\7n\2\2\u00b3\u00b4\7q\2\2\u00b4\u00b5\7c\2\2\u00b5\u00be")
        buf.write("\7v\2\2\u00b6\u00b7\7d\2\2\u00b7\u00b8\7q\2\2\u00b8\u00b9")
        buf.write("\7q\2\2\u00b9\u00ba\7n\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc")
        buf.write("\7c\2\2\u00bc\u00be\7p\2\2\u00bd\u00a8\3\2\2\2\u00bd\u00ae")
        buf.write("\3\2\2\2\u00bd\u00b1\3\2\2\2\u00bd\u00b6\3\2\2\2\u00be")
        buf.write("\u00bf\3\2\2\2\u00bf\u00c0\b\n\2\2\u00c0\24\3\2\2\2\u00c1")
        buf.write("\u00c2\7\61\2\2\u00c2\u00c3\7\61\2\2\u00c3\u00c7\3\2\2")
        buf.write("\2\u00c4\u00c6\n\b\2\2\u00c5\u00c4\3\2\2\2\u00c6\u00c9")
        buf.write("\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8")
        buf.write("\u00ca\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca\u00cb\b\13\3")
        buf.write("\2\u00cb\26\3\2\2\2\u00cc\u00cd\7\61\2\2\u00cd\u00ce\7")
        buf.write(",\2\2\u00ce\u00d2\3\2\2\2\u00cf\u00d1\13\2\2\2\u00d0\u00cf")
        buf.write("\3\2\2\2\u00d1\u00d4\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d2")
        buf.write("\u00d3\3\2\2\2\u00d3\u00d5\3\2\2\2\u00d4\u00d2\3\2\2\2")
        buf.write("\u00d5\u00d6\7,\2\2\u00d6\u00d7\7\61\2\2\u00d7\u00d8\3")
        buf.write("\2\2\2\u00d8\u00d9\b\f\3\2\u00d9\30\3\2\2\2\u00da\u00db")
        buf.write("\7p\2\2\u00db\u00dc\7k\2\2\u00dc\u00dd\7n\2\2\u00dd\32")
        buf.write("\3\2\2\2\u00de\u00df\7x\2\2\u00df\u00e0\7c\2\2\u00e0\u00e1")
        buf.write("\7t\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e3\b\16\4\2\u00e3")
        buf.write("\34\3\2\2\2\u00e4\u00e5\7e\2\2\u00e5\u00e6\7q\2\2\u00e6")
        buf.write("\u00e7\7p\2\2\u00e7\u00e8\7u\2\2\u00e8\u00e9\7v\2\2\u00e9")
        buf.write("\u00ea\3\2\2\2\u00ea\u00eb\b\17\5\2\u00eb\36\3\2\2\2\u00ec")
        buf.write("\u00ed\7v\2\2\u00ed\u00ee\7{\2\2\u00ee\u00ef\7r\2\2\u00ef")
        buf.write("\u00f0\7g\2\2\u00f0 \3\2\2\2\u00f1\u00f2\7u\2\2\u00f2")
        buf.write("\u00f3\7v\2\2\u00f3\u00f4\7t\2\2\u00f4\u00f5\7w\2\2\u00f5")
        buf.write("\u00f6\7e\2\2\u00f6\u00f7\7v\2\2\u00f7\u00f8\3\2\2\2\u00f8")
        buf.write("\u00f9\b\21\6\2\u00f9\"\3\2\2\2\u00fa\u00fb\7k\2\2\u00fb")
        buf.write("\u00fc\7p\2\2\u00fc\u00fd\7v\2\2\u00fd\u00fe\7g\2\2\u00fe")
        buf.write("\u00ff\7t\2\2\u00ff\u0100\7h\2\2\u0100\u0101\7c\2\2\u0101")
        buf.write("\u0102\7e\2\2\u0102\u0103\7g\2\2\u0103$\3\2\2\2\u0104")
        buf.write("\u0105\7h\2\2\u0105\u0106\7w\2\2\u0106\u0107\7p\2\2\u0107")
        buf.write("\u0108\7e\2\2\u0108&\3\2\2\2\u0109\u010a\7t\2\2\u010a")
        buf.write("\u010b\7g\2\2\u010b\u010c\7v\2\2\u010c\u010d\7w\2\2\u010d")
        buf.write("\u010e\7t\2\2\u010e\u010f\7p\2\2\u010f\u0110\3\2\2\2\u0110")
        buf.write("\u0111\b\24\7\2\u0111(\3\2\2\2\u0112\u0113\7k\2\2\u0113")
        buf.write("\u0114\7h\2\2\u0114\u0115\3\2\2\2\u0115\u0116\b\25\b\2")
        buf.write("\u0116*\3\2\2\2\u0117\u0118\7g\2\2\u0118\u0119\7n\2\2")
        buf.write("\u0119\u011a\7u\2\2\u011a\u011b\7g\2\2\u011b,\3\2\2\2")
        buf.write("\u011c\u011d\7h\2\2\u011d\u011e\7q\2\2\u011e\u011f\7t")
        buf.write("\2\2\u011f\u0120\3\2\2\2\u0120\u0121\b\27\t\2\u0121.\3")
        buf.write("\2\2\2\u0122\u0123\7t\2\2\u0123\u0124\7c\2\2\u0124\u0125")
        buf.write("\7p\2\2\u0125\u0126\7i\2\2\u0126\u0127\7g\2\2\u0127\60")
        buf.write("\3\2\2\2\u0128\u0129\7d\2\2\u0129\u012a\7t\2\2\u012a\u012b")
        buf.write("\7g\2\2\u012b\u012c\7c\2\2\u012c\u012d\7m\2\2\u012d\u012e")
        buf.write("\3\2\2\2\u012e\u012f\b\31\n\2\u012f\62\3\2\2\2\u0130\u0131")
        buf.write("\7e\2\2\u0131\u0132\7q\2\2\u0132\u0133\7p\2\2\u0133\u0134")
        buf.write("\7v\2\2\u0134\u0135\7k\2\2\u0135\u0136\7p\2\2\u0136\u0137")
        buf.write("\7w\2\2\u0137\u0138\7g\2\2\u0138\u0139\3\2\2\2\u0139\u013a")
        buf.write("\b\32\13\2\u013a\64\3\2\2\2\u013b\u013c\7v\2\2\u013c\u013d")
        buf.write("\7t\2\2\u013d\u013e\7w\2\2\u013e\u0145\7g\2\2\u013f\u0140")
        buf.write("\7h\2\2\u0140\u0141\7c\2\2\u0141\u0142\7n\2\2\u0142\u0143")
        buf.write("\7u\2\2\u0143\u0145\7g\2\2\u0144\u013b\3\2\2\2\u0144\u013f")
        buf.write("\3\2\2\2\u0145\66\3\2\2\2\u0146\u0147\7-\2\2\u0147\u0151")
        buf.write("\7?\2\2\u0148\u0149\7/\2\2\u0149\u0151\7?\2\2\u014a\u014b")
        buf.write("\7,\2\2\u014b\u0151\7?\2\2\u014c\u014d\7\61\2\2\u014d")
        buf.write("\u0151\7?\2\2\u014e\u014f\7\'\2\2\u014f\u0151\7?\2\2\u0150")
        buf.write("\u0146\3\2\2\2\u0150\u0148\3\2\2\2\u0150\u014a\3\2\2\2")
        buf.write("\u0150\u014c\3\2\2\2\u0150\u014e\3\2\2\2\u0151\u0152\3")
        buf.write("\2\2\2\u0152\u0153\b\34\f\2\u01538\3\2\2\2\u0154\u0155")
        buf.write("\7<\2\2\u0155\u0156\7?\2\2\u0156\u0157\3\2\2\2\u0157\u0158")
        buf.write("\b\35\r\2\u0158:\3\2\2\2\u0159\u015b\5k\66\2\u015a\u0159")
        buf.write("\3\2\2\2\u015b\u015e\3\2\2\2\u015c\u015a\3\2\2\2\u015c")
        buf.write("\u015d\3\2\2\2\u015d\u015f\3\2\2\2\u015e\u015c\3\2\2\2")
        buf.write("\u015f\u0163\7\60\2\2\u0160\u0162\5k\66\2\u0161\u0160")
        buf.write("\3\2\2\2\u0162\u0165\3\2\2\2\u0163\u0161\3\2\2\2\u0163")
        buf.write("\u0164\3\2\2\2\u0164\u0170\3\2\2\2\u0165\u0163\3\2\2\2")
        buf.write("\u0166\u0168\t\t\2\2\u0167\u0169\t\n\2\2\u0168\u0167\3")
        buf.write("\2\2\2\u0168\u0169\3\2\2\2\u0169\u016d\3\2\2\2\u016a\u016c")
        buf.write("\5k\66\2\u016b\u016a\3\2\2\2\u016c\u016f\3\2\2\2\u016d")
        buf.write("\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u0171\3\2\2\2")
        buf.write("\u016f\u016d\3\2\2\2\u0170\u0166\3\2\2\2\u0170\u0171\3")
        buf.write("\2\2\2\u0171<\3\2\2\2\u0172\u0173\7=\2\2\u0173\u0174\b")
        buf.write("\37\16\2\u0174>\3\2\2\2\u0175\u0176\7?\2\2\u0176\u0180")
        buf.write("\7?\2\2\u0177\u0178\7#\2\2\u0178\u0180\7?\2\2\u0179\u0180")
        buf.write("\7>\2\2\u017a\u017b\7>\2\2\u017b\u0180\7?\2\2\u017c\u0180")
        buf.write("\7@\2\2\u017d\u017e\7@\2\2\u017e\u0180\7?\2\2\u017f\u0175")
        buf.write("\3\2\2\2\u017f\u0177\3\2\2\2\u017f\u0179\3\2\2\2\u017f")
        buf.write("\u017a\3\2\2\2\u017f\u017c\3\2\2\2\u017f\u017d\3\2\2\2")
        buf.write("\u0180@\3\2\2\2\u0181\u0182\7(\2\2\u0182\u0183\7(\2\2")
        buf.write("\u0183B\3\2\2\2\u0184\u0185\7~\2\2\u0185\u0186\7~\2\2")
        buf.write("\u0186D\3\2\2\2\u0187\u0188\7#\2\2\u0188F\3\2\2\2\u0189")
        buf.write("\u018a\7-\2\2\u018aH\3\2\2\2\u018b\u018c\7/\2\2\u018c")
        buf.write("J\3\2\2\2\u018d\u018e\7,\2\2\u018eL\3\2\2\2\u018f\u0190")
        buf.write("\7\61\2\2\u0190N\3\2\2\2\u0191\u0192\7\'\2\2\u0192P\3")
        buf.write("\2\2\2\u0193\u0194\7?\2\2\u0194R\3\2\2\2\u0195\u0196\7")
        buf.write("*\2\2\u0196T\3\2\2\2\u0197\u0198\7+\2\2\u0198\u0199\b")
        buf.write("+\17\2\u0199V\3\2\2\2\u019a\u019b\7}\2\2\u019b\u019c\b")
        buf.write(",\20\2\u019cX\3\2\2\2\u019d\u019e\7\177\2\2\u019e\u019f")
        buf.write("\b-\21\2\u019fZ\3\2\2\2\u01a0\u01a1\7]\2\2\u01a1\\\3\2")
        buf.write("\2\2\u01a2\u01a3\7_\2\2\u01a3^\3\2\2\2\u01a4\u01a5\7.")
        buf.write("\2\2\u01a5`\3\2\2\2\u01a6\u01a7\7^\2\2\u01a7\u01b1\7p")
        buf.write("\2\2\u01a8\u01a9\7^\2\2\u01a9\u01b1\7v\2\2\u01aa\u01ab")
        buf.write("\7^\2\2\u01ab\u01b1\7t\2\2\u01ac\u01ad\7^\2\2\u01ad\u01b1")
        buf.write("\7$\2\2\u01ae\u01af\7^\2\2\u01af\u01b1\7^\2\2\u01b0\u01a6")
        buf.write("\3\2\2\2\u01b0\u01a8\3\2\2\2\u01b0\u01aa\3\2\2\2\u01b0")
        buf.write("\u01ac\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1b\3\2\2\2\u01b2")
        buf.write("\u01b5\n\13\2\2\u01b3\u01b5\5a\61\2\u01b4\u01b2\3\2\2")
        buf.write("\2\u01b4\u01b3\3\2\2\2\u01b5\u01b8\3\2\2\2\u01b6\u01b4")
        buf.write("\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7d\3\2\2\2\u01b8\u01b6")
        buf.write("\3\2\2\2\u01b9\u01ba\7$\2\2\u01ba\u01bb\5c\62\2\u01bb")
        buf.write("\u01bc\7$\2\2\u01bcf\3\2\2\2\u01bd\u01be\t\f\2\2\u01be")
        buf.write("h\3\2\2\2\u01bf\u01c0\t\r\2\2\u01c0j\3\2\2\2\u01c1\u01c2")
        buf.write("\t\16\2\2\u01c2l\3\2\2\2\u01c3\u01c4\t\17\2\2\u01c4n\3")
        buf.write("\2\2\2\u01c5\u01c9\5g\64\2\u01c6\u01c9\5i\65\2\u01c7\u01c9")
        buf.write("\7a\2\2\u01c8\u01c5\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8")
        buf.write("\u01c7\3\2\2\2\u01c9p\3\2\2\2\u01ca\u01cf\5o8\2\u01cb")
        buf.write("\u01ce\5o8\2\u01cc\u01ce\5k\66\2\u01cd\u01cb\3\2\2\2\u01cd")
        buf.write("\u01cc\3\2\2\2\u01ce\u01d1\3\2\2\2\u01cf\u01cd\3\2\2\2")
        buf.write("\u01cf\u01d0\3\2\2\2\u01d0\u01d2\3\2\2\2\u01d1\u01cf\3")
        buf.write("\2\2\2\u01d2\u01d3\b9\22\2\u01d3r\3\2\2\2\u01d4\u01d6")
        buf.write("\t\20\2\2\u01d5\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7")
        buf.write("\u01d5\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01d9\3\2\2\2")
        buf.write("\u01d9\u01da\b:\3\2\u01dat\3\2\2\2\u01db\u01dc\7\f\2\2")
        buf.write("\u01dc\u01dd\b;\23\2\u01ddv\3\2\2\2\u01de\u01df\7$\2\2")
        buf.write("\u01df\u01e0\5c\62\2\u01e0\u01e1\7^\2\2\u01e1\u01e2\13")
        buf.write("\2\2\2\u01e2\u01e3\b<\24\2\u01e3x\3\2\2\2\u01e4\u01e5")
        buf.write("\7$\2\2\u01e5\u01e8\5c\62\2\u01e6\u01e9\5u;\2\u01e7\u01e9")
        buf.write("\7\2\2\3\u01e8\u01e6\3\2\2\2\u01e8\u01e7\3\2\2\2\u01e9")
        buf.write("\u01ea\3\2\2\2\u01ea\u01eb\b=\25\2\u01ebz\3\2\2\2\u01ec")
        buf.write("\u01ed\13\2\2\2\u01ed|\3\2\2\2\34\2\u0088\u008f\u0096")
        buf.write("\u009d\u00a0\u00a6\u00bd\u00c7\u00d2\u0144\u0150\u015c")
        buf.write("\u0163\u0168\u016d\u0170\u017f\u01b0\u01b4\u01b6\u01c8")
        buf.write("\u01cd\u01cf\u01d7\u01e8\26\3\n\2\b\2\2\3\16\3\3\17\4")
        buf.write("\3\21\5\3\24\6\3\25\7\3\27\b\3\31\t\3\32\n\3\34\13\3\35")
        buf.write("\f\3\37\r\3+\16\3,\17\3-\20\39\21\3;\22\3<\23\3=\24")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    INTEGER = 4
    ATOMIC_TYPE = 5
    COMMENT1 = 6
    COMMENT2 = 7
    KEYWORD = 8
    VAR = 9
    CONST = 10
    TYPE = 11
    STRUCT = 12
    INTERFACE = 13
    FUNC = 14
    RETURN = 15
    IF = 16
    ELSE = 17
    FOR = 18
    RANGE = 19
    BREAK = 20
    CONTINUE = 21
    BOOLEAN = 22
    ASSIGN_OP = 23
    ASSIGN_STMT_OP = 24
    FLOAT = 25
    SEMI = 26
    COMPARE_OP = 27
    AND_OP = 28
    OR_OP = 29
    NOT_OP = 30
    ADD_OP = 31
    MINUS_OP = 32
    MUL_OP = 33
    DIV_OP = 34
    MOD_OP = 35
    ASSIGN_INIT = 36
    LPARENTHESIS = 37
    RPARENTHESIS = 38
    LBRACE = 39
    RBRACE = 40
    LBRACKET = 41
    RBRACKET = 42
    SEPARATOR = 43
    ESCAPE = 44
    STRING = 45
    ID = 46
    WS = 47
    NL = 48
    ILLEGAL_ESCAPE = 49
    UNCLOSE_STRING = 50
    ERROR_CHAR = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'.'", "'_'", "'nil'", "'var'", "'const'", "'type'", 
            "'struct'", "'interface'", "'func'", "'return'", "'if'", "'else'", 
            "'for'", "'range'", "'break'", "'continue'", "':='", "';'", 
            "'&&'", "'||'", "'!'", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "INTEGER", "ATOMIC_TYPE", "COMMENT1", "COMMENT2", "KEYWORD", 
            "VAR", "CONST", "TYPE", "STRUCT", "INTERFACE", "FUNC", "RETURN", 
            "IF", "ELSE", "FOR", "RANGE", "BREAK", "CONTINUE", "BOOLEAN", 
            "ASSIGN_OP", "ASSIGN_STMT_OP", "FLOAT", "SEMI", "COMPARE_OP", 
            "AND_OP", "OR_OP", "NOT_OP", "ADD_OP", "MINUS_OP", "MUL_OP", 
            "DIV_OP", "MOD_OP", "ASSIGN_INIT", "LPARENTHESIS", "RPARENTHESIS", 
            "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", "SEPARATOR", "ESCAPE", 
            "STRING", "ID", "WS", "NL", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
            "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "BINARY", "OCTAL", "HEXADEC", 
                  "DECIMAL", "INTEGER", "ATOMIC_TYPE", "COMMENT1", "COMMENT2", 
                  "KEYWORD", "VAR", "CONST", "TYPE", "STRUCT", "INTERFACE", 
                  "FUNC", "RETURN", "IF", "ELSE", "FOR", "RANGE", "BREAK", 
                  "CONTINUE", "BOOLEAN", "ASSIGN_OP", "ASSIGN_STMT_OP", 
                  "FLOAT", "SEMI", "COMPARE_OP", "AND_OP", "OR_OP", "NOT_OP", 
                  "ADD_OP", "MINUS_OP", "MUL_OP", "DIV_OP", "MOD_OP", "ASSIGN_INIT", 
                  "LPARENTHESIS", "RPARENTHESIS", "LBRACE", "RBRACE", "LBRACKET", 
                  "RBRACKET", "SEPARATOR", "ESCAPE", "IN_STRING", "STRING", 
                  "UpperLetter", "LowerLetter", "Digit", "NonZeroDigit", 
                  "IdentifierStart", "ID", "WS", "NL", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();

    afterStatement = False

    afterIf = False
    afterFor = False

    inStruct = False
    idInStruct = False


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[8] = self.ATOMIC_TYPE_action 
            actions[12] = self.VAR_action 
            actions[13] = self.CONST_action 
            actions[15] = self.STRUCT_action 
            actions[18] = self.RETURN_action 
            actions[19] = self.IF_action 
            actions[21] = self.FOR_action 
            actions[23] = self.BREAK_action 
            actions[24] = self.CONTINUE_action 
            actions[26] = self.ASSIGN_OP_action 
            actions[27] = self.ASSIGN_STMT_OP_action 
            actions[29] = self.SEMI_action 
            actions[41] = self.RPARENTHESIS_action 
            actions[42] = self.LBRACE_action 
            actions[43] = self.RBRACE_action 
            actions[55] = self.ID_action 
            actions[57] = self.NL_action 
            actions[58] = self.ILLEGAL_ESCAPE_action 
            actions[59] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ATOMIC_TYPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                if self.inStruct:
                    self.afterStatement = True

     

    def VAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                self.afterStatement = True

     

    def CONST_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                self.afterStatement = True

     

    def STRUCT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                self.inStruct = True

     

    def RETURN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                self.afterStatement = True

     

    def IF_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                self.afterIf = True

     

    def FOR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

                self.afterFor = True

     

    def BREAK_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:

                self.afterStatement = True

     

    def CONTINUE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:

                self.afterStatement = True

     

    def ASSIGN_OP_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 9:

                self.afterStatement = True

     

    def ASSIGN_STMT_OP_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 10:

                if not self.afterFor:
                    self.afterStatement = True
                else:
                    self.afterFor = False

     

    def SEMI_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 11:

                self.afterStatement = False

     

    def RPARENTHESIS_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 12:

                if not self.afterIf:
                    self.afterStatement = True
                else:
                    self.afterIf = False

     

    def LBRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 13:

                self.afterStatement = False

     

    def RBRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 14:

                self.afterStatement = True
                if self.inStruct:
                    self.inStruct = False

     

    def ID_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 15:

                if self.inStruct:
                    if not self.idInStruct:
                        self.idInStruct = True
                    else:
                        self.afterStatement = True

     

    def NL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 16:

                if self.afterStatement:
                    self.afterStatement = False
                    self.type = self.SEMI
                    self.text = ";"
                    return self.emit()
                self.skip()

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 17:

                raise IllegalEscape(self.text)

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 18:

                self.text = self.text.split('\r\n')[0]
                raise UncloseString(self.text)

     



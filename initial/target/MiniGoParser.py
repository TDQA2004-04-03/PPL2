# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u01b6\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\3\2\6\2J\n")
        buf.write("\2\r\2\16\2K\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3V\n\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\5\4i\n\4\3\4\3\4\3\5\3\5\3\5\5\5p\n\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\5\b\u0082\n\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u008a")
        buf.write("\n\b\5\b\u008c\n\b\3\t\3\t\3\t\3\n\6\n\u0092\n\n\r\n\16")
        buf.write("\n\u0093\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\7")
        buf.write("\f\u00a0\n\f\f\f\16\f\u00a3\13\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\r\5\r\u00ab\n\r\3\16\3\16\3\16\3\16\3\16\6\16\u00b2\n")
        buf.write("\16\r\16\16\16\u00b3\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\7\20\u00c2\n\20\f\20\16\20\u00c5")
        buf.write("\13\20\5\20\u00c7\n\20\3\20\3\20\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\5\21\u00d2\n\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\6\22\u00db\n\22\r\22\16\22\u00dc\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\7\23\u00e6\n\23\f\23\16\23\u00e9")
        buf.write("\13\23\5\23\u00eb\n\23\3\23\3\23\5\23\u00ef\n\23\3\24")
        buf.write("\3\24\3\24\7\24\u00f4\n\24\f\24\16\24\u00f7\13\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\7\25\u00fe\n\25\f\25\16\25\u0101")
        buf.write("\13\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\7\27\u010a\n")
        buf.write("\27\f\27\16\27\u010d\13\27\3\30\3\30\5\30\u0111\n\30\3")
        buf.write("\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\5\32\u011f\n\32\3\33\3\33\3\33\3\33\3\33\7\33\u0126")
        buf.write("\n\33\f\33\16\33\u0129\13\33\5\33\u012b\n\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u0137\n")
        buf.write("\34\f\34\16\34\u013a\13\34\5\34\u013c\n\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u0147\n\34\f\34")
        buf.write("\16\34\u014a\13\34\5\34\u014c\n\34\3\34\7\34\u014f\n\34")
        buf.write("\f\34\16\34\u0152\13\34\3\35\3\35\3\35\3\35\3\35\5\35")
        buf.write("\u0159\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\5\36\u0168\n\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\7\36\u0179\n\36\f\36\16\36\u017c\13\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\5\37\u0183\n\37\5\37\u0185\n\37\3 \3 ")
        buf.write("\3 \3 \3 \3!\3!\6!\u018e\n!\r!\16!\u018f\3!\3!\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\5\"\u019b\n\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u01ab\n\"\3#")
        buf.write("\3#\3#\3#\3#\5#\u01b2\n#\3$\3$\3$\2\4\66:%\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@")
        buf.write("BDF\2\n\4\2\7\7\60\60\4\2\6\6\60\60\3\2\31\32\4\2  \"")
        buf.write("\"\3\2#%\3\2!\"\4\2\5\5\60\60\6\2\6\6\30\30\33\33//\2")
        buf.write("\u01e2\2I\3\2\2\2\4U\3\2\2\2\6h\3\2\2\2\bo\3\2\2\2\nq")
        buf.write("\3\2\2\2\fv\3\2\2\2\16\u008b\3\2\2\2\20\u008d\3\2\2\2")
        buf.write("\22\u0091\3\2\2\2\24\u0097\3\2\2\2\26\u009b\3\2\2\2\30")
        buf.write("\u00aa\3\2\2\2\32\u00ac\3\2\2\2\34\u00b7\3\2\2\2\36\u00bc")
        buf.write("\3\2\2\2 \u00ca\3\2\2\2\"\u00d3\3\2\2\2$\u00e0\3\2\2\2")
        buf.write("&\u00f0\3\2\2\2(\u00fa\3\2\2\2*\u0102\3\2\2\2,\u0105\3")
        buf.write("\2\2\2.\u010e\3\2\2\2\60\u0115\3\2\2\2\62\u011a\3\2\2")
        buf.write("\2\64\u0120\3\2\2\2\66\u012e\3\2\2\28\u0153\3\2\2\2:\u0167")
        buf.write("\3\2\2\2<\u017d\3\2\2\2>\u0186\3\2\2\2@\u018b\3\2\2\2")
        buf.write("B\u01aa\3\2\2\2D\u01ac\3\2\2\2F\u01b3\3\2\2\2HJ\5\4\3")
        buf.write("\2IH\3\2\2\2JK\3\2\2\2KI\3\2\2\2KL\3\2\2\2LM\3\2\2\2M")
        buf.write("N\7\2\2\3N\3\3\2\2\2OV\5\n\6\2PV\5\f\7\2QV\5\16\b\2RV")
        buf.write("\5\32\16\2SV\5\"\22\2TV\5.\30\2UO\3\2\2\2UP\3\2\2\2UQ")
        buf.write("\3\2\2\2UR\3\2\2\2US\3\2\2\2UT\3\2\2\2VW\3\2\2\2WX\7\34")
        buf.write("\2\2X\5\3\2\2\2Yi\5.\30\2Zi\5\32\16\2[i\5\"\22\2\\i\5")
        buf.write("<\37\2]i\5B\"\2^i\5\f\7\2_i\5\16\b\2`i\5\n\6\2ai\58\35")
        buf.write("\2bi\5\62\32\2ci\5\64\33\2di\5\66\34\2ei\5,\27\2fi\7\26")
        buf.write("\2\2gi\7\27\2\2hY\3\2\2\2hZ\3\2\2\2h[\3\2\2\2h\\\3\2\2")
        buf.write("\2h]\3\2\2\2h^\3\2\2\2h_\3\2\2\2h`\3\2\2\2ha\3\2\2\2h")
        buf.write("b\3\2\2\2hc\3\2\2\2hd\3\2\2\2he\3\2\2\2hf\3\2\2\2hg\3")
        buf.write("\2\2\2ij\3\2\2\2jk\7\34\2\2k\7\3\2\2\2lp\7\7\2\2mp\7\60")
        buf.write("\2\2np\5\22\n\2ol\3\2\2\2om\3\2\2\2on\3\2\2\2p\t\3\2\2")
        buf.write("\2qr\7\f\2\2rs\7\60\2\2st\7&\2\2tu\5:\36\2u\13\3\2\2\2")
        buf.write("vw\7\13\2\2wx\7\60\2\2xy\5\b\5\2y\r\3\2\2\2z{\7\13\2\2")
        buf.write("{|\7\60\2\2|}\5\b\5\2}\u0081\7&\2\2~\u0082\5:\36\2\177")
        buf.write("\u0082\5\20\t\2\u0080\u0082\5\36\20\2\u0081~\3\2\2\2\u0081")
        buf.write("\177\3\2\2\2\u0081\u0080\3\2\2\2\u0082\u008c\3\2\2\2\u0083")
        buf.write("\u0084\7\13\2\2\u0084\u0085\7\60\2\2\u0085\u0089\7&\2")
        buf.write("\2\u0086\u008a\5:\36\2\u0087\u008a\5\20\t\2\u0088\u008a")
        buf.write("\5\36\20\2\u0089\u0086\3\2\2\2\u0089\u0087\3\2\2\2\u0089")
        buf.write("\u0088\3\2\2\2\u008a\u008c\3\2\2\2\u008bz\3\2\2\2\u008b")
        buf.write("\u0083\3\2\2\2\u008c\17\3\2\2\2\u008d\u008e\5\22\n\2\u008e")
        buf.write("\u008f\5\26\f\2\u008f\21\3\2\2\2\u0090\u0092\5\24\13\2")
        buf.write("\u0091\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0091\3")
        buf.write("\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0096")
        buf.write("\t\2\2\2\u0096\23\3\2\2\2\u0097\u0098\7+\2\2\u0098\u0099")
        buf.write("\t\3\2\2\u0099\u009a\7,\2\2\u009a\25\3\2\2\2\u009b\u009c")
        buf.write("\7)\2\2\u009c\u00a1\5\30\r\2\u009d\u009e\7-\2\2\u009e")
        buf.write("\u00a0\5\30\r\2\u009f\u009d\3\2\2\2\u00a0\u00a3\3\2\2")
        buf.write("\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a4")
        buf.write("\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a5\7*\2\2\u00a5")
        buf.write("\27\3\2\2\2\u00a6\u00ab\5F$\2\u00a7\u00ab\5\36\20\2\u00a8")
        buf.write("\u00ab\7\60\2\2\u00a9\u00ab\5\26\f\2\u00aa\u00a6\3\2\2")
        buf.write("\2\u00aa\u00a7\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00a9")
        buf.write("\3\2\2\2\u00ab\31\3\2\2\2\u00ac\u00ad\7\r\2\2\u00ad\u00ae")
        buf.write("\7\60\2\2\u00ae\u00af\7\16\2\2\u00af\u00b1\7)\2\2\u00b0")
        buf.write("\u00b2\5\34\17\2\u00b1\u00b0\3\2\2\2\u00b2\u00b3\3\2\2")
        buf.write("\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5")
        buf.write("\3\2\2\2\u00b5\u00b6\7*\2\2\u00b6\33\3\2\2\2\u00b7\u00b8")
        buf.write("\7\60\2\2\u00b8\u00b9\5\b\5\2\u00b9\u00ba\3\2\2\2\u00ba")
        buf.write("\u00bb\7\34\2\2\u00bb\35\3\2\2\2\u00bc\u00bd\7\60\2\2")
        buf.write("\u00bd\u00c6\7)\2\2\u00be\u00c3\5 \21\2\u00bf\u00c0\7")
        buf.write("-\2\2\u00c0\u00c2\5 \21\2\u00c1\u00bf\3\2\2\2\u00c2\u00c5")
        buf.write("\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4")
        buf.write("\u00c7\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c6\u00be\3\2\2\2")
        buf.write("\u00c6\u00c7\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c9\7")
        buf.write("*\2\2\u00c9\37\3\2\2\2\u00ca\u00cb\7\60\2\2\u00cb\u00d1")
        buf.write("\7\3\2\2\u00cc\u00d2\5F$\2\u00cd\u00d2\5\20\t\2\u00ce")
        buf.write("\u00d2\5\36\20\2\u00cf\u00d2\5 \21\2\u00d0\u00d2\5(\25")
        buf.write("\2\u00d1\u00cc\3\2\2\2\u00d1\u00cd\3\2\2\2\u00d1\u00ce")
        buf.write("\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d1\u00d0\3\2\2\2\u00d2")
        buf.write("!\3\2\2\2\u00d3\u00d4\7\r\2\2\u00d4\u00d5\7\60\2\2\u00d5")
        buf.write("\u00d6\7\17\2\2\u00d6\u00da\7)\2\2\u00d7\u00d8\5$\23\2")
        buf.write("\u00d8\u00d9\7\34\2\2\u00d9\u00db\3\2\2\2\u00da\u00d7")
        buf.write("\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc")
        buf.write("\u00dd\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00df\7*\2\2")
        buf.write("\u00df#\3\2\2\2\u00e0\u00e1\7\60\2\2\u00e1\u00ea\7\'\2")
        buf.write("\2\u00e2\u00e7\5&\24\2\u00e3\u00e4\7-\2\2\u00e4\u00e6")
        buf.write("\5&\24\2\u00e5\u00e3\3\2\2\2\u00e6\u00e9\3\2\2\2\u00e7")
        buf.write("\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00eb\3\2\2\2")
        buf.write("\u00e9\u00e7\3\2\2\2\u00ea\u00e2\3\2\2\2\u00ea\u00eb\3")
        buf.write("\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ee\7(\2\2\u00ed\u00ef")
        buf.write("\5\b\5\2\u00ee\u00ed\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef")
        buf.write("%\3\2\2\2\u00f0\u00f5\7\60\2\2\u00f1\u00f2\7-\2\2\u00f2")
        buf.write("\u00f4\7\60\2\2\u00f3\u00f1\3\2\2\2\u00f4\u00f7\3\2\2")
        buf.write("\2\u00f5\u00f3\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f8")
        buf.write("\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f8\u00f9\5\b\5\2\u00f9")
        buf.write("\'\3\2\2\2\u00fa\u00ff\7\60\2\2\u00fb\u00fe\5\24\13\2")
        buf.write("\u00fc\u00fe\5*\26\2\u00fd\u00fb\3\2\2\2\u00fd\u00fc\3")
        buf.write("\2\2\2\u00fe\u0101\3\2\2\2\u00ff\u00fd\3\2\2\2\u00ff\u0100")
        buf.write("\3\2\2\2\u0100)\3\2\2\2\u0101\u00ff\3\2\2\2\u0102\u0103")
        buf.write("\7\4\2\2\u0103\u0104\7\60\2\2\u0104+\3\2\2\2\u0105\u010b")
        buf.write("\5\66\34\2\u0106\u010a\5\24\13\2\u0107\u0108\7\4\2\2\u0108")
        buf.write("\u010a\7\60\2\2\u0109\u0106\3\2\2\2\u0109\u0107\3\2\2")
        buf.write("\2\u010a\u010d\3\2\2\2\u010b\u0109\3\2\2\2\u010b\u010c")
        buf.write("\3\2\2\2\u010c-\3\2\2\2\u010d\u010b\3\2\2\2\u010e\u0110")
        buf.write("\7\20\2\2\u010f\u0111\5\60\31\2\u0110\u010f\3\2\2\2\u0110")
        buf.write("\u0111\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0113\5$\23\2")
        buf.write("\u0113\u0114\5@!\2\u0114/\3\2\2\2\u0115\u0116\7\'\2\2")
        buf.write("\u0116\u0117\7\60\2\2\u0117\u0118\7\60\2\2\u0118\u0119")
        buf.write("\7(\2\2\u0119\61\3\2\2\2\u011a\u011e\7\21\2\2\u011b\u011f")
        buf.write("\5:\36\2\u011c\u011f\5\20\t\2\u011d\u011f\5\36\20\2\u011e")
        buf.write("\u011b\3\2\2\2\u011e\u011c\3\2\2\2\u011e\u011d\3\2\2\2")
        buf.write("\u011f\63\3\2\2\2\u0120\u0121\7\60\2\2\u0121\u012a\7\'")
        buf.write("\2\2\u0122\u0127\5:\36\2\u0123\u0124\7-\2\2\u0124\u0126")
        buf.write("\5:\36\2\u0125\u0123\3\2\2\2\u0126\u0129\3\2\2\2\u0127")
        buf.write("\u0125\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u012b\3\2\2\2")
        buf.write("\u0129\u0127\3\2\2\2\u012a\u0122\3\2\2\2\u012a\u012b\3")
        buf.write("\2\2\2\u012b\u012c\3\2\2\2\u012c\u012d\7(\2\2\u012d\65")
        buf.write("\3\2\2\2\u012e\u012f\b\34\1\2\u012f\u0130\5(\25\2\u0130")
        buf.write("\u0131\7\4\2\2\u0131\u0132\7\60\2\2\u0132\u013b\7\'\2")
        buf.write("\2\u0133\u0138\5:\36\2\u0134\u0135\7-\2\2\u0135\u0137")
        buf.write("\5:\36\2\u0136\u0134\3\2\2\2\u0137\u013a\3\2\2\2\u0138")
        buf.write("\u0136\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013c\3\2\2\2")
        buf.write("\u013a\u0138\3\2\2\2\u013b\u0133\3\2\2\2\u013b\u013c\3")
        buf.write("\2\2\2\u013c\u013d\3\2\2\2\u013d\u013e\7(\2\2\u013e\u0150")
        buf.write("\3\2\2\2\u013f\u0140\f\4\2\2\u0140\u0141\7\4\2\2\u0141")
        buf.write("\u0142\7\60\2\2\u0142\u014b\7\'\2\2\u0143\u0148\5:\36")
        buf.write("\2\u0144\u0145\7-\2\2\u0145\u0147\5:\36\2\u0146\u0144")
        buf.write("\3\2\2\2\u0147\u014a\3\2\2\2\u0148\u0146\3\2\2\2\u0148")
        buf.write("\u0149\3\2\2\2\u0149\u014c\3\2\2\2\u014a\u0148\3\2\2\2")
        buf.write("\u014b\u0143\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014d\3")
        buf.write("\2\2\2\u014d\u014f\7(\2\2\u014e\u013f\3\2\2\2\u014f\u0152")
        buf.write("\3\2\2\2\u0150\u014e\3\2\2\2\u0150\u0151\3\2\2\2\u0151")
        buf.write("\67\3\2\2\2\u0152\u0150\3\2\2\2\u0153\u0154\5(\25\2\u0154")
        buf.write("\u0158\t\4\2\2\u0155\u0159\5:\36\2\u0156\u0159\5\20\t")
        buf.write("\2\u0157\u0159\5\36\20\2\u0158\u0155\3\2\2\2\u0158\u0156")
        buf.write("\3\2\2\2\u0158\u0157\3\2\2\2\u01599\3\2\2\2\u015a\u015b")
        buf.write("\b\36\1\2\u015b\u015c\7\'\2\2\u015c\u015d\5:\36\2\u015d")
        buf.write("\u015e\7(\2\2\u015e\u0168\3\2\2\2\u015f\u0160\t\5\2\2")
        buf.write("\u0160\u0168\5:\36\16\u0161\u0168\5\64\33\2\u0162\u0168")
        buf.write("\5\66\34\2\u0163\u0168\5,\27\2\u0164\u0168\5(\25\2\u0165")
        buf.write("\u0168\5F$\2\u0166\u0168\7\n\2\2\u0167\u015a\3\2\2\2\u0167")
        buf.write("\u015f\3\2\2\2\u0167\u0161\3\2\2\2\u0167\u0162\3\2\2\2")
        buf.write("\u0167\u0163\3\2\2\2\u0167\u0164\3\2\2\2\u0167\u0165\3")
        buf.write("\2\2\2\u0167\u0166\3\2\2\2\u0168\u017a\3\2\2\2\u0169\u016a")
        buf.write("\f\r\2\2\u016a\u016b\t\6\2\2\u016b\u0179\5:\36\16\u016c")
        buf.write("\u016d\f\f\2\2\u016d\u016e\t\7\2\2\u016e\u0179\5:\36\r")
        buf.write("\u016f\u0170\f\13\2\2\u0170\u0171\7\35\2\2\u0171\u0179")
        buf.write("\5:\36\f\u0172\u0173\f\n\2\2\u0173\u0174\7\36\2\2\u0174")
        buf.write("\u0179\5:\36\13\u0175\u0176\f\t\2\2\u0176\u0177\7\37\2")
        buf.write("\2\u0177\u0179\5:\36\n\u0178\u0169\3\2\2\2\u0178\u016c")
        buf.write("\3\2\2\2\u0178\u016f\3\2\2\2\u0178\u0172\3\2\2\2\u0178")
        buf.write("\u0175\3\2\2\2\u0179\u017c\3\2\2\2\u017a\u0178\3\2\2\2")
        buf.write("\u017a\u017b\3\2\2\2\u017b;\3\2\2\2\u017c\u017a\3\2\2")
        buf.write("\2\u017d\u017e\5> \2\u017e\u0184\5@!\2\u017f\u0182\7\23")
        buf.write("\2\2\u0180\u0183\5<\37\2\u0181\u0183\5@!\2\u0182\u0180")
        buf.write("\3\2\2\2\u0182\u0181\3\2\2\2\u0183\u0185\3\2\2\2\u0184")
        buf.write("\u017f\3\2\2\2\u0184\u0185\3\2\2\2\u0185=\3\2\2\2\u0186")
        buf.write("\u0187\7\22\2\2\u0187\u0188\7\'\2\2\u0188\u0189\5:\36")
        buf.write("\2\u0189\u018a\7(\2\2\u018a?\3\2\2\2\u018b\u018d\7)\2")
        buf.write("\2\u018c\u018e\5\6\4\2\u018d\u018c\3\2\2\2\u018e\u018f")
        buf.write("\3\2\2\2\u018f\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190")
        buf.write("\u0191\3\2\2\2\u0191\u0192\7*\2\2\u0192A\3\2\2\2\u0193")
        buf.write("\u0194\7\24\2\2\u0194\u0195\5:\36\2\u0195\u0196\5@!\2")
        buf.write("\u0196\u01ab\3\2\2\2\u0197\u019a\7\24\2\2\u0198\u019b")
        buf.write("\5D#\2\u0199\u019b\5\16\b\2\u019a\u0198\3\2\2\2\u019a")
        buf.write("\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019d\7\34\2")
        buf.write("\2\u019d\u019e\5:\36\2\u019e\u019f\7\34\2\2\u019f\u01a0")
        buf.write("\58\35\2\u01a0\u01a1\5@!\2\u01a1\u01ab\3\2\2\2\u01a2\u01a3")
        buf.write("\7\24\2\2\u01a3\u01a4\t\b\2\2\u01a4\u01a5\7-\2\2\u01a5")
        buf.write("\u01a6\7\60\2\2\u01a6\u01a7\7\32\2\2\u01a7\u01a8\7\25")
        buf.write("\2\2\u01a8\u01a9\7\60\2\2\u01a9\u01ab\5@!\2\u01aa\u0193")
        buf.write("\3\2\2\2\u01aa\u0197\3\2\2\2\u01aa\u01a2\3\2\2\2\u01ab")
        buf.write("C\3\2\2\2\u01ac\u01ad\7\60\2\2\u01ad\u01b1\t\4\2\2\u01ae")
        buf.write("\u01b2\5:\36\2\u01af\u01b2\5\20\t\2\u01b0\u01b2\5\36\20")
        buf.write("\2\u01b1\u01ae\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1\u01b0")
        buf.write("\3\2\2\2\u01b2E\3\2\2\2\u01b3\u01b4\t\t\2\2\u01b4G\3\2")
        buf.write("\2\2,KUho\u0081\u0089\u008b\u0093\u00a1\u00aa\u00b3\u00c3")
        buf.write("\u00c6\u00d1\u00dc\u00e7\u00ea\u00ee\u00f5\u00fd\u00ff")
        buf.write("\u0109\u010b\u0110\u011e\u0127\u012a\u0138\u013b\u0148")
        buf.write("\u014b\u0150\u0158\u0167\u0178\u017a\u0182\u0184\u018f")
        buf.write("\u019a\u01aa\u01b1")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'.'", "'_'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'nil'", "'var'", "'const'", 
                     "'type'", "'struct'", "'interface'", "'func'", "'return'", 
                     "'if'", "'else'", "'for'", "'range'", "'break'", "'continue'", 
                     "<INVALID>", "<INVALID>", "':='", "<INVALID>", "';'", 
                     "<INVALID>", "'&&'", "'||'", "'!'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'='", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "','", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INTEGER", "ATOMIC_TYPE", "COMMENT1", "COMMENT2", 
                      "KEYWORD", "VAR", "CONST", "TYPE", "STRUCT", "INTERFACE", 
                      "FUNC", "RETURN", "IF", "ELSE", "FOR", "RANGE", "BREAK", 
                      "CONTINUE", "BOOLEAN", "ASSIGN_OP", "ASSIGN_STMT_OP", 
                      "FLOAT", "SEMI", "COMPARE_OP", "AND_OP", "OR_OP", 
                      "NOT_OP", "ADD_OP", "MINUS_OP", "MUL_OP", "DIV_OP", 
                      "MOD_OP", "ASSIGN_INIT", "LPARENTHESIS", "RPARENTHESIS", 
                      "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", "SEPARATOR", 
                      "ESCAPE", "STRING", "ID", "WS", "NL", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_statement = 2
    RULE_typedef = 3
    RULE_constdecl = 4
    RULE_vardecl = 5
    RULE_vardeclassign = 6
    RULE_array = 7
    RULE_array_type = 8
    RULE_array_index = 9
    RULE_array_list = 10
    RULE_array_mem = 11
    RULE_structdecl = 12
    RULE_structfielddecl = 13
    RULE_structliteral = 14
    RULE_structfieldliteral = 15
    RULE_interfacedecl = 16
    RULE_method_signature = 17
    RULE_argument = 18
    RULE_var_access = 19
    RULE_field_access = 20
    RULE_method_var_access = 21
    RULE_func_and_method_decl = 22
    RULE_method_receiver = 23
    RULE_ret = 24
    RULE_funccall = 25
    RULE_methodcall = 26
    RULE_assignment = 27
    RULE_expression = 28
    RULE_if_stmt = 29
    RULE_if_condition = 30
    RULE_block = 31
    RULE_for_loop = 32
    RULE_assignment_for = 33
    RULE_literal = 34

    ruleNames =  [ "program", "decl", "statement", "typedef", "constdecl", 
                   "vardecl", "vardeclassign", "array", "array_type", "array_index", 
                   "array_list", "array_mem", "structdecl", "structfielddecl", 
                   "structliteral", "structfieldliteral", "interfacedecl", 
                   "method_signature", "argument", "var_access", "field_access", 
                   "method_var_access", "func_and_method_decl", "method_receiver", 
                   "ret", "funccall", "methodcall", "assignment", "expression", 
                   "if_stmt", "if_condition", "block", "for_loop", "assignment_for", 
                   "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    INTEGER=4
    ATOMIC_TYPE=5
    COMMENT1=6
    COMMENT2=7
    KEYWORD=8
    VAR=9
    CONST=10
    TYPE=11
    STRUCT=12
    INTERFACE=13
    FUNC=14
    RETURN=15
    IF=16
    ELSE=17
    FOR=18
    RANGE=19
    BREAK=20
    CONTINUE=21
    BOOLEAN=22
    ASSIGN_OP=23
    ASSIGN_STMT_OP=24
    FLOAT=25
    SEMI=26
    COMPARE_OP=27
    AND_OP=28
    OR_OP=29
    NOT_OP=30
    ADD_OP=31
    MINUS_OP=32
    MUL_OP=33
    DIV_OP=34
    MOD_OP=35
    ASSIGN_INIT=36
    LPARENTHESIS=37
    RPARENTHESIS=38
    LBRACE=39
    RBRACE=40
    LBRACKET=41
    RBRACKET=42
    SEPARATOR=43
    ESCAPE=44
    STRING=45
    ID=46
    WS=47
    NL=48
    ILLEGAL_ESCAPE=49
    UNCLOSE_STRING=50
    ERROR_CHAR=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 70
                self.decl()
                self.state = 73 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.FUNC))) != 0)):
                    break

            self.state = 75
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def vardeclassign(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclassignContext,0)


        def structdecl(self):
            return self.getTypedRuleContext(MiniGoParser.StructdeclContext,0)


        def interfacedecl(self):
            return self.getTypedRuleContext(MiniGoParser.InterfacedeclContext,0)


        def func_and_method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_and_method_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 77
                self.constdecl()
                pass

            elif la_ == 2:
                self.state = 78
                self.vardecl()
                pass

            elif la_ == 3:
                self.state = 79
                self.vardeclassign()
                pass

            elif la_ == 4:
                self.state = 80
                self.structdecl()
                pass

            elif la_ == 5:
                self.state = 81
                self.interfacedecl()
                pass

            elif la_ == 6:
                self.state = 82
                self.func_and_method_decl()
                pass


            self.state = 85
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def func_and_method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_and_method_declContext,0)


        def structdecl(self):
            return self.getTypedRuleContext(MiniGoParser.StructdeclContext,0)


        def interfacedecl(self):
            return self.getTypedRuleContext(MiniGoParser.InterfacedeclContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmtContext,0)


        def for_loop(self):
            return self.getTypedRuleContext(MiniGoParser.For_loopContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def vardeclassign(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclassignContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentContext,0)


        def ret(self):
            return self.getTypedRuleContext(MiniGoParser.RetContext,0)


        def funccall(self):
            return self.getTypedRuleContext(MiniGoParser.FunccallContext,0)


        def methodcall(self):
            return self.getTypedRuleContext(MiniGoParser.MethodcallContext,0)


        def method_var_access(self):
            return self.getTypedRuleContext(MiniGoParser.Method_var_accessContext,0)


        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 87
                self.func_and_method_decl()
                pass

            elif la_ == 2:
                self.state = 88
                self.structdecl()
                pass

            elif la_ == 3:
                self.state = 89
                self.interfacedecl()
                pass

            elif la_ == 4:
                self.state = 90
                self.if_stmt()
                pass

            elif la_ == 5:
                self.state = 91
                self.for_loop()
                pass

            elif la_ == 6:
                self.state = 92
                self.vardecl()
                pass

            elif la_ == 7:
                self.state = 93
                self.vardeclassign()
                pass

            elif la_ == 8:
                self.state = 94
                self.constdecl()
                pass

            elif la_ == 9:
                self.state = 95
                self.assignment()
                pass

            elif la_ == 10:
                self.state = 96
                self.ret()
                pass

            elif la_ == 11:
                self.state = 97
                self.funccall()
                pass

            elif la_ == 12:
                self.state = 98
                self.methodcall(0)
                pass

            elif la_ == 13:
                self.state = 99
                self.method_var_access()
                pass

            elif la_ == 14:
                self.state = 100
                self.match(MiniGoParser.BREAK)
                pass

            elif la_ == 15:
                self.state = 101
                self.match(MiniGoParser.CONTINUE)
                pass


            self.state = 104
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATOMIC_TYPE(self):
            return self.getToken(MiniGoParser.ATOMIC_TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typedef

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypedef" ):
                return visitor.visitTypedef(self)
            else:
                return visitor.visitChildren(self)




    def typedef(self):

        localctx = MiniGoParser.TypedefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_typedef)
        try:
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ATOMIC_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.match(MiniGoParser.ATOMIC_TYPE)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 3)
                self.state = 108
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN_INIT(self):
            return self.getToken(MiniGoParser.ASSIGN_INIT, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstdecl" ):
                return visitor.visitConstdecl(self)
            else:
                return visitor.visitChildren(self)




    def constdecl(self):

        localctx = MiniGoParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_constdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(MiniGoParser.CONST)
            self.state = 112
            self.match(MiniGoParser.ID)
            self.state = 113
            self.match(MiniGoParser.ASSIGN_INIT)
            self.state = 114
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typedef(self):
            return self.getTypedRuleContext(MiniGoParser.TypedefContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(MiniGoParser.VAR)
            self.state = 117
            self.match(MiniGoParser.ID)
            self.state = 118
            self.typedef()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclassignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typedef(self):
            return self.getTypedRuleContext(MiniGoParser.TypedefContext,0)


        def ASSIGN_INIT(self):
            return self.getToken(MiniGoParser.ASSIGN_INIT, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def array(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayContext,0)


        def structliteral(self):
            return self.getTypedRuleContext(MiniGoParser.StructliteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_vardeclassign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardeclassign" ):
                return visitor.visitVardeclassign(self)
            else:
                return visitor.visitChildren(self)




    def vardeclassign(self):

        localctx = MiniGoParser.VardeclassignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vardeclassign)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.match(MiniGoParser.VAR)
                self.state = 121
                self.match(MiniGoParser.ID)
                self.state = 122
                self.typedef()
                self.state = 123
                self.match(MiniGoParser.ASSIGN_INIT)
                self.state = 127
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 124
                    self.expression(0)
                    pass

                elif la_ == 2:
                    self.state = 125
                    self.array()
                    pass

                elif la_ == 3:
                    self.state = 126
                    self.structliteral()
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.match(MiniGoParser.VAR)
                self.state = 130
                self.match(MiniGoParser.ID)
                self.state = 131
                self.match(MiniGoParser.ASSIGN_INIT)
                self.state = 135
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 132
                    self.expression(0)
                    pass

                elif la_ == 2:
                    self.state = 133
                    self.array()
                    pass

                elif la_ == 3:
                    self.state = 134
                    self.structliteral()
                    pass


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def array_list(self):
            return self.getTypedRuleContext(MiniGoParser.Array_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = MiniGoParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.array_type()
            self.state = 140
            self.array_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATOMIC_TYPE(self):
            return self.getToken(MiniGoParser.ATOMIC_TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def array_index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_indexContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_indexContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = MiniGoParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 142
                self.array_index()
                self.state = 145 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LBRACKET):
                    break

            self.state = 147
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ATOMIC_TYPE or _la==MiniGoParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def INTEGER(self):
            return self.getToken(MiniGoParser.INTEGER, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_index" ):
                return visitor.visitArray_index(self)
            else:
                return visitor.visitChildren(self)




    def array_index(self):

        localctx = MiniGoParser.Array_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array_index)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(MiniGoParser.LBRACKET)
            self.state = 150
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.INTEGER or _la==MiniGoParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 151
            self.match(MiniGoParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def array_mem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_memContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_memContext,i)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEPARATOR(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEPARATOR)
            else:
                return self.getToken(MiniGoParser.SEPARATOR, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list" ):
                return visitor.visitArray_list(self)
            else:
                return visitor.visitChildren(self)




    def array_list(self):

        localctx = MiniGoParser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_array_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(MiniGoParser.LBRACE)
            self.state = 154
            self.array_mem()
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEPARATOR:
                self.state = 155
                self.match(MiniGoParser.SEPARATOR)
                self.state = 156
                self.array_mem()
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 162
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_memContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def structliteral(self):
            return self.getTypedRuleContext(MiniGoParser.StructliteralContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def array_list(self):
            return self.getTypedRuleContext(MiniGoParser.Array_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_mem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_mem" ):
                return visitor.visitArray_mem(self)
            else:
                return visitor.visitChildren(self)




    def array_mem(self):

        localctx = MiniGoParser.Array_memContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_array_mem)
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.structliteral()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 166
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 167
                self.array_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def structfielddecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StructfielddeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StructfielddeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructdecl" ):
                return visitor.visitStructdecl(self)
            else:
                return visitor.visitChildren(self)




    def structdecl(self):

        localctx = MiniGoParser.StructdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_structdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(MiniGoParser.TYPE)
            self.state = 171
            self.match(MiniGoParser.ID)
            self.state = 172
            self.match(MiniGoParser.STRUCT)
            self.state = 173
            self.match(MiniGoParser.LBRACE)
            self.state = 175 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 174
                self.structfielddecl()
                self.state = 177 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.ID):
                    break

            self.state = 179
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructfielddeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typedef(self):
            return self.getTypedRuleContext(MiniGoParser.TypedefContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structfielddecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructfielddecl" ):
                return visitor.visitStructfielddecl(self)
            else:
                return visitor.visitChildren(self)




    def structfielddecl(self):

        localctx = MiniGoParser.StructfielddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_structfielddecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(MiniGoParser.ID)
            self.state = 182
            self.typedef()
            self.state = 184
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructliteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def structfieldliteral(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StructfieldliteralContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StructfieldliteralContext,i)


        def SEPARATOR(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEPARATOR)
            else:
                return self.getToken(MiniGoParser.SEPARATOR, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structliteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructliteral" ):
                return visitor.visitStructliteral(self)
            else:
                return visitor.visitChildren(self)




    def structliteral(self):

        localctx = MiniGoParser.StructliteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_structliteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(MiniGoParser.ID)
            self.state = 187
            self.match(MiniGoParser.LBRACE)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 188
                self.structfieldliteral()
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.SEPARATOR:
                    self.state = 189
                    self.match(MiniGoParser.SEPARATOR)
                    self.state = 190
                    self.structfieldliteral()
                    self.state = 195
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 198
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructfieldliteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def array(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayContext,0)


        def structliteral(self):
            return self.getTypedRuleContext(MiniGoParser.StructliteralContext,0)


        def structfieldliteral(self):
            return self.getTypedRuleContext(MiniGoParser.StructfieldliteralContext,0)


        def var_access(self):
            return self.getTypedRuleContext(MiniGoParser.Var_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structfieldliteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructfieldliteral" ):
                return visitor.visitStructfieldliteral(self)
            else:
                return visitor.visitChildren(self)




    def structfieldliteral(self):

        localctx = MiniGoParser.StructfieldliteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_structfieldliteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(MiniGoParser.ID)
            self.state = 201
            self.match(MiniGoParser.T__0)
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 202
                self.literal()
                pass

            elif la_ == 2:
                self.state = 203
                self.array()
                pass

            elif la_ == 3:
                self.state = 204
                self.structliteral()
                pass

            elif la_ == 4:
                self.state = 205
                self.structfieldliteral()
                pass

            elif la_ == 5:
                self.state = 206
                self.var_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfacedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def method_signature(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Method_signatureContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Method_signatureContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interfacedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfacedecl" ):
                return visitor.visitInterfacedecl(self)
            else:
                return visitor.visitChildren(self)




    def interfacedecl(self):

        localctx = MiniGoParser.InterfacedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_interfacedecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(MiniGoParser.TYPE)
            self.state = 210
            self.match(MiniGoParser.ID)
            self.state = 211
            self.match(MiniGoParser.INTERFACE)
            self.state = 212
            self.match(MiniGoParser.LBRACE)
            self.state = 216 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 213
                self.method_signature()
                self.state = 214
                self.match(MiniGoParser.SEMI)
                self.state = 218 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.ID):
                    break

            self.state = 220
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_signatureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPARENTHESIS(self):
            return self.getToken(MiniGoParser.LPARENTHESIS, 0)

        def RPARENTHESIS(self):
            return self.getToken(MiniGoParser.RPARENTHESIS, 0)

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ArgumentContext,i)


        def typedef(self):
            return self.getTypedRuleContext(MiniGoParser.TypedefContext,0)


        def SEPARATOR(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEPARATOR)
            else:
                return self.getToken(MiniGoParser.SEPARATOR, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_method_signature

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_signature" ):
                return visitor.visitMethod_signature(self)
            else:
                return visitor.visitChildren(self)




    def method_signature(self):

        localctx = MiniGoParser.Method_signatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_method_signature)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(MiniGoParser.ID)
            self.state = 223
            self.match(MiniGoParser.LPARENTHESIS)
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 224
                self.argument()
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.SEPARATOR:
                    self.state = 225
                    self.match(MiniGoParser.SEPARATOR)
                    self.state = 226
                    self.argument()
                    self.state = 231
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 234
            self.match(MiniGoParser.RPARENTHESIS)
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ATOMIC_TYPE) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.ID))) != 0):
                self.state = 235
                self.typedef()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def typedef(self):
            return self.getTypedRuleContext(MiniGoParser.TypedefContext,0)


        def SEPARATOR(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEPARATOR)
            else:
                return self.getToken(MiniGoParser.SEPARATOR, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = MiniGoParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(MiniGoParser.ID)
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEPARATOR:
                self.state = 239
                self.match(MiniGoParser.SEPARATOR)
                self.state = 240
                self.match(MiniGoParser.ID)
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 246
            self.typedef()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def array_index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_indexContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_indexContext,i)


        def field_access(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Field_accessContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Field_accessContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_access" ):
                return visitor.visitVar_access(self)
            else:
                return visitor.visitChildren(self)




    def var_access(self):

        localctx = MiniGoParser.Var_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_var_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(MiniGoParser.ID)
            self.state = 253
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 251
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LBRACKET]:
                        self.state = 249
                        self.array_index()
                        pass
                    elif token in [MiniGoParser.T__1]:
                        self.state = 250
                        self.field_access()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 255
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_field_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_access" ):
                return visitor.visitField_access(self)
            else:
                return visitor.visitChildren(self)




    def field_access(self):

        localctx = MiniGoParser.Field_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_field_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(MiniGoParser.T__1)
            self.state = 257
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_var_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodcall(self):
            return self.getTypedRuleContext(MiniGoParser.MethodcallContext,0)


        def array_index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_indexContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_indexContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_method_var_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_var_access" ):
                return visitor.visitMethod_var_access(self)
            else:
                return visitor.visitChildren(self)




    def method_var_access(self):

        localctx = MiniGoParser.Method_var_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_method_var_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.methodcall(0)
            self.state = 265
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 263
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LBRACKET]:
                        self.state = 260
                        self.array_index()
                        pass
                    elif token in [MiniGoParser.T__1]:
                        self.state = 261
                        self.match(MiniGoParser.T__1)
                        self.state = 262
                        self.match(MiniGoParser.ID)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 267
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_and_method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def method_signature(self):
            return self.getTypedRuleContext(MiniGoParser.Method_signatureContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def method_receiver(self):
            return self.getTypedRuleContext(MiniGoParser.Method_receiverContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_and_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_and_method_decl" ):
                return visitor.visitFunc_and_method_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_and_method_decl(self):

        localctx = MiniGoParser.Func_and_method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_func_and_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(MiniGoParser.FUNC)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LPARENTHESIS:
                self.state = 269
                self.method_receiver()


            self.state = 272
            self.method_signature()
            self.state = 273
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_receiverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPARENTHESIS(self):
            return self.getToken(MiniGoParser.LPARENTHESIS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def RPARENTHESIS(self):
            return self.getToken(MiniGoParser.RPARENTHESIS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_method_receiver

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_receiver" ):
                return visitor.visitMethod_receiver(self)
            else:
                return visitor.visitChildren(self)




    def method_receiver(self):

        localctx = MiniGoParser.Method_receiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_method_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(MiniGoParser.LPARENTHESIS)
            self.state = 276
            self.match(MiniGoParser.ID)
            self.state = 277
            self.match(MiniGoParser.ID)
            self.state = 278
            self.match(MiniGoParser.RPARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def array(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayContext,0)


        def structliteral(self):
            return self.getTypedRuleContext(MiniGoParser.StructliteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ret

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRet" ):
                return visitor.visitRet(self)
            else:
                return visitor.visitChildren(self)




    def ret(self):

        localctx = MiniGoParser.RetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_ret)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(MiniGoParser.RETURN)
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 281
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 282
                self.array()
                pass

            elif la_ == 3:
                self.state = 283
                self.structliteral()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunccallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPARENTHESIS(self):
            return self.getToken(MiniGoParser.LPARENTHESIS, 0)

        def RPARENTHESIS(self):
            return self.getToken(MiniGoParser.RPARENTHESIS, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def SEPARATOR(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEPARATOR)
            else:
                return self.getToken(MiniGoParser.SEPARATOR, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funccall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccall" ):
                return visitor.visitFunccall(self)
            else:
                return visitor.visitChildren(self)




    def funccall(self):

        localctx = MiniGoParser.FunccallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_funccall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(MiniGoParser.ID)
            self.state = 287
            self.match(MiniGoParser.LPARENTHESIS)
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.KEYWORD) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.NOT_OP) | (1 << MiniGoParser.MINUS_OP) | (1 << MiniGoParser.LPARENTHESIS) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.ID))) != 0):
                self.state = 288
                self.expression(0)
                self.state = 293
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.SEPARATOR:
                    self.state = 289
                    self.match(MiniGoParser.SEPARATOR)
                    self.state = 290
                    self.expression(0)
                    self.state = 295
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 298
            self.match(MiniGoParser.RPARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodcallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_access(self):
            return self.getTypedRuleContext(MiniGoParser.Var_accessContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPARENTHESIS(self):
            return self.getToken(MiniGoParser.LPARENTHESIS, 0)

        def RPARENTHESIS(self):
            return self.getToken(MiniGoParser.RPARENTHESIS, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def SEPARATOR(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEPARATOR)
            else:
                return self.getToken(MiniGoParser.SEPARATOR, i)

        def methodcall(self):
            return self.getTypedRuleContext(MiniGoParser.MethodcallContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodcall" ):
                return visitor.visitMethodcall(self)
            else:
                return visitor.visitChildren(self)



    def methodcall(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.MethodcallContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_methodcall, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.var_access()
            self.state = 302
            self.match(MiniGoParser.T__1)
            self.state = 303
            self.match(MiniGoParser.ID)
            self.state = 304
            self.match(MiniGoParser.LPARENTHESIS)
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.KEYWORD) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.NOT_OP) | (1 << MiniGoParser.MINUS_OP) | (1 << MiniGoParser.LPARENTHESIS) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.ID))) != 0):
                self.state = 305
                self.expression(0)
                self.state = 310
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.SEPARATOR:
                    self.state = 306
                    self.match(MiniGoParser.SEPARATOR)
                    self.state = 307
                    self.expression(0)
                    self.state = 312
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 315
            self.match(MiniGoParser.RPARENTHESIS)
            self._ctx.stop = self._input.LT(-1)
            self.state = 334
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.MethodcallContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_methodcall)
                    self.state = 317
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 318
                    self.match(MiniGoParser.T__1)
                    self.state = 319
                    self.match(MiniGoParser.ID)
                    self.state = 320
                    self.match(MiniGoParser.LPARENTHESIS)
                    self.state = 329
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.KEYWORD) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.NOT_OP) | (1 << MiniGoParser.MINUS_OP) | (1 << MiniGoParser.LPARENTHESIS) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.ID))) != 0):
                        self.state = 321
                        self.expression(0)
                        self.state = 326
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==MiniGoParser.SEPARATOR:
                            self.state = 322
                            self.match(MiniGoParser.SEPARATOR)
                            self.state = 323
                            self.expression(0)
                            self.state = 328
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)



                    self.state = 331
                    self.match(MiniGoParser.RPARENTHESIS) 
                self.state = 336
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_access(self):
            return self.getTypedRuleContext(MiniGoParser.Var_accessContext,0)


        def ASSIGN_OP(self):
            return self.getToken(MiniGoParser.ASSIGN_OP, 0)

        def ASSIGN_STMT_OP(self):
            return self.getToken(MiniGoParser.ASSIGN_STMT_OP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def array(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayContext,0)


        def structliteral(self):
            return self.getTypedRuleContext(MiniGoParser.StructliteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MiniGoParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.var_access()
            self.state = 338
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ASSIGN_OP or _la==MiniGoParser.ASSIGN_STMT_OP):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 339
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 340
                self.array()
                pass

            elif la_ == 3:
                self.state = 341
                self.structliteral()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPARENTHESIS(self):
            return self.getToken(MiniGoParser.LPARENTHESIS, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def RPARENTHESIS(self):
            return self.getToken(MiniGoParser.RPARENTHESIS, 0)

        def MINUS_OP(self):
            return self.getToken(MiniGoParser.MINUS_OP, 0)

        def NOT_OP(self):
            return self.getToken(MiniGoParser.NOT_OP, 0)

        def funccall(self):
            return self.getTypedRuleContext(MiniGoParser.FunccallContext,0)


        def methodcall(self):
            return self.getTypedRuleContext(MiniGoParser.MethodcallContext,0)


        def method_var_access(self):
            return self.getTypedRuleContext(MiniGoParser.Method_var_accessContext,0)


        def var_access(self):
            return self.getTypedRuleContext(MiniGoParser.Var_accessContext,0)


        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def KEYWORD(self):
            return self.getToken(MiniGoParser.KEYWORD, 0)

        def MUL_OP(self):
            return self.getToken(MiniGoParser.MUL_OP, 0)

        def DIV_OP(self):
            return self.getToken(MiniGoParser.DIV_OP, 0)

        def MOD_OP(self):
            return self.getToken(MiniGoParser.MOD_OP, 0)

        def ADD_OP(self):
            return self.getToken(MiniGoParser.ADD_OP, 0)

        def COMPARE_OP(self):
            return self.getToken(MiniGoParser.COMPARE_OP, 0)

        def AND_OP(self):
            return self.getToken(MiniGoParser.AND_OP, 0)

        def OR_OP(self):
            return self.getToken(MiniGoParser.OR_OP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 345
                self.match(MiniGoParser.LPARENTHESIS)
                self.state = 346
                self.expression(0)
                self.state = 347
                self.match(MiniGoParser.RPARENTHESIS)
                pass

            elif la_ == 2:
                self.state = 349
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.NOT_OP or _la==MiniGoParser.MINUS_OP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 350
                self.expression(12)
                pass

            elif la_ == 3:
                self.state = 351
                self.funccall()
                pass

            elif la_ == 4:
                self.state = 352
                self.methodcall(0)
                pass

            elif la_ == 5:
                self.state = 353
                self.method_var_access()
                pass

            elif la_ == 6:
                self.state = 354
                self.var_access()
                pass

            elif la_ == 7:
                self.state = 355
                self.literal()
                pass

            elif la_ == 8:
                self.state = 356
                self.match(MiniGoParser.KEYWORD)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 376
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 374
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 359
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 360
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL_OP) | (1 << MiniGoParser.DIV_OP) | (1 << MiniGoParser.MOD_OP))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 361
                        self.expression(12)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 362
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 363
                        _la = self._input.LA(1)
                        if not(_la==MiniGoParser.ADD_OP or _la==MiniGoParser.MINUS_OP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 364
                        self.expression(11)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 365
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 366
                        self.match(MiniGoParser.COMPARE_OP)
                        self.state = 367
                        self.expression(10)
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 368
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 369
                        self.match(MiniGoParser.AND_OP)
                        self.state = 370
                        self.expression(9)
                        pass

                    elif la_ == 5:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 371
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 372
                        self.match(MiniGoParser.OR_OP)
                        self.state = 373
                        self.expression(8)
                        pass

             
                self.state = 378
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_condition(self):
            return self.getTypedRuleContext(MiniGoParser.If_conditionContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BlockContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = MiniGoParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.if_condition()
            self.state = 380
            self.block()
            self.state = 386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 381
                self.match(MiniGoParser.ELSE)
                self.state = 384
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.IF]:
                    self.state = 382
                    self.if_stmt()
                    pass
                elif token in [MiniGoParser.LBRACE]:
                    self.state = 383
                    self.block()
                    pass
                else:
                    raise NoViableAltException(self)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPARENTHESIS(self):
            return self.getToken(MiniGoParser.LPARENTHESIS, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPARENTHESIS(self):
            return self.getToken(MiniGoParser.RPARENTHESIS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_if_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_condition" ):
                return visitor.visitIf_condition(self)
            else:
                return visitor.visitChildren(self)




    def if_condition(self):

        localctx = MiniGoParser.If_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_if_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(MiniGoParser.IF)
            self.state = 389
            self.match(MiniGoParser.LPARENTHESIS)
            self.state = 390
            self.expression(0)
            self.state = 391
            self.match(MiniGoParser.RPARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(MiniGoParser.LBRACE)
            self.state = 395 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 394
                self.statement()
                self.state = 397 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.ID))) != 0)):
                    break

            self.state = 399
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def assignment(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentContext,0)


        def assignment_for(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_forContext,0)


        def vardeclassign(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclassignContext,0)


        def SEPARATOR(self):
            return self.getToken(MiniGoParser.SEPARATOR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def ASSIGN_STMT_OP(self):
            return self.getToken(MiniGoParser.ASSIGN_STMT_OP, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_for_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop" ):
                return visitor.visitFor_loop(self)
            else:
                return visitor.visitChildren(self)




    def for_loop(self):

        localctx = MiniGoParser.For_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_for_loop)
        self._la = 0 # Token type
        try:
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.match(MiniGoParser.FOR)
                self.state = 402
                self.expression(0)
                self.state = 403
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
                self.match(MiniGoParser.FOR)
                self.state = 408
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.ID]:
                    self.state = 406
                    self.assignment_for()
                    pass
                elif token in [MiniGoParser.VAR]:
                    self.state = 407
                    self.vardeclassign()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 410
                self.match(MiniGoParser.SEMI)
                self.state = 411
                self.expression(0)
                self.state = 412
                self.match(MiniGoParser.SEMI)
                self.state = 413
                self.assignment()
                self.state = 414
                self.block()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 416
                self.match(MiniGoParser.FOR)
                self.state = 417
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.T__2 or _la==MiniGoParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 418
                self.match(MiniGoParser.SEPARATOR)
                self.state = 419
                self.match(MiniGoParser.ID)
                self.state = 420
                self.match(MiniGoParser.ASSIGN_STMT_OP)
                self.state = 421
                self.match(MiniGoParser.RANGE)
                self.state = 422
                self.match(MiniGoParser.ID)
                self.state = 423
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN_OP(self):
            return self.getToken(MiniGoParser.ASSIGN_OP, 0)

        def ASSIGN_STMT_OP(self):
            return self.getToken(MiniGoParser.ASSIGN_STMT_OP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def array(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayContext,0)


        def structliteral(self):
            return self.getTypedRuleContext(MiniGoParser.StructliteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_for" ):
                return visitor.visitAssignment_for(self)
            else:
                return visitor.visitChildren(self)




    def assignment_for(self):

        localctx = MiniGoParser.Assignment_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_assignment_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(MiniGoParser.ID)
            self.state = 427
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ASSIGN_OP or _la==MiniGoParser.ASSIGN_STMT_OP):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 431
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 428
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 429
                self.array()
                pass

            elif la_ == 3:
                self.state = 430
                self.structliteral()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(MiniGoParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[26] = self.methodcall_sempred
        self._predicates[28] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def methodcall_sempred(self, localctx:MethodcallContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 7)
         





//ID: 2210134

grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
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
}


options{
	language=Python3;
}


program  : decl+ EOF;

decl: (constdecl | vardecl | vardeclassign | structdecl | interfacedecl | func_and_method_decl) SEMI;

statement: (func_and_method_decl | structdecl | interfacedecl | if_stmt | for_loop | vardecl | vardeclassign | constdecl 
| assignment | ret | funccall | methodcall | method_var_access | BREAK | CONTINUE) SEMI;

typedef: ATOMIC_TYPE | ID | array_type;

constdecl: CONST ID ASSIGN_INIT expression;

vardecl: VAR ID typedef;
vardeclassign
        : VAR ID typedef ASSIGN_INIT (expression | array | structliteral)
        | VAR ID ASSIGN_INIT (expression | array | structliteral);

array: array_type array_list;
array_type: array_index+ (ATOMIC_TYPE | ID);
array_index: LBRACKET (INTEGER | ID) RBRACKET;
array_list: LBRACE array_mem (SEPARATOR array_mem)* RBRACE;
array_mem: literal | structliteral | ID | array_list;

structdecl: TYPE ID STRUCT LBRACE structfielddecl+ RBRACE;
structfielddecl: (ID typedef) SEMI;
structliteral: ID LBRACE (structfieldliteral (SEPARATOR structfieldliteral)*)? RBRACE;
structfieldliteral: ID ':' (literal | array | structliteral | structfieldliteral | var_access);

interfacedecl: TYPE ID INTERFACE LBRACE (method_signature SEMI)+ RBRACE;
method_signature: ID LPARENTHESIS (argument (SEPARATOR argument)*)? RPARENTHESIS typedef?;
argument: ID (SEPARATOR ID)* typedef;

var_access: ID (array_index | field_access)*;


field_access: '.' ID;

method_var_access: methodcall (array_index | '.' ID)*;

func_and_method_decl: FUNC method_receiver? method_signature block;
method_receiver: LPARENTHESIS ID ID RPARENTHESIS;
ret: RETURN (expression | array | structliteral);
funccall: ID LPARENTHESIS (expression (SEPARATOR expression)*)? RPARENTHESIS;
methodcall: methodcall '.' ID LPARENTHESIS (expression (SEPARATOR expression)*)? RPARENTHESIS  
        | var_access '.' ID LPARENTHESIS (expression (SEPARATOR expression)*)? RPARENTHESIS;

assignment: var_access  (ASSIGN_OP | ASSIGN_STMT_OP) (expression | array | structliteral);

expression: LPARENTHESIS expression RPARENTHESIS
    | (MINUS_OP | NOT_OP) expression
    | expression (MUL_OP | DIV_OP | MOD_OP) expression
    | expression (ADD_OP | MINUS_OP) expression  
    | expression COMPARE_OP expression
    | expression AND_OP expression
    | expression OR_OP expression
    | funccall| methodcall | method_var_access | var_access | literal | 'nil';

if_stmt: if_condition block (ELSE (if_stmt | block))?;
if_condition: IF LPARENTHESIS expression RPARENTHESIS;
block: LBRACE statement+ RBRACE;

for_loop
    : FOR expression block
    | FOR (assignment_for | vardeclassign) SEMI expression SEMI assignment block
    | FOR (ID | '_') SEPARATOR ID ASSIGN_STMT_OP RANGE ID block;
assignment_for: ID (ASSIGN_OP | ASSIGN_STMT_OP) (expression | array | structliteral);

fragment BINARY: '0' [bB] [0-1]+;
fragment OCTAL: '0' [oO] [0-7]+;
fragment HEXADEC: '0' [xX] [0-9a-fA-F]+;
fragment DECIMAL: '0' | NonZeroDigit Digit*;
INTEGER: DECIMAL | BINARY | OCTAL | HEXADEC;

ATOMIC_TYPE: ('string' | 'int' | 'float' | 'boolean') {
    if self.inStruct:
        self.afterStatement = True
};
literal: (INTEGER | FLOAT | STRING | BOOLEAN);

// Consider array and structliteral

COMMENT1: '//' ~[\r\n]* -> skip;
COMMENT2: '/*' .* '*/' -> skip;


KEYWORD: 'nil';

VAR: 'var' {
    self.afterStatement = True
};
CONST: 'const' {
    self.afterStatement = True
};
TYPE: 'type';
STRUCT: 'struct' {
    self.inStruct = True
};
INTERFACE: 'interface';
FUNC: 'func';
RETURN: 'return' {
    self.afterStatement = True
};
IF: 'if' {
    self.afterIf = True
};
ELSE: 'else';
FOR: 'for' {
    self.afterFor = True
};
RANGE: 'range';
BREAK: 'break' {
    self.afterStatement = True
};
CONTINUE: 'continue' {
    self.afterStatement = True
};

BOOLEAN: 'true' | 'false';

ASSIGN_OP: ('+=' | '-=' | '*=' | '/=' | '%=') {
    self.afterStatement = True
};
ASSIGN_STMT_OP: ':=' {
    if not self.afterFor:
        self.afterStatement = True
    else:
        self.afterFor = False
};

FLOAT: Digit* '.' Digit* ([eE] ('+'|'-')? Digit*)?;

SEMI: ';' {
    self.afterStatement = False
};

COMPARE_OP: '==' | '!=' | '<' | '<=' | '>' | '>=';
AND_OP: '&&';
OR_OP: '||';
NOT_OP: '!';
ADD_OP: '+';
MINUS_OP: '-';
MUL_OP: '*';
DIV_OP: '/';
MOD_OP: '%';
ASSIGN_INIT: '=';

LPARENTHESIS: '(';
RPARENTHESIS: ')' {
    if not self.afterIf:
        self.afterStatement = True
    else:
        self.afterIf = False
};
LBRACE: '{' {
    self.afterStatement = False
};
RBRACE: '}' {
    self.afterStatement = True
    if self.inStruct:
        self.inStruct = False
};
LBRACKET: '[';
RBRACKET: ']';

SEPARATOR: ',';

ESCAPE: '\\n' | '\\t' | '\\r' | '\\"' | '\\\\';

fragment IN_STRING: (~["\\] | ESCAPE)*;

STRING: '"' IN_STRING '"';

fragment UpperLetter: [A-Z];
fragment LowerLetter: [a-z];
fragment Digit: [0-9];
fragment NonZeroDigit: [1-9];
fragment IdentifierStart: UpperLetter | LowerLetter | '_';
ID: IdentifierStart (IdentifierStart | Digit)* {
    if self.inStruct:
        if not self.idInStruct:
            self.idInStruct = True
        else:
            self.afterStatement = True
};

WS : [ \t\r]+ -> skip ; // skip spaces, tabs 



NL: '\n' {
    if self.afterStatement:
        self.afterStatement = False
        self.type = self.SEMI
        self.text = ";"
        return self.emit()
    self.skip()
}; // skip newlines

ILLEGAL_ESCAPE: '"' IN_STRING '\\' . {
    raise IllegalEscape(self.text)
};
UNCLOSE_STRING: '"' IN_STRING (NL | EOF)  {
    self.text = self.text.split('\r\n')[0]
    raise UncloseString(self.text)
};
ERROR_CHAR: .;
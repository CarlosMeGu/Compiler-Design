from enum import Enum


class TokenType(Enum):
    ENDFILE = 'End of file'
    INT = 'int'
    IF = 'if'
    THEN = 'then'
    ELSE = 'else'
    WHILE = 'while'
    READ = 'read'
    DO = 'do'
    L_PARENTHESIS = 'Left Parenthesis'
    R_PARENTHESIS = 'Right Parenthesis'
    L_BRACE = 'Left Brace'
    R_BRACE = 'Right Brace'
    COMMA = 'coma'
    SEMI_COLON = 'semi colon'
    LT = 'Less than'
    GT = 'Greater than'
    EQ = 'Equal'
    LTEQ = 'Less or equal'
    GTEQ = 'Greater or equal'
    PLUS = 'plus'
    MINUS = 'minus'
    TIMES = 'times'
    DIV = 'division'
    INT_NUM = 'int number'
    ID = 'identifier'
    RETURN = 'return'
    OPEN_MULTI_LINE_COMMENT = 'Open multi line comment'
    CLOSE_MULTI_LINE_COMMENT = 'Close multi line comment'
    ERR = 'error'

class TokenValue(Enum):
    ENDFILE = '$'
    INT = 'int'
    IF = 'if'
    THEN = 'then'
    ELSE = 'else'
    WHILE = 'while'
    READ = 'read'
    DO = 'do'
    L_PARENTHESIS = '('
    R_PARENTHESIS = ')'
    L_BRACE = '{'
    R_BRACE = '}'
    COMMA = ','
    SEMI_COLON = ';'
    LT = '<'
    GT = '>'
    EQ = '='
    LTEQ = '<='
    GTEQ = '>='
    PLUS = '+'
    MINUS = '-'
    TIMES = '*'
    DIV = '/'
    INT_NUM = '^([0-9]+)+$'
    ID = '^([A-Za-z_][A-Za-z0-9_]*)+$'
    RETURN = 'return'
    SPECIAL = '^([|\^&+\-%*/=!$>{}(),]*)+$'
    ONE_LINE_COMMENT = '//'
    OPEN_MULTI_LINE_COMMENT = '/*'
    CLOSE_MULTI_LINE_COMMENT = '*/'

#   /* Expresions for blank spaces in the files*/
# \n  {line++;}
# \t
# \r
# \v
# \f
#
# int					{return INTEGER;}
# if					{return IF;}
# then				{return THEN;}
# else				{return ELSE;}
# while				{return WHILE;}
# read				{return READ;}
# write				{return WRITE;}
# do          {return DO;}
#   /* These are the definitions for puntuation symbols, we could combine them in one with various | but I decided to seperate them. */
# \(					{return LPAREN;}
# \)					{return RPAREN;}
# \{					{return LBRACE;}
# \}					{return RBRACE;}
# ,					{return COMMA;}
# ;					{return SEMI;}
#   /* These are the definitions for relational symbols, we could combine them in one with various | but I decided to seperate them. */
# \<					{return LT;}
# =					{return EQ;}
# \<=					{return LTEQ;}
# \>=					{return MTEQ;}
# !=					{return NEQ;}
#   /* These are the definitions for arithmetic and logical symbols, we could combine them in one with various | but I decided to seperate them. */
# \+					{return PLUS;}
# -					{return MINUS;}
# \*					{return TIMES;}
# \/					{return DIV;}
#   /* These are the definitions for number symbols, we could combine them in one with various | but I decided to seperate them. */
# [0-9][0-9]*			{return INT_NUM;}
#   /* These are the definitions for Identifier symbols, we could combine them in one with various | but I decided to seperate them. */
# [A-Za-z_][A-Za-z0-9_]*						{yylval.stringVal = strdup(yytext);;return ID;}
#   /* These are the definitions for comment symbols, we could combine them in one with various | but I decided to seperate them. */
# "/*"((("*"[^/])?)|[^*])*"*/"				{for(int i = 0; i<strlen(yytext);i++){if(yytext[i]=='\n')line++;}}
# "//".*
#   /* Expresions for blank spaces in the files*/
# \n  {line++;}
# \t
# \r
# \v
# \f
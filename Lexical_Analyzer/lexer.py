from globalTypes import *
import re


def globales(prog, pos, long):
    global programa
    global posicion
    global progLong
    programa = prog
    posicion = pos
    progLong = long


def getToken(imprime=True):
    intPattern = re.compile('^([0-9]+)+$')
    idPattern = re.compile('^([A-Za-z_][A-Za-z0-9_]*)+$')
    specialPattern = re.compile('[@_!#$%^&*()<,;>?/\|\-}{~:]')
    actualPosicion = posicion
    stop = False
    tokenString = programa[actualPosicion]
    token = ''
    while not stop:
        if programa[actualPosicion] == '$' or programa[actualPosicion] == ' ' or programa[actualPosicion] == '\n':
            stop = True
            if programa[actualPosicion] == '$':
                token = TokenType.ENDFILE.value
            else:
                tokenString = tokenString[:-1]
                if idPattern.match(tokenString):
                    token = TokenType.ID.value
                elif intPattern.match(tokenString):
                    token = TokenType.INT.value
                else:
                    token = TokenType.ERR.value
            actualPosicion += 1
        else:
            if tokenString == TokenValue.INT.value:
                token = TokenType.INT.value
            elif tokenString == TokenValue.IF.value:
                token = TokenType.IF.value
            elif tokenString == TokenValue.THEN.value:
                token = TokenType.THEN.value
            elif tokenString == TokenValue.ELSE.value:
                token = TokenType.ELSE.value
            elif tokenString == TokenValue.WHILE.value:
                token = TokenType.WHILE.value
            elif tokenString == TokenValue.READ.value:
                token = TokenType.READ.value
            elif tokenString == TokenValue.DO.value:
                token = TokenType.DO.value
            elif tokenString == TokenValue.L_PARENTHESIS.value:
                token = TokenType.L_PARENTHESIS.value
            elif tokenString == TokenValue.R_PARENTHESIS.value:
                token = TokenType.R_PARENTHESIS.value
            elif tokenString == TokenValue.L_BRACE.value:
                token = TokenType.L_BRACE.value
            elif tokenString == TokenValue.R_BRACE.value:
                token = TokenType.R_BRACE.value
            elif tokenString == TokenValue.COMMA.value:
                token = TokenType.COMMA.value
            elif tokenString == TokenValue.SEMI_COLON.value:
                token = TokenType.SEMI_COLON.value
            elif tokenString == TokenValue.LT.value:
                token = TokenType.LT.value
            elif tokenString == TokenValue.GT.value:
                token = TokenType.GT.value
            elif tokenString == TokenValue.EQ.value:
                token = TokenType.EQ.value
            elif tokenString == TokenValue.LTEQ.value:
                token = TokenType.LTEQ.value
            elif tokenString == TokenValue.GTEQ.value:
                token = TokenType.GTEQ.value
            elif tokenString == TokenValue.PLUS.value:
                token = TokenType.PLUS.value
            elif tokenString == TokenValue.MINUS.value:
                token = TokenType.MINUS.value
            elif tokenString == TokenValue.TIMES.value:
                token = TokenType.TIMES.value
            elif tokenString == TokenValue.DIV.value:
                token = TokenType.DIV.value
            elif tokenString == TokenValue.INT_NUM.value:
                token = TokenType.INT_NUM.value
            elif specialPattern.search(tokenString):
                #print('Encontre un caracter especial en: ', tokenString)
                tokenString = tokenString[:-1]
                if idPattern.match(tokenString):
                    token = TokenType.ID.value
                    actualPosicion -= 1
                elif intPattern.match(tokenString):
                    token = TokenType.ID.value
                    actualPosicion -= 1



            actualPosicion += 1
            if token != '':
                stop = True
            else:
                tokenString += programa[actualPosicion]

    if imprime and not tokenString == ' ' and not tokenString == '\n' and not tokenString == '':
        print(token, " = ", tokenString )

    globales(programa, actualPosicion, progLong)

    return token, tokenString

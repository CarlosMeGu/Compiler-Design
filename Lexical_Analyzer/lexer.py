from globalTypes import  *


def globales(prog, pos, long):
    global programa
    global posicion
    global progLong
    programa = prog
    posicion = pos
    progLong = long


def getToken(imprime=True):
    actualPosicion = posicion
    stop = False
    tokenString = programa[actualPosicion]
    token = ''
    while not stop:
        if programa[actualPosicion] == ' ' or programa[actualPosicion] == '$':
            stop = True
            if programa[actualPosicion] == '$':
                token = TokenType.ENDFILE

            actualPosicion += 1

        else:
            token = TokenType.OTHER
            actualPosicion += 1
            tokenString += programa[actualPosicion]

    if imprime and not tokenString == ' ':
        print(token, " = ", tokenString)

    globales(programa, actualPosicion, progLong)

    return token, tokenString

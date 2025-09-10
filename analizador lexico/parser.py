# parser.py
from lexer import scan

# Gramática:
# 1) E → E * E
# 2) E → E + E
# 3) E → id

producciones = {
    1: ("E", ["E", "*", "E"]),
    2: ("E", ["E", "+", "E"]),
    3: ("E", ["id"])
}

# Tabla LR(0)
# Formato: action[(estado, token)] = ("s", destino) / ("r", num_prod) / ("acc")
#          goto[(estado, NoTerminal)] = destino
action = {
    (0, 0): ("s", 5),   # id
    (1, 1): ("s", 2),   # *
    (1, 2): ("s", 3),   # +
    (1, 3): ("acc",),   # $
    (2, 0): ("s", 5),
    (3, 0): ("s", 5),
    (4, 1): ("r", 1),   # E → E * E
    (4, 2): ("r", 1),
    (4, 3): ("r", 1),
    (5, 1): ("r", 3),   # E → id
    (5, 2): ("r", 3),
    (5, 3): ("r", 3),
    (6, 1): ("r", 2),   # E → E + E
    (6, 2): ("r", 2),
    (6, 3): ("r", 2),
}

goto = {
    (0, "E"): 1,
    (2, "E"): 4,
    (3, "E"): 6,
}

def parse(tokens):
    """
    tokens: lista de enteros [0=id,1=*,2=+,3=$]
    """
    stack = [0]  # pila de estados
    pos = 0

    while True:
        estado = stack[-1]
        token = tokens[pos]

        if (estado, token) not in action:
            raise SyntaxError(f"Error de sintaxis en token {token}, estado {estado}")

        act = action[(estado, token)]

        if act[0] == "s":  # shift
            stack.append(token)
            stack.append(act[1])  # nuevo estado
            pos += 1

        elif act[0] == "r":  # reduce
            num = act[1]
            lhs, rhs = producciones[num]
            n = len(rhs) * 2
            for _ in range(n):
                stack.pop()
            estado = stack[-1]
            stack.append(lhs)
            if (estado, lhs) not in goto:
                raise SyntaxError(f"Error de goto en estado {estado}, símbolo {lhs}")
            stack.append(goto[(estado, lhs)])
            print(f"Reduciendo con {num}: {lhs} → {' '.join(rhs)}")

        elif act[0] == "acc":
            print("Cadena aceptada ✔")
            return True

if __name__ == "__main__":
    # Ejemplo: id + id * id $
    entrada = "a + b * c $"
    tokens = []
    for t in scan(entrada):
        if t.lexema == "id" or t.tipo == 0:  # identificador
            tokens.append(0)
        elif t.lexema == "*":
            tokens.append(1)
        elif t.lexema == "+":
            tokens.append(2)
        elif t.lexema == "$":
            tokens.append(3)
    print("Tokens:", tokens)
    parse(tokens)

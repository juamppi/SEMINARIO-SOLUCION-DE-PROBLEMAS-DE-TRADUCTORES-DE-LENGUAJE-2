from pila import Pila
from estado import Estado
from terminal import Terminal
from noterminal import NoTerminal

if __name__ == "__main__":
    pila = Pila()

    pila.push(Estado(0))
    pila.push(Terminal("id"))
    pila.push(Estado(2))
    pila.push(Terminal("+"))
    pila.push(Estado(3))
    pila.push(NoTerminal("E"))
    pila.push(Estado(5))

    print("Contenido de la pila:", pila)

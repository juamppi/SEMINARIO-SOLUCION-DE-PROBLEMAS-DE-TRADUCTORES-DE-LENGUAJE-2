# clases_derivadas.py

from abc import ABC, abstractmethod


# Clase base abstracta
class ElementoPila(ABC):
    @abstractmethod
    def __str__(self):
        pass


# Clase Terminal
class Terminal(ElementoPila):
    def __init__(self, simbolo: str):
        self.simbolo = simbolo

    def __str__(self):
        return self.simbolo


# Clase NoTerminal
class NoTerminal(ElementoPila):
    def __init__(self, simbolo: str):
        self.simbolo = simbolo

    def __str__(self):
        return self.simbolo

# Clase Estado
class Estado(ElementoPila):
    def __init__(self, numero: int):
        self.numero = numero

    def __str__(self):
        return str(self.numero)


# Clase Pila
class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, elemento: ElementoPila):
        self.elementos.append(elemento)

    def pop(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        return None

    def cima(self):
        if not self.esta_vacia():
            return self.elementos[-1]
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0

    def __str__(self):
        return "".join(str(e) for e in self.elementos)


# uso
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

from elemento_pila import ElementoPila

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

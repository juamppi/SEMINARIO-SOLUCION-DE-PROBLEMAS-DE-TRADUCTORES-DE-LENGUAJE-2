from elemento_pila import ElementoPila

class Terminal(ElementoPila):
    def __init__(self, simbolo: str):
        self.simbolo = simbolo

    def __str__(self):
        return self.simbolo

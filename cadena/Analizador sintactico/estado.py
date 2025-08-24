from elemento_pila import ElementoPila

class Estado(ElementoPila):
    def __init__(self, numero: int):
        self.numero = numero

    def __str__(self):
        return str(self.numero)

valores = ["hola", "9", "9.8", "10", "mundo"]

for valor in valores:
    try:
        
        numero = int(valor)
        print(f"{valor} int")
    except ValueError:
        try:
          
            numero = float(valor)
            print(f"{valor} real")
        except ValueError:
            
            print(f"{valor} str")

"""

# cadena2.py
import sys
from lexer import scan
from parser import parse

def main():
    if len(sys.argv) < 2:
        print("Uso: python cadena2.py \"<codigo>\"")
        return
    
    codigo = sys.argv[1]
    tokens = scan(codigo)
    print("Tokens generados:", tokens)
    
    # Ahora pasamos los tokens al parser
    aceptado = parse(tokens)
    if aceptado:
        print("Cadena aceptada")
    else:
        print("Cadena rechazada")

if __name__ == "__main__":
    main()
"""
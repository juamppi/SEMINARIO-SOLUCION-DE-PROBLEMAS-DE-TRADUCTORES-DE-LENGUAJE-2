valores = ["hola", "9", "9.8", "10", "mundito"]

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

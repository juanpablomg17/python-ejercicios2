

def main():
  

    precio = float(input("¿Cuánto cuesta 1 segundo de llamada?: "))
    n = int(input("¿Cuántas comunicaciones hubo?: "))
    for i in range(n):
        hs = float(input("¿Cuántas horas?: "))
        min = float(input("¿Cuántos minutos?: "))
        seg = float(input("¿Cuántos segundos?: "))
        totalsegundos = segundos(hs, min, seg)
        costo = totalsegundos * precio
        print("En la otra llamada que Realizó...")
    
    print ("Duracion: ", totalsegundos, "segundos. Costo: ",costo, "$.")

def segundos (horas, minutos, segundos):
    segsal = 3600 * horas + 60 * minutos + segundos
    return segsal

main()

    

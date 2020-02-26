
def convertir(pesos):
    bitcoin = pesos* 2.9e-8
    dolares = pesos * 0.00029
    euro = pesos * 0.00027

    print(" $", pesos, "colombiados son: ",bitcoin, "bitcoins")
    print(" $", pesos, "colombiados son: ",dolares, "dolares")
    print(" $", pesos, "colombiados son: ",euro, "euros")








def validar():
    correcto = False

    while (not correcto):
        
        try:
            pesos = float(input("Digite la cantidad de pesos que desea convertir: "))
            if(pesos > 0):
                convertir(pesos)

                correcto = True
            else:
                print("La cantidad Ingresada debe ser mayor que 0")
                correcto = False
            

            
        except ValueError:
            print("La cantidad ingresada debe ser del tipo numérica")


validar()
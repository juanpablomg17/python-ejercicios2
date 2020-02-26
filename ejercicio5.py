
def organizarN(n1,n2,n3):
  if ((n1!=n2) and (n1!=n3) and (n2!=n3)):    
    if ((n1 < n2) and (n2 < n3) ):
        print(n1, " ", n2," ",n3)
    if ((n1 < n3) and (n3 <n2)):
        print(n1, " ", n3," ",n2)
    if ((n2 < n1) and (n1 <n3)):
        print(n2, " ", n1," ",n3)
    if ((n2 < n3) and (n3 < n1)):
        print(n2, " ", n3," ",n1)
    if ((n3 < n1) and (n1 < n2)):
        print(n3, " ", n1," ",n2)
    if ((n3 < n2) and (n2 < n1)):
        print(n3, " ", n2," ",n1)
  else:
      print("los números deben ser diferentes")
    


def validar():
    correcto = False
    while (not correcto):
        try:
            print("PROGRAMA PARA ORGANIZAR NÚMEROS DE FORMAR ASCENDENTE")
            n1 = float(input("digite el prinmer número: "))
            n2 = float(input("digite el segundo número: "))
            n3 = float(input("digite el tercer  número: "))
            organizarN(n1,n2,n3)
            correcto = True
        except ValueError:
            print("la entrada debe ser de tipo numérica")



validar()

        

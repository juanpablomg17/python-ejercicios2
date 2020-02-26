def numerosTriangulares(n):
 
    b = 1

    for i in range(1,n+1,1):
 
        
        print(i, "--->",b )
        b = i + b +1
   
 


def validar():
    correcto= False

    while(not correcto):
        try:
            n = int(input("Introduce el número de triángulos "))
            numerosTriangulares(n)

            correcto = True
        
        except ValueError:
            print("El valor introducido debe ser un número entero")

    


validar()





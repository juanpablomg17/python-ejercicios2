

def numeropares(n1,n2):
  
   for i  in range(n1,n2+1):
           if ((i%2) == 0):
               print(i)
pass


def pedirNumeroEntero():
 
    correcto=False
    
    while(not correcto):
        try:
            n1 = int(input("Introduce un numero entero: "))
            n2 = int(input("Introduce un número entero: "))
            numeropares(n1,n2)
            correcto=True

            
        except ValueError:
            print('Error, introduce un numero entero')
     
    return correcto
    pass


pedirNumeroEntero()






















       



             
                
               
            
         
            
            
    


    

       

            




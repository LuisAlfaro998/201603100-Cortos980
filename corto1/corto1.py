#--------------------------CORTO 1--------------------------------------------
#LUIS ALBERTO ALFARO HEREDIA--------------------------------------------------
#201603100--------------------------------------------------------------------

def collat(n):                  #se crea una funcion para solo llamarla despues
    numeros=[]
    while n>1:
        if (n%2==0):                 #se revisa si el numero n es par o no
            n=n/2                    #si es par se divide netre 2
            numeros.append(n)        #guarda los valores de n
        else:
            n=3*n+1
            numeros.append(n)
    print(numeros)
    archivo = open('collatz.txt','w')
    archivo.writelines(str(numeros))
    archivo.close()
    return(numeros)

                      #ultimos 3 digitos de mi carnet
x=100
for i in range(2,x):
    collat(i)
    
    #for linea in archivo:
    
    


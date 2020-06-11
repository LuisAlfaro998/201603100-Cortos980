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
    archivo = open('collatz.txt','w') #remplazar 'w' por 'a'. Cada vez que es llamada la funcion se sobreescribe el archivo
    archivo.writelines(str(numeros))  #por lo tanto el archivo solo tendra la ultima secuencia
    archivo.close()
    return(numeros)

                      #ultimos 3 digitos de mi carnet
x=100
for i in range(2,x):
    collat(i)
    
    #for linea in archivo:
    
#Funcionamiento:        30/40 no agrega todas las secuencias en el archivo
#Uso de Funciones       20/20
#Manejo de archivos     10/10
#Manejo de Listas       10/10
#Uso de git             20/20
#*****************************
#Total                  90/100



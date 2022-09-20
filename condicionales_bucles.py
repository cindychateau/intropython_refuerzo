#Condicionales
x = 2
if x < 10:
    print("Menor a 10")
    print("Otra cosa")
else:
    print("Mayor a 10")

x = 27
if x < 10:
    print("Menor a 10")
elif x > 25:
    print("Mayor a 25")
else:
    print("Número entre 10 y 25")


llueve = False
soleado = True

if(llueve):
    print("Lleva un paraguas")
elif(soleado):
    print("Ponte bloqueador")
else:
    print("Disfruta tu día")

llueve = True
if(llueve and soleado): #Estamos buscando que tanto llueva como soleado sean verdaderos
    print("Busca el arcoiris")


soleado = False
if(llueve or soleado): #Si cumplimos con cualquiera de las dos
    print("Aunque llueve o haga mucho sol estamos contentos")


#Ciclos/Bucles
for i in range(5): #0 - 4. Avanzando de 1 en 1
    print(i)

print("------")

for i in range(2, 5): #2 - 4, Avanzando de 1 en 1. Primer valor es dónde comenzar, segundo valor dónde acabar
    print(i)

print("------")
for i in range(2, 10, 3): #Comienzo, Parada, Cantidad a avanzar
    print(i)

print("------")
for i in range(20, 0, -5): 
    print(i)


#Podemos recorrer textos
string = "Buenos días"
for letra in string:
    print(letra)


arreglo1 = ['A', 'B', 'C', 'D']
for elemento in arreglo1:
    print(elemento)

gastos = [10, 20, 30, 10]
total = 0
for gasto in gastos:
    total += gasto #total = total + gasto
    print(gasto)

print(total)

diccionario = {"nombre": "Elena", "apellido":"De troya", "edad":30}
for llave in diccionario:
    #print(llave, diccionario[llave])
    print(diccionario[llave])
    #print('--')

arreglo2 = ["F", "G", "H", "I"]
for i in range(len(arreglo2)): #Menor al tamaño total de mi arreglo2
    print(i, arreglo2[i]) #Imprimiendo la posición e imprimiendo el valor
#Una función es un bloque de código que podemos ejecutar las veces que nosotros queramos siempre y cuando la mandemos llamar
def hola():
    print("Hola a todos")

def holaReturn():
    return "Hola, este es un return"

hola()

texto = holaReturn() #texto = "Hola, este es un return"
texto = texto.upper()
print(texto)
print(holaReturn()) #print("Hola, este es un return")

def sumatoria(num1, num2): #num1 = 3, num2 = 4
    return num1 + num2 # 3 + 4 = 7. RETURN 7

suma = sumatoria(3, 4) #suma = 7
print(suma)

#RETO 1 - Crear una función sumatoriaArray que va recibir un arreglo/lista y va a regresar la sumatoria de todos los elementos del arreglo
#arreglo = [2, 3, 4, 5]
#total = 0
#numero = 2
#total = 2

#numero = 3
#total = 2 + 3 = 5

#numero = 4
#total = 5 + 4 = 9

#numero = 5
#total = 9 + 5 = 14
#RETURN 14
def sumatoriaArray(arreglo):
    total = 0

    for numero in arreglo:
        total += numero
    
    return total

total_sumatoria = sumatoriaArray([2, 3, 4, 5]) #total_sumatoria = 14
print(total_sumatoria)

#RETO 2 - Crear una función que reciba un arreglo y que me regrese el promedio de los elementos del arreglo. promedioArray(arreglo)
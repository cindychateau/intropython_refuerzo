#Para ejecutar el archivo usamos:
#python3 nombre_archivo.py
#py nombre_archivo.py
#python nombre_archivo.py

#Booleans
boolean = True #True o False

#Numerales
num = 10
fl = 10.50

nuevo_flotante = float(10)
nuevo_entero = int(10.50)

print(nuevo_flotante)
print(nuevo_entero)

#Cadena/Texto/String
string = "ABCDEFG"
print("Este es el abecedario:", string) #la coma en automático me agrega un espacio entre texto y texto
print("Este es el abecedario:"+ string) #Me concatena las cadenas tal cual están
print("Este es un número", num) #Todo lo que va después de la coma lo transforma en texto
print("Este es un número "+str(num)) #Transformo mi número en string/texto

print("Este es el alfabeto '"+string+"'. ")
print(f"Este es el alfabeto '{string}'. ")

#Métodos que pudieran servir para los textos
texto = "hola mundo! soy Elena de Troya y hoy en 19 de Septiembre"
print(texto.title()) #Todas las primeras letras se vuelve mayúsculas
print(texto.upper()) #Todas las letras las hace mayúsculas
print(texto.lower()) #Todas minúsculas
print(texto.count('oy')) #Regresar cuántos 'oy' hay en el texto
print(texto.find('Elena')) #Devuelve dónde comienza 'Elena'. Regresa -1 si no encuentra la palabra. OJO es case sensitive

division = texto.split("!")
print(division)
print(division[0].upper(), division[1].lower())


#Tuplas -> Lista que NO se puede modificar
tupla = (1, 2, 3, 4)
print(tupla[0])

#Listas/Arreglos/Arrays
lista_vacia = []
lista_llena = ["Elena", "Juana", "Pablo"]
lista_llena.append("Pedro")
print(lista_llena)
print(lista_llena[0])
lista_llena.pop() #Elimina el último dato de mi lista
print(lista_llena)
lista_llena.pop(0)
print(lista_llena)

lista_mix = ["Texto1", "Texto2", 1, 1.1, ["Elemento1", "Elemento2"]] #Mis listas pueden guardar cualquier tipo de dato
print(lista_mix)

#Diccionarios
persona = {"nombre": "Elena", "apellido": "De Troya", "edad":30, "soltero": False}
print(persona)
print(persona['nombre'])
persona['estatura'] = 1.65
print(persona)
persona['hobbies'] = ['leer', 'ver tele', 'jugar videojuegos']
print(persona)
persona.pop("estatura") #Eliminamos la llave 'estatura' y su valor
print(persona)

lista_alumnos = [
    {"nombre": "Elena", "apellido": "De Troya", "id": 123, "cursos": ["Fundamentos de la Web", "Python"]},
    {"nombre": "Juana", "apellido": "De Arco", "id": 234, "cursos": ["Fundamentos de la Web", "Python", "MERN"]},
    {"nombre": "Pedro", "apellido": "Páramo", "id": 345, "cursos": ["Fundamentos de la Web", "Python", "MERN", "Java"]}
]

#¿Cómo eliminamos de la lista de cursos de PEDRO el de MERN?
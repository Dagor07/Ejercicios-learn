import random

# 🔴 Nivel Avanzado
# Validar contraseña segura
# Escribe una función que valide si una contraseña cumple con requisitos de seguridad (mayúsculas, minúsculas, números y símbolos).
def es_contrasena_segura(contrasena: str):
    mayuscula = False
    minuscula = False
    numero = False
    simbolo = False

    for caracter in contrasena:
        if caracter.isupper():
            mayuscula = True
        elif caracter.islower():
            minuscula = True
        elif caracter.isdigit():
            numero = True
        else:
            if not caracter.isspace():
                simbolo = True

    if mayuscula and minuscula and numero and simbolo:
        return True
    else:
        return False
print(es_contrasena_segura("Hola1/"))


# Simular dado
# Crea una función que simule el lanzamiento de un dado de 6 caras.
def lanzar_dado():
    return random.randint(1, 6)

# Suma de elementos únicos
# Escribe una función que reciba una lista de números y devuelva la suma de los elementos únicos.
def suma_unicos(lista):
    return sum([x for x in lista if lista.count(x) == 1])
# Generador de contraseñas
# Crea una función que genere una contraseña aleatoria de una longitud dada.
import random

def passwordgenerator(length):
    if length < 4:
        return "La contraseña debe tener al menos 4 caracteres."
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
    simbolos = "!#$%&/()=?¡+*[]}{-.,<>~|"
    todos = minusculas + mayusculas + numeros + simbolos
    password = ''.join(random.choice(todos) for _ in range(length))
    return password
# Composición de funciones
# Escribe una función que reciba otra función como parámetro y aplique una composición de funciones.
def componer(func1,func2, valor):
    return func1(func2(valor))


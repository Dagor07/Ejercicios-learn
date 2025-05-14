import random

# 🔴 Nivel Avanzado
# Validar contraseña segura
# Escribe una función que valide si una contraseña cumple con requisitos de seguridad (mayúsculas, minúsculas, números y símbolos).
def is_password_secure(password: str):
    upper = False
    lower = False
    number = False
    symbol = False

    for character in password:
        if character.isupper():
            upper = True
        elif character.islower():
            lower = True
        elif character.isdigit():
            number = True
        else:
            if not caracter.isspace():
                symbol = True

    if upper and lower and number and symbol:
        return True
    else:
        return False

# Simular dado
# Crea una función que simule el lanzamiento de un dado de 6 caras.
def roll_dice():
    return random.randint(1, 6)

# Suma de elementos únicos
# Escribe una función que reciba una lista de números y devuelva la suma de los elementos únicos.
def single_sum(list):
    return sum([x for x in list if list.count(x) == 1])
# Generador de contraseñas
# Crea una función que genere una contraseña aleatoria de una longitud dada.
import random

def passwordgenerator(length):
    if length < 4:
        return "La contraseña debe tener al menos 4 caracteres."

    # Definir manualmente los caracteres
    lowers = "abcdefghijklmnopqrstuvwxyz"
    uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!#$%&/()=?¡+*[]}{-.,<>~|"

    All = lowers + uppers + numbers + symbols

    # Generar contraseña aleatoria
    password = ''.join(random.choice(All) for _ in range(length))
    return password
# Composición de funciones
# Escribe una función que reciba otra función como parámetro y aplique una composición de funciones.
def componer(func1,func2, value):
    return func1(func2(value))


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
print(es_contrasena_segura("holA/246 "))


# Simular dado
# Crea una función que simule el lanzamiento de un dado de 6 caras.

# Suma de elementos únicos
# Escribe una función que reciba una lista de números y devuelva la suma de los elementos únicos.

# Generador de contraseñas
# Crea una función que genere una contraseña aleatoria de una longitud dada.

# Composición de funciones
# Escribe una función que reciba otra función como parámetro y aplique una composición de funciones.


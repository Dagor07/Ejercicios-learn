# Saludo personalizado
# Crea una función que reciba un nombre y muestre un saludo personalizado.

def greeting(name):
    if name.strip() != "":
        print(f"Hello, {name.strip()}! Welcome.")
    else:
        print("Please enter a valid name.")

# Suma de dos números
# Escribe una función que reciba dos números y devuelva su suma.

add = lambda a, b: float(a) + float(b)

# Número par o impar
# Crea una función que determine si un número es par o impar.

even_or_odd = lambda n: "Even" if int(n) % 2 == 0 else "Odd"

# Mayoría de edad
# Escribe una función que reciba una edad y devuelva si es mayor o menor de edad.
def is_adult(age):
    try:
        age = int(age)
        if age >= 18:
            return "Adult"
        elif age >= 0:
            return "Minor"
        else: 
            return "Error: Age cannot be negative."
    except:
        return "Error: Please enter a valid age."


# Conversor de temperatura
# Crea una función que convierta grados Celsius a Fahrenheit

celsius_to_fahrenheit = lambda c: (float(c) * 9/5) + 32

# Área de un triángulo
# Escribe una función que devuelva el área de un triángulo dado su base y altura.

triangle_area = lambda base, height: (float(base) * float(height)) / 2

# Mayor de una lista
# Crea una función que reciba una lista de números y devuelva el mayor.
def max_in_list(numbers):
    try:
        num_list = [float(n) for n in numbers]
        if len(num_list) == 0:
            return "List is empty."
        return max(num_list)
    except:
        return "Error: The list must contain only numbers."


# Contar letras
# Escribe una función que cuente cuántas veces aparece una letra en una palabra.
count_letters = lambda word, letter: word.count(letter) if len(letter) == 1 else "Only one letter allowed"



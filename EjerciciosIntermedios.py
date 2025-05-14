# 🟡 Nivel Intermedio
# Filtrar pares
# Crea una función que reciba una lista de números y devuelva solo los pares.

def filter_even(numbers):
    try:
        result = [int(n) for n in numbers if int(n) % 2 == 0]
        return result
    except:
        return "Error: The list must contain only numbers."


# Palíndromo
# Escribe una función que determine si un texto es un palíndromo.

def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


# Factorial
# Crea una función que calcule el factorial de un número entero positivo.

def factorial(n):
    try:
        n = int(n)
        if n < 0:
            return "Error: Number must be positive."
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    except:
        return "Error: Enter a valid integer."

# Eliminar duplicados
# Escribe una función que reciba una lista y devuelva una nueva sin elementos repetidos.

def remove_duplicates(lst):
    try:
        return list(dict.fromkeys(lst))  # maintains the original order
    except:
        return "Error: Input must be a list."


# FizzBuzz
# Crea una función que reciba un número y devuelva "Fizz", "Buzz" o "FizzBuzz" según las reglas del juego.

def fizzbuzz(n):
    try:
        n = int(n)
        if n % 3 == 0 and n % 5 == 0:
            return "FizzBuzz"
        elif n % 3 == 0:
            return "Fizz"
        elif n % 5 == 0:
            return "Buzz"
        else:
            return n
    except:
        return "Error: Enter a valid integer."

# Contar vocales
# Escribe una función que reciba una cadena y devuelva la cantidad de vocales.

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for i in text if i in vowels)
print(count_vowels("palabraaaaa"))
# Invertir texto
# Crea una función que invierta una cadena de texto.

def invert_text(text):
    return text[::-1]

print("variables y tipos de variables")

enteros = 10 # Números sin decimales.
print(f"{enteros} es", type(enteros)) 

decimal = 36.5 # Números con decimales.
print(f"{decimal} es", type(decimal)) 

numero_complejo = 3 + 4j # Tienen una parte real y una imaginaria.
print(f"{numero_complejo} es", type(numero_complejo))

texto = "Hola, Mundo" # Cadenas de texto encerradas entre comillas simples ' o dobles "
print(f"{texto} es", type(texto))

verdad = True # Representan valores de verdadero (True) o falso (False)
print(f"{verdad} es", type(verdad))

falso = False # Representan valores de verdadero (True) o falso (False)
print(f"{falso} es", type(falso))

lista = [1, 2, 3, "manzana", "uva"] # Colección ordenada de elementos (pueden ser de tipos diferentes).
print(f"{lista} es", type(lista))

tuplas = (10, 20, 30, 30, "Alo") # Similar a las listas, pero son inmutables (no se pueden modificar).
print(f"{tuplas} es", type(tuplas))

elset = {1, 2, 3, 3} # Colección de elementos únicos (sin orden).
print(f"{elset} es", type(elset))

diccionario = { # Colección de pares clave-valor.
    "nombre": "Mario",
    "edad": 30,
    "mayor_de_edad": True
}
print(f"{diccionario} es", type(diccionario))

sin_valor = None # Representa la ausencia de un valor.
print(f"{sin_valor} es", type(sin_valor))


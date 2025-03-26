# 1. Dada la siguiente lista, imprime sus elementos en orden inverso
nombres = ["Fulano", "Mengano", "Zutano"]
print("Elementos en orden inverso:", nombres[:: -1])

# 2. El usuario escribe un nombre por consola
nombre_buscar = str(input("NOMBRE: "))

# 3. El nombre escrito por el usuario es buscado con un bucle en la lista
# - Si el nombre está en la lista, "{nombre_buscar} encontrado"
# - Si el nombre no está en la lista, "{nombre_buscar} no encontrado"
if nombre_buscar in nombres:
    print(f"{nombre_buscar} encontrado")
else:
    print(f"{nombre_buscar} no encontrado")

# 4. Crea un diccionario, cuya clave sea el nombre de cada uno, y el valor su edad (te la inventas)
edades = {
    "Fulano": 30,
    "Mengano": 25,
    "Zutano": 20
}

# 5. Muestra por pantalla la edad del último elemento de la lista
# IMPORTANTE: desconocemos la cantidad, por lo que no es correcto utilizar el 2 para Zutano.
ultimo_nombre = nombres[-1]
print(f"La edad de {ultimo_nombre} es {edades[ultimo_nombre]}")
# 3. El nombre escrito por el usuario es buscado con un bucle en la lista
# - Si el nombre está en la lista, "{nombre_buscar} encontrado"
# - Si el nombre no está en la lista, "{nombre_buscar} no encontrado"
if nombre_buscar in nombres: # type: ignore
    print(f"{nombre_buscar} encontrado") # type: ignore
else:
    print(f"{nombre_buscar} no encontrado") # type: ignore


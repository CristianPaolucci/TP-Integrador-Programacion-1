# Insertion Sort para ordenar nombres
def insertion_sort(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and actual.lower() < lista[j].lower():
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista

# Búsqueda lineal
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i].lower() == objetivo.lower():
            return i
    return -1

# Búsqueda binaria
def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1
    objetivo = objetivo.lower()
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio].lower() == objetivo:
            return medio
        elif lista[medio].lower() < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Lista pequeña de autores
autores = ["Cortázar", "Borges", "Neruda", "Paz", "García Márquez"]

print("Lista original de autores:")
print(autores)

# Ordenar la lista
autores_ordenados = insertion_sort(autores.copy())
print("\nLista ordenada alfabéticamente:")
print(autores_ordenados)

# Buscar un autor
objetivo = "Paz"

# Búsqueda lineal
indice_lineal = busqueda_lineal(autores, objetivo)
print(f"\nResultado búsqueda lineal de '{objetivo}':")
if indice_lineal != -1:
    print(f"Encontrado en la posición {indice_lineal} (lista original)")
else:
    print("No encontrado.")

# Búsqueda binaria
indice_binaria = busqueda_binaria(autores_ordenados, objetivo)
print(f"\nResultado búsqueda binaria de '{objetivo}':")
if indice_binaria != -1:
    print(f"Encontrado en la posición {indice_binaria} (lista ordenada)")
else:
    print("No encontrado.")
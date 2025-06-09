# TP-Integrador-Programacion-1
Repositorio TP Integrador Programacion

Algoritmo de Búsqueda y Ordenamiento

Alumnos:

Lautaro Pez- lautapez@gmail.com
Cristian Paolucci- cristianodixit@gmail.com


Materia: Programación I

Profesor:

Fecha de entrega:

Comisión: 4


Este proyecto implementa y compara tres algoritmos utilizados para el manejo de datos:

    1. Insertion Sort (para ordenar alfabéticamente una lista de nombres)
   
    2. Búsqueda Lineal
  
    3. Búsqueda Binaria


Incluye un caso con una lista de autores.



Contenido

1.insertion_sort( ): Función para ordenar una lista de nombres usando el algoritmo de inserción

2.busqueda_lineal( ): Función para buscar un nombre en una lista, uno por uno

3.busqueda_binaria( ): Función que realiza búsqueda binaria sobre una lista ordenada
4.Ejemplo práctico de uso con una lista de autores


Ejemplo de uso

autores = ["Cortázar", "Borges", "Neruda", "Paz", "García Márquez"]
objetivo = "Paz"

# Ordenar la lista
autores_ordenados = insertion_sort(autores.copy())

# Búsqueda lineal en la lista original
indice_lineal = busqueda_lineal(autores, objetivo)

# Búsqueda binaria en la lista ordenada
indice_binaria = busqueda_binaria(autores_ordenados, objetivo)
 

Algoritmo utilizados

Insert Sort

Ordena alfabéticamente elementos uno a uno
Ideal para listas pequeñas o casi ordenadas
Complejidad: O(n²) en el peor caso


Búsqueda Lineal

Recorre secuencialmente todos los elementos
No requiere lista ordenada
Complejidad: O(n)

Búsqueda Binaria

Solo funciona con listas ordenadas
Divide el rango de búsqueda por la mitad en cada caso
Complejidad: O(log n)

 Cómo ejecutar

Descargar o clonar este repositorio
Abrir el archivo .py con cualquier editor de texto o IDE
Ejecutar el script desde consola:

python Tp-Integrador-Busqueda-Ordenamiento.py


Resultados esperados

El programa imprime:

  La lista original de autores
  La lista ordenada alfabéticamente
  El resultado de búsqueda lineal (posición en la lista original)
  El resultado de la búsqueda binaria (posición en la lista ordenada)

Desarrollo del Tp Integrador

Investigación previa: Lautaro Pez-Cristian Paolucci 
Desarrollo del Caso Práctico: Lautaro Pez-Cristian Paolucci
Pdf Tp Integrador y README: Lautaro Pez-Cristian Paolucci

Link al video: https://www.youtube.com/watch?v=rY2EtceMys0

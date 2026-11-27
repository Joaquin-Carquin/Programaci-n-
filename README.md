# Sistema de Gestión de Productos

Estudiante: Joaquín Carquín
Asignatura: FPY1101 - Fundamentos de Programación
Lenguaje: Python

Descripción

Este proyecto consiste en un sistema de gestión de productos de una tienda. Permite registrar, buscar, eliminar y mostrar productos mediante un menú interactivo.

Funciones principales

1. Agregar productos.
2. Buscar productos.
3. Eliminar productos.
4. Actualizar disponibilidad.
5. Mostrar productos registrados.
6. Salir del sistema.

Datos utilizados

Cada producto almacena su nombre, stock, precio y disponibilidad. Para organizar la información se utilizan listas y diccionarios.

Archivo principal:

"joaquin_carquin.py"

# Optimiza la búsqueda y actualización de disponibilidad de productos

Se modifica el proceso de búsqueda para permitir encontrar productos sin depender de las diferencias entre mayúsculas, minúsculas o espacios adicionales en el nombre ingresado.

También se incorpora la actualización de disponibilidad antes de mostrar los datos de un producto encontrado, asegurando que el estado mostrado corresponda con su cantidad de stock actual.

Con estos cambios se mejora la precisión de las búsquedas y la consistencia de la información presentada por el sistema.

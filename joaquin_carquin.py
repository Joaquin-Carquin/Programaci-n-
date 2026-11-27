# joaquin_carquin
# Evaluacion Parcial 4 - Fundamentos de Programacion (FPY1101)
# Sistema de gestion de productos de una tienda

def validar_nombre(nombre):
    return nombre.strip() != ""


def validar_stock(stock):
    try:
        cantidad = int(stock)
        return cantidad >= 0
    except ValueError:
        return False


def validar_precio(precio):
    try:
        valor = float(precio)
        return valor > 0
    except ValueError:
        return False


def mostrar_menu():
    print("\n========== MENU PRINCIPAL ==========")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Eliminar producto")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar productos")
    print("6. Salir")
    print("====================================")


def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opcion (1-6): "))
            if opcion >= 1 and opcion <= 6:
                return opcion
            else:
                print("Opcion no valida. Ingrese un numero del 1 al 6.")
        except ValueError:
            print("Debe ingresar un numero entero.")


def agregar_producto(productos):
    print("\n--- AGREGAR PRODUCTO ---")
    nombre = input("Ingrese el nombre del producto: ")

    if not validar_nombre(nombre):
        print("Error: el nombre no puede estar vacio.")
        return

    stock_ingresado = input("Ingrese el stock del producto: ")
    if not validar_stock(stock_ingresado):
        print("Error: el stock debe ser un numero entero mayor o igual a cero.")
        return

    precio_ingresado = input("Ingrese el precio del producto: ")
    if not validar_precio(precio_ingresado):
        print("Error: el precio debe ser un numero mayor que cero.")
        return

    producto = {
        "nombre": nombre.strip(),
        "stock": int(stock_ingresado),
        "precio": float(precio_ingresado),
        "disponible": False
    }

    productos.append(producto)
    print("Producto agregado correctamente.")


def buscar_producto(productos, nombre):
    for posicion in range(len(productos)):
        if productos[posicion]["nombre"] == nombre:
            return posicion
    return -1


def eliminar_producto(productos):
    print("\n--- ELIMINAR PRODUCTO ---")
    nombre = input("Ingrese el nombre del producto que desea eliminar: ")
    posicion = buscar_producto(productos, nombre)

    if posicion != -1:
        productos.pop(posicion)
        print("Producto eliminado correctamente.")
    else:
        print("El producto '" + nombre + "' no se encuentra registrado.")


def actualizar_disponibilidad(productos):
    for producto in productos:
        if producto["stock"] > 0:
            producto["disponible"] = True
        else:
            producto["disponible"] = False

    print("Disponibilidad actualizada.")


def mostrar_productos(productos):
    actualizar_disponibilidad(productos)

    print("\n=== LISTA DE PRODUCTOS ===")
    if len(productos) == 0:
        print("No hay productos registrados.")
    else:
        for producto in productos:
            print("Nombre:", producto["nombre"])
            print("Stock:", producto["stock"])
            print("Precio:", producto["precio"])

            if producto["disponible"]:
                print("Estado: DISPONIBLE")
            else:
                print("Estado: SIN STOCK")

            print("********************************************")


def main():
    productos = []

    print("Bienvenido al sistema de gestion de productos")

    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            agregar_producto(productos)

        elif opcion == 2:
            nombre = input("Ingrese el nombre del producto que desea buscar: ")
            posicion = buscar_producto(productos, nombre)

            if posicion != -1:
                print("\nProducto encontrado:")
                print("Nombre:", productos[posicion]["nombre"])
                print("Stock:", productos[posicion]["stock"])
                print("Precio:", productos[posicion]["precio"])
                print("Disponible:", productos[posicion]["disponible"])
            else:
                print("El producto '" + nombre + "' no se encuentra registrado.")

        elif opcion == 3:
            eliminar_producto(productos)

        elif opcion == 4:
            actualizar_disponibilidad(productos)

        elif opcion == 5:
            mostrar_productos(productos)

        elif opcion == 6:
            print("Gracias por usar el sistema. Vuelva Pronto")
            break


main()


# Justificacion del desarrollo:
# La lista de productos se envia como parametro a las funciones que la necesitan,
# para que cada funcion pueda trabajar con los mismos datos sin usar una variable global.
# La funcion de busqueda retorna -1 cuando no encuentra un producto, asi las opciones
# de buscar y eliminar pueden saber si existe antes de mostrarlo o quitarlo de la lista.

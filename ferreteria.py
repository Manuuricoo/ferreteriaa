import sqlite3
from provv import Proveedor
from producto import Producto
from ventas import Venta

conn = sqlite3.connect("ferreteria.db")
cursor = conn.cursor()
 
cursor.execute("CREATE TABLE IF NOT EXISTS Producto (idP INTEGER PRIMARY KEY,nombre TEXT,cantidad INTEGER,precio REAL,proveedor_id INTEGER,FOREIGN KEY(proveedor_id) REFERENCES Proveedor(id))")

cursor.execute("CREATE TABLE IF NOT EXISTS Proveedor (id INTEGER PRIMARY KEY,nombre TEXT,telefono TEXT,direccion TEXT)")

cursor.execute("CREATE TABLE IF NOT EXISTS Venta (idV INTEGER PRIMARY KEY,producto_id INTEGER,cantidad_vendida INTEGER,fecha INTEGER, FOREIGN KEY(producto_id) REFERENCES Producto(idP))")
    
proveedorTabla = Proveedor()
productosTabla = Producto()
ventasTabla = Venta()


apartado = True
while apartado:
   print("Proveedor--Producto--Venta")
   apartado = input("ingrese su eleccion: ")

     #terminado
   if apartado == "proveedor":
        apartado1 = ""
        while apartado1 != "4":
            print("¿Que deseas hacer?")
            print("-Ver proveedores")
            print("-Agregar proveedor")
            print("-Borrar proveedor")
            print("-Salir")
            apartado1 = input("ingrese su eleccion:")

            if apartado1 =="1":
                print("estos son los proveedores existentes")
                proveedorTabla.verProveedores()

            elif apartado1 == "2":
                print("Vamos a agregar un nuevo proveedor a la tabla ")
                nombre = input("ingrese el nombre del nuevo proveedor: ")
                telefono = input(f" ingrese el numero telefonico del nuevo proveedor: ")
                direccion = input(f"ingrese la direccion del nuevo proveedor: ")
                proveedorTabla.agregar_proveedor(nombre,telefono,direccion)

            elif apartado1 == "3": 
                print("Vamos a borrar un proveedor.")
                value = input("Porfavor ingrese el id del proveedor a eliminar: ")
                proveedorTabla.eliminar_proveedor(value)

            elif apartado1 =="4":
                print("saliendo")
                apartado1 = "4"
                break

            else:
                print("ingrese una eleccion valida.")
                break

   elif apartado == "productos":
        apartado1 = ""
        while apartado1 != "6":
            print("¿Que deseas hacer?")
            print("-Ver los procutos existentes")
            print("-Agregar un nuevo producto")
            print("-Borrar un producto existente")
            print("-Ver productos menores a 10")
            print("-Mostrar suma total de los productos")
            apartado1 = input("Ingrese su eleccion: ")
            if apartado1 == "1":
                print("- Vamos a ver los registros de Productos -")
                productosTabla.ver_Productos()

            elif apartado1 == "2":
                print("- Vamos a agregar un nuevo producto a la tabla ")
                id = input ("ingresa el id del nuevo producto")
                nombre = input("ingresa el nombre del nuevo producto: ")
                nombre = nombre.capitalize()
                cantidad = input("ingresa la cantidad")
                precio = input("ingresa el precio del producto: ")
                proveedor_id = input("ingresa el id del proveedor del producto: ")
                productosTabla.agregar_producto(id,nombre,cantidad,precio,proveedor_id)


            elif apartado1 == "3": 
                print("Vamos a borrar el registro de un producto")
                value = input("Porfavor ingrese el id del producto a eliminar: ")
                productosTabla.eliminar_producto(value)

            elif apartado1 == "4":
                productosTabla.mostrar_productos_bajos()

            elif apartado1 == "5":
                suma = productosTabla.valor_total_inventario()
                print(f"La suma total de todos los productos si se vendieran seria: {suma}")

            elif apartado1 == "6":
                print("Saliendo de Productos.\n")
                apartado1 = "6"
                break
            else: 
                print("Ingrese una opcion validad, porfavor.")
            
            answer = input("Desea realizar otra operacion en productos? S/N: ")
            if answer == "N" or answer  == "n" or answer == "No" or answer == "no" or answer == "NO":
                print("Saliendo de Productos.\n")
                apartado1 = "6"
                break

   elif apartado == "venta":
        apartado1 = ""
        while apartado1 != "5":
            print("¿Que deseas hacer?")
            print("-Ver ventas")
            print("-Agregar venta")
            print("-Borrar venta")
            print("-Mostrar ultimas 5 ventas")
            print("-Salir")
            apartado1 = input("Ingrese su eleccion: ")
            if apartado1 == "1":
                print("- Veamos todas las ventas registradas ")
                ventasTabla.ver_Ventas()


            elif apartado1 == "2":
                print("- Vamos a agregar una nueva venta a la tabla. ")
                idV = ("Ingresa un id para la venta")
                producto_id = input("Ingresa el id del producto comprado: ")
                cantidad_vendida = int(input("Ingresa la cantidad comprada: "))
                fecha = input("Ingresa la fecha de la venta: ")
                ventasTabla.agregar_Venta(idV,producto_id,cantidad_vendida, fecha)

            elif apartado1 == "3": 
                print("-Vamos a borrar un registro de ventas")
                value = int(input("Ingresa el id del registro de venta a eliminar: "))
                ventasTabla.eliminar_Venta(value)

            
            elif apartado1 == "4":
                print("estas son las ultimas  ventas registradas")
                ventasTabla.mostrar_ultimos_5_vendidos()

            elif apartado1 == "5":
                print("Saliendo de  Venta.\n")
                opcion1 = "5"
                break

            else: 
                print("Ingresa una opcion valida.")
            
            answer = input("¿Queres hacer otra operacion en Venta? S/N: ")
            if answer == "N" or answer  == "n" or answer == "No" or answer == "no" or answer == "NO":
                print("Saliendo de Venta.\n")
                opcion1 = "5"
                break

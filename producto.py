import sqlite3
from provv import Proveedor
proveedorTabla = Proveedor
conn = sqlite3.connect("ferreteria.db")
cursor = conn.cursor()

class Producto:
    def __init__(self):
        pass

    def ver_Productos(self):
        datos = ["IdP","nombre","cantidad","precio", "Id del proveedor"]
        res = cursor.execute("SELECT * FROM Producto")
        respuesta = res.fetchall()
        y = 0
        for item in respuesta:
            y += 1
            i = 0
            print(f"-Producto {y}")
            for dato in datos:
                print(f"{dato}: {item[i]}")
                i += 1  
            print("\n")
    
    def returnBusqueda(self, idP):
            res = cursor.execute("SELECT * FROM Producto WHERE idP = ?", (idP,))
            respuesta = res.fetchall()
            return respuesta

    def agregar_producto(self,idP,nombre,cantidad,precio,proveedor_id):
        cursor.execute ("INSERT INTO Producto (idP,nombre,cantidad,precio,proveedor_id) VALUES(?,?,?,?,?)",(idP,nombre,cantidad,precio,proveedor_id))
        conn.commit()
        print("el producto se agrego correctamente")   

    def eliminar_producto(self,idP):
        resp = self.returnBusqueda(idP)
        if resp:
            print("Vamos a eliminar el siguiente producto: ")
            answer = input("¿Desea borrarlo? S/N: ")
            if answer == "S" or answer == "s" or answer == "si" or answer == "Si" or answer == "SI":
             cursor.execute ("DELETE FROM Producto WHERE idP = ?",(idP,))
             conn.commit()
             print("el producto se ha eliminado")
        else:
            print("El id ingresado no corresponde no coincide con ningun producto o no fue encontrado, intente de nuevo.")


    def mostrar_productos_bajos(self):
        cursor.execute("SELECT * FROM Producto WHERE cantidad < 10")
        mostrar_productos_bajos = cursor.fetchall()
        for producto in mostrar_productos_bajos:
         print(producto)

         conn.close()
        
    def valor_total_inventario(self):
      conn = sqlite3.connect('ferreteria.db')
      cursor = conn.cursor()
    
      cursor.execute("SELECT SUM(precio * cantidad) FROM Producto")
      total_valor = cursor.fetchone()[0]
    
      print(f"El valor total del inventario es: {total_valor}")

      conn.close()
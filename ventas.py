import sqlite3
from producto import Producto
productosTabla = Producto()
conn = sqlite3.connect("ferreteria.db")
cursor = conn.cursor()

class Venta:
    def __init__(self):
       pass

    def  ver_Ventas(self):
        datos = ["idV,Cantidad_vendida","producto_id", "Producto", "Fecha"]
        res = cursor.execute("SELECT * FROM Venta")
        respuesta = res.fetchall()
        y = 0
        for item in respuesta:
            y += 1
            i = 0
            print(f"-Registro {y}")
            for dato in datos:
                print(f"{dato}: {item[i]}")
                i += 1  
            print("\n")   

   
    def returnBusqueda(self, idV):
            res = cursor.execute("SELECT * FROM Venta WHERE idV = ?", (idV,))
            respuesta = res.fetchall()
            return respuesta

    def ultId(self):
        res = cursor.execute("SELECT idV FROM Venta ORDER BY idV DESC LIMIT 1") 
        respuesta = res.fetchall()
        return respuesta[0][0]

    def agregar_Venta(self, idV,producto_id,cantidad_vendida, fecha):
            cursor.execute("INSERT INTO Venta (idV,producto_id,cantidad_vendida, fecha) VALUES (?,?,?,?)", (idV,producto_id,cantidad_vendida, fecha))
            conn.commit()
            print("Se registro la venta correctamente.")

    def eliminar_Venta(self, idV):
        resppp = self.returnBusqueda(idV)
        if resppp:
            print("El registro a eliminar es el siguiente:")
            answer = input("¿Desea borrarlo? S/N: ")
            if answer == "S" or answer == "s" or answer == "si" or answer == "Si" or answer == "SI":
                    cursor.execute("DELETE FROM Venta WHERE idV = ?", (idV,))
                    conn.commit()
                    print("Venta eliminada correctamente.")

    def mostrar_ultimos_5_vendidos(self):
     cursor.execute("SELECT * FROM Venta ORDER BY idV DESC LIMIT 5")
     mostrar_ultimos_5_vendidos = cursor.fetchall()
     for venta in mostrar_ultimos_5_vendidos:
      print ("-Las ultimas 5 ventas fueron:")
      print(venta)
    
      
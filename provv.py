import sqlite3

conn = sqlite3.connect("ferreteria.db")
cursor = conn.cursor()

class Proveedor:
    def __init__(self):
        pass

    def verProveedores(self):
        datos = ["Id", "nombre", "telefono","direccion"]
        res = cursor.execute("SELECT * FROM Proveedor")
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

    def return_Busqueda(self, id):
        res = cursor.execute("SELECT * FROM Proveedor WHERE id = ?", (id,))
        respuesta = res.fetchall()
        return respuesta

    def ultId(self):
        res = cursor.execute("SELECT proveedor_id FROM Proveedor ORDER BY id DESC LIMIT 1") 
        respuesta = res.fetchall()
        return respuesta[0][0]

    def agregar_proveedor(self, nombre, telefono, direccion):
        cursor.execute ("INSERT INTO Proveedor (nombre,telefono,direccion) VALUES(?,?,?)", (nombre, telefono, direccion,))
        conn.commit()
        nId = self.ultId()
        self.verProveedores(nId)
        print("el proveedor se cargo correctamente")


    def eliminar_proveedor(self, id):
        print("Vamos a borrar el siguiente proveedor: ")
        cursor.execute("DELETE FROM Proveedor WHERE id = ?", (id,))
        conn.commit()
        print("¡Registro borrado exitosamente!")
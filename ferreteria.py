import sqlite3
conn = sqlite3.connect("ferreteria.db")
cursor = conn.cursor()
 
cursor.execute("CREATE TABLE IF NOT EXISTS Producto (id INTEGER PRIMARY KEY,nombre TEXT,cantidad INTEGER,precio REAL,proveedor_id INTEGER,FOREIGN KEY(proveedor_id) REFERENCES Proveedor(id))")

cursor.execute("CREATE TABLE IF NOT EXISTS Proveedor (id INTEGER PRIMARY KEY,nombre TEXT,telefono TEXT,direccion TEXT)")

cursor.execute("CREATE TABLE IF NOT EXISTS Venta (  id INTEGER PRIMARY KEY,producto_id INTEGER,cantidad_vendida INTEGER,fecha DATE, FOREIGN KEY(producto_id) REFERENCES Producto(id))")
    
conn.commit()
conn.close()

class Producto:
    def __init__(self, id, nombre, cantidad, precio, proveedor_id):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.proveedor_id = proveedor_id


    def agregar_producto(self):
        # Método para agregar un producto a la base de datos
        pass

    def actualizar_producto(self):
        # Método para actualizar un producto en la base de datos
        pass

    def eliminar_producto(self):
        # Método para eliminar un producto de la base de datos
        pass

class Proveedor:
    def __init__(self, id, nombre, telefono, direccion):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

    def agregar_proveedor(self):
        # Método para agregar un proveedor a la base de datos
        pass

class Venta:
    def __init__(self, id, producto_id, cantidad_vendida, fecha):
        self.id = id
        self.producto_id = producto_id
        self.cantidad_vendida = cantidad_vendida
        self.fecha = fecha

    def registrar_venta(self):
        # Método para registrar una venta en la base de datos
        pass


def mostrar_productos_bajos():
    conn = sqlite3.connect('ferreteria.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Producto WHERE cantidad < 10")
    productos_bajos = cursor.fetchall()
    
    for producto in productos_bajos:
        print(producto)

    conn.close()


def mostrar_ultimos_productos_vendidos():
    conn = sqlite3.connect('ferreteria.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Venta ORDER BY fecha DESC LIMIT 5")
    ultimas_ventas = cursor.fetchall()
    
    for venta in ultimas_ventas:
        print(venta)

    conn.close()


def valor_total_inventario():
    conn = sqlite3.connect('ferreteria.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(precio * cantidad) FROM Producto")
    total_valor = cursor.fetchone()[0]
    
    print(f"El valor total del inventario es: {total_valor}")

    conn.close()
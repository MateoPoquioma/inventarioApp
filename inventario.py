import csv

class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f'{self.nombre} (ID: {self.id}, Precio: {self.precio}, Cantidad: {self.cantidad})'

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.id in self.productos:
            self.productos[producto.id].cantidad += producto.cantidad
        else:
            self.productos[producto.id] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]

    def buscar_producto(self, id):
        return self.productos.get(id, None)

    def actualizar_producto(self, id, precio, cantidad):
        if id in self.productos:
            self.productos[id].precio = precio
            self.productos[id].cantidad = cantidad


    def listar_productos(self):
        return list(self.productos.values())

    def guardar_datos(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Nombre', 'Precio', 'Cantidad'])
            for producto in self.productos.values():
                writer.writerow([producto.id, producto.nombre, producto.precio, producto.cantidad])

    def cargar_datos(self, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    producto = Producto(row['ID'], row['Nombre'], float(row['Precio']), int(row['Cantidad']))
                    self.productos[producto.id] = producto
        except FileNotFoundError:
            pass

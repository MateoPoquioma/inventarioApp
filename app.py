from flask import Flask, render_template, request, redirect, url_for
from inventario import Inventario, Producto

app = Flask(__name__)
inventario = Inventario()
inventario.cargar_datos('data.csv')

@app.route('/')
def mostrar_inventario():
    productos = inventario.listar_productos()
    return render_template('index.html', productos=productos)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        id = request.form['id']
        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        cantidad = int(request.form['cantidad'])
        producto = Producto(id, nombre, precio, cantidad)
        inventario.agregar_producto(producto)
        inventario.guardar_datos('data.csv')
        return redirect(url_for('mostrar_inventario'))
    return render_template('agregar.html')

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    producto = None
    if request.method == 'POST':
        id = request.form['id']
        producto = inventario.buscar_producto(id)
    return render_template('buscar.html', producto=producto)

@app.route('/actualizar', methods=['GET', 'POST'])
def actualizar():
    if request.method == 'POST':
        id = request.form['id']
        cantidad = int(request.form['cantidad'])
        precio = float(request.form['precio'])
        inventario.actualizar_producto(id, cantidad, precio)
        inventario.guardar_datos('data.csv')
        return redirect(url_for('mostrar_inventario'))
    return render_template('actualizar.html')

@app.route('/eliminar', methods=['POST'])
def eliminar():
    id = request.form['id']
    inventario.eliminar_producto(id)
    inventario.guardar_datos('data.csv')
    return redirect(url_for('mostrar_inventario'))

if __name__ == '__main__':
    app.run(debug=True)

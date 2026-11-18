import json

with open("data.json", "r") as f:
    data = json.load(f)

print(data)

# TOTAL FACTURADO

total_facturado = 0

for ventas, productos in data.items():
    for producto in productos:

        precio = producto["precio_unitario"]
        cantidad = producto["cantidad"]

        total_facturado += precio*cantidad

print(total_facturado)

# VENTAS POR CATEGORÍA

ventas_cat = {}

for ventas, productos in data.items():
    for producto in productos:

        categoria = producto["categoria"]
        cantidad = producto["cantidad"]

        if categoria in ventas_cat:
            ventas_cat[categoria] += cantidad

        else:
            ventas_cat[categoria] = cantidad

print(ventas_cat)

# PRODUCTO MÁS VENDIDO

ventas_prod = {}

for ventas, productos in data.items():
    for producto in productos:

        nombre = producto["producto"]
        cantidad = producto["cantidad"]

        if nombre in ventas_prod:
            ventas_prod[nombre] += cantidad

        else:
            ventas_prod[nombre] = cantidad


cantidad = 0

for producto, ventas in ventas_prod.items():

    if ventas > cantidad:
        cantidad = ventas
        producto_mas_vendido = producto

print(f"Producto Más vendido: {producto_mas_vendido} - Cantidad: {cantidad}")
import json

#  data.json
with open("data.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

ventas = datos["ventas"]


def total_facturado(ventas):
    total = 0

    for venta in ventas:
        importe = venta["cantidad"] * venta["precio_unitario"]
        total = total + importe

    return total


print("Total facturado:", total_facturado(ventas))

def ventas_por_categoria(ventas):
    categorias = {}

    for venta in ventas:
        categoria = venta["categoria"]
        importe = venta["cantidad"] * venta["precio_unitario"]

        if categoria in categorias:
            categorias[categoria] = categorias[categoria] + importe
        else:
            categorias[categoria] = importe

    return categorias


print("Ventas por categoría:", ventas_por_categoria(ventas))

def producto_mas_vendido(ventas):
    cantidades = {}

    for venta in ventas:
        producto = venta["producto"]
        cantidad = venta["cantidad"]

        if producto in cantidades:
            cantidades[producto] = cantidades[producto] + cantidad
        else:
            cantidades[producto] = cantidad

    producto = max(cantidades, key=cantidades.get)

    return producto, cantidades[producto]


print("Producto más vendido:", producto_mas_vendido(ventas))


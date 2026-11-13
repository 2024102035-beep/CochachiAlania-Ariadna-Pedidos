# Autor: Cochachi Alania Ariadna
# CR-015: Implementar el calculo del envio y total del pedido

def calcular_subtotal(precio, cantidad):
    return precio * cantidad

def calcular_envio(subtotal):
    if subtotal >= 300:
        return 0
    else:
        return 20

precio = 80
cantidad = 3

subtotal = calcular_subtotal(precio, cantidad)
envio = calcular_envio(subtotal)
total = subtotal + envio

print("Subtotal: S/", subtotal)
print("Costo de envio: S/", envio)
print("Total del pedido: S/", total)
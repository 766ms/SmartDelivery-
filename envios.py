
def envios(**kwargs):
    return kwargs

nombre = input("Ingrese su nombre para realizar el pedido= ")
direccion = input("Ingrese su dirección para realizar el pedido= ")
telefono = int(input("Ingrese su telefono para realizar el pedido= "))

fullInfoenvio = envios(nombre=nombre, direccion=direccion, telefono=telefono)
print(f"Envíos= {fullInfoenvio}")


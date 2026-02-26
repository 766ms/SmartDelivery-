
def envios(*args, **kwargs):
    return args, kwargs

nombre = input("Ingrese su nombre para realizar el pedido= ")
direccion = input("Ingrese su dirección para realizar el pedido= ")
telefono = int(input("Ingrese su telefono para realizar el pedido= "))

fullInfoenvio = envios(nombre, direccion, telefono)
print(f"Envíos con *args= {fullInfoenvio}")

fullInfoenvio2 = envios(nombre=nombre, direccion=direccion, telefono=telefono)
print(f"Envíos con **kwargs= {fullInfoenvio2}")

def envios(nombre, direccion, telefono):
    return nombre, direccion, telefono
nombre= input("Ingrese su nombre para realizar el pedido= ")
direccion=input("Ingrese su dirección para realizar el pedido= ")
telefono=int(input ("Ingrese su telefono para realizar el pedido=  "))

fullInfoenvio= envios(nombre,direccion, telefono)

print (f"envios= {fullInfoenvio}" )

#ingrese lugares como marbella, torices, ciudad jardin
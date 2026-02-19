def repartidores (ruta, nombre) :
    return ruta, nombre
ruta=  ["marbella", "ciudad jardin", "bocagrande", "manga" "todo los barrios"]
nombre= ["Garridita","Bleyder", "Yudis", "Sebastian", "Jose"]
print("0. marbella - Garridita")
print("1. ciudad jardin - Bleyder")
print("2. bocagrande - Yudis")
print("3. manga - Sebastian") 
print("4. todos los barrios - Jose") 
selectrepartidor = int(input("Escoge el número del barrio: "))
print(f"El repartidor seleccionado es {nombre[selectrepartidor]} y su ruta es por {ruta[selectrepartidor]}")
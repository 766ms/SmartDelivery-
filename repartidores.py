
def repartidores(**kwargs):
    return kwargs

repartidores_info = repartidores(
    Garridita="marbella",
    Bleyder="ciudad jardin",
    Yudis="bocagrande",
    Sebastian="manga",
    Jose="todos los barrios"
)

for i, (nombre, ruta) in enumerate(repartidores_info.items()):
    print(f"{i}. {ruta} - {nombre}")

selectrepartidor = int(input("Escoge el número del barrio: "))

nombre = list(repartidores_info.keys())[selectrepartidor]
ruta = list(repartidores_info.values())[selectrepartidor]

print(f"El repartidor seleccionado es {nombre} y su ruta es por {ruta}")
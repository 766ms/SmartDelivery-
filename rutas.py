
def rutas(*args):
    return args

barrio, km, precios = rutas(
    ["marbella", "ciudad jardin", "bocagrande", "manga"],
    [2, 14, 2, 3],
    [2000, 5000, 1000, 2000]
)

for i in range(len(barrio)):
    print(f"{i}. {barrio[i]} - {km[i]} km - ${precios[i]}")

selectbarrio = int(input("Escoge el número del barrio: "))

print(f"El barrio seleccionado es {barrio[selectbarrio]} y se encuentra a {km[selectbarrio]} km de nuestra sede del centro y su envio tiene un valor de ${precios[selectbarrio]}")

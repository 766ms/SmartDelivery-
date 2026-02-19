def rutas (barrio, km, precios) :
    return barrio, km, precios
barrio=  ["marbella", "ciudad jardin", "bocagrande", "manga"]
km= [2,14,2,3]
precios= [2000, 5000, 1000, 2000]
print("0. marbella - 2 km - $2000")
print("1. ciudad jardin - 14 km - $5000")
print("2. bocagrande - 2 km - $1000")
print("3. manga - 3 km - $2000") 
selectbarrio = int(input("Escoge el número del barrio: "))
print(f"El barrio seleccionado es {barrio[selectbarrio]} y se encuentra a {km[selectbarrio]} km de nuestra sede del centro y su envio tiene un valor de ${precios[selectbarrio]}")

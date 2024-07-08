inventario = ["Tomate", "Pera", "Manzana"]

fruta = input("Ingrese una nueva fruta: ")

inventario.append(fruta)

fruta = input("Ingrese Fruta a eliminar: ")

inventario.remove(fruta) if fruta in inventario else print("No esta esa fruta")

inventario.sort()

print("Frutas:")
print(*inventario, sep="\n")

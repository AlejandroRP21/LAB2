class Producto:
    def __init__(self, nombre, categoria, precio, stock):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad):
        self.stock += cantidad
        print(f"Nuevo stock de {self.nombre}: {self.stock}")
def main():
    productos = []

    while True:
        print("\n--- Gestión de Productos ---")
        print("1. Crear nuevo producto")
        print("2. Actualizar stock")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            nombre = input("Nombre del producto: ")
            categoria = input("Categoría del producto: ")
            precio = float(input("Precio del producto: "))
            stock = int(input("Stock inicial: "))
            producto = Producto(nombre, categoria, precio, stock)
            productos.append(producto)
            print("Producto creado con éxito.")

        elif opcion == '2':
            nombre = input("Nombre del producto a actualizar: ")
            for producto in productos:
                if producto.nombre == nombre:
                    cantidad = int(input("Cantidad a añadir al stock: "))
                    producto.actualizar_stock(cantidad)
                    break
            else:
                print("Producto no encontrado.")

        elif opcion == '3':
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
    

#Este codigo es funcional para una tienda o un minisuper y llevar un registro de productos que se manejan dentro de la tienda 
# se puede utilizar para actualizar datos de algunos productos o ingresar nuevos productos, la problematica que resuelve es para poder ingresar un registro
#de manera mas rapida de forma basica utilizando pythone
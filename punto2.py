class Articulo:
    def __init__(self, nombre, precioDcompra):
        self.nombre = nombre
        self.precioDcompra = precioDcompra
        self.precioDventa = precioDcompra * 1.30

    def mostrar_info(self):
        return f"{self.nombre} - Precio de compra: ${self.precioDcompra:.2f}, Precio de venta: ${self.precioDventa:.2f}"

class Cuaderno(Articulo):
    def __init__(self, numerohojas, preciocompra1):
        nombre = f"Cuaderno {numerohojas} hojas (HOJITAS)"
        super().__init__(nombre, preciocompra1)

class Lapiz(Articulo):
    def __init__(self, tipo, preciocompra1):
        nombre = f"Lápiz {tipo} (RAYAS)"
        super().__init__(nombre, preciocompra1)

def registrar_articulos():
    articulos = []
    
    precioCuaderno50 = float(input("Escriba el precio del cuaderno de 50 hojas: "))
    cuaderno50 = Cuaderno(50, precioCuaderno50)
    articulos.append(cuaderno50)

    precioDcuaderno100 = float(input("Escriba el precio del cuaderno de 100 hojas: "))
    cuaderno100 = Cuaderno(100, precioDcuaderno100)
    articulos.append(cuaderno100)

    preciolapizDgrafito = float(input("Escriba el precio del lápiz de grafito: "))
    lapizDgrafito = Lapiz("grafito", preciolapizDgrafito)
    articulos.append(lapizDgrafito)

    preciolapizDcolores = float(input("Escriba el precio del lápiz de colores: "))
    lapizDcolores = Lapiz("colores", preciolapizDcolores)
    articulos.append(lapizDcolores)

    return articulos

def visualizar_articulos(articulos):
    print("\n--- Información de los artículos ---")
    for articulo in articulos:
        print(articulo.mostrar_info())
        
if __name__ == "__main__":
    articulos = registrar_articulos()
    visualizar_articulos(articulos)


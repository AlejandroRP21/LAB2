class Auto:
    def __init__(self, marca, modelo, precioDcompra):
        self.marca = marca
        self.modelo = modelo
        self.precioDcompra = precioDcompra
        self.precioDventa = precioDcompra * 1.40
        self.caracteristicas = {
            "Ruedas": 4,
            "Capacidad de pasajeros": 5
        }

    def mostrar_info(self):
        return (f"Marca: {self.marca}\nModelo: {self.modelo}\nPrecio de compra: ${self.precioDcompra:.2f}\n"
                f"Precio de venta: ${self.precioDventa:.2f}\nCaracterísticas: {self.caracteristicas}")
    
def registrarautos():
    autos = []
    
    for i in range(2): 
        marca = input(f"Escriba la marca del carro {i + 1}: ")
        modelo = input(f" Escriba el modelo del carro {i + 1}: ")
        precioDcompra = float(input(f"Escriba el precio de compra {i + 1}: "))
        auto = Auto(marca, modelo, precioDcompra)
        autos.append(auto)
    
    return autos

def visualizarautos(autos):
    print("\n--- Información de los autos ---")
    for auto in autos:
        print(auto.mostrar_info())
        
if __name__ == "__main__":
    autos = registrarautos()
    visualizarautos(autos)

class DispositivoElectronico:
    def __init__(self, nombre, precioDcompra, modelo, memoria, megapixeles, pantalla, bateria):
        self.nombre = nombre
        self.precioDcompra = precioDcompra
        self.modelo = modelo
        self.memoria = memoria
        self.megapixeles = megapixeles
        self.pantalla = pantalla
        self.bateria = bateria
        self.precioDventa = precioDcompra * 1.7

    def mostrar_info(self):
        return (f"Nombre: {self.nombre}\n"
                f"Modelo: {self.modelo}\n"
                f"Memoria: {self.memoria}\n"
                f"Cámara: {self.megapixeles} MP\n"
                f"Pantalla: {self.pantalla}\n"
                f"Batería: {self.bateria}\n"
                f"Precio de compra: ${self.precioDcompra:.2f}\n"
                f"Precio de venta: ${self.precioDventa:.2f}\n")

class Celular(DispositivoElectronico):
    def __init__(self, precioDcompra, modelo, memoria, megapixeles, pantalla, bateria):
        super().__init__("Celular PHR", precioDcompra, modelo, memoria, megapixeles, pantalla, bateria)

class Tablet(DispositivoElectronico):
    def __init__(self, precioDcompra, modelo, memoria, megapixeles, pantalla, bateria):
        super().__init__("Tablet PHR", precioDcompra, modelo, memoria, megapixeles, pantalla, bateria)

class Portatil(DispositivoElectronico):
    def __init__(self, precioDcompra, modelo, memoria, pantalla, bateria):
        super().__init__("Portátil PHR", precioDcompra, modelo, memoria, None, pantalla, bateria)  # No tiene megapíxeles

def registrar_dispositivos():
    dispositivos = []

    while True:
        print("\n--- Seleccione qué producto va a ingresar ---")
        print("1. Ingresar teléfono nuevo")
        print("2. Ingresar tablet nueva")
        print("3. Ingresar laptop nueva")
        print("4. Mostrar datos ingresados")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            # Teléfono
            precioDcompra = float(input("Ingresa el precio de compra del celular: "))
            modelo = input("Ingresa el modelo del celular: ")
            memoria = input("Ingresa la memoria del celular: ")
            megapixeles = input("Ingresa los megapíxeles de la cámara del celular: ")
            pantalla = input("Ingresa el tamaño de pantalla del celular: ")
            bateria = input("Ingresa la capacidad de la batería del celular: ")
            celular = Celular(precioDcompra, modelo, memoria, megapixeles, pantalla, bateria)
            dispositivos.append(celular)

        elif opcion == '2':
            # Tablet
            precioDcompra = float(input("Ingresa el precio de compra de la tablet: "))
            modelo = input("Ingresa el modelo de la tablet: ")
            memoria = input("Ingresa la memoria de la tablet: ")
            megapixeles = input("Ingresa los megapíxeles de la cámara de la tablet: ")
            pantalla = input("Ingresa el tamaño de pantalla de la tablet: ")
            bateria = input("Ingresa la capacidad de la batería de la tablet: ")
            tablet = Tablet(precioDcompra, modelo, memoria, megapixeles, pantalla, bateria)
            dispositivos.append(tablet)

        elif opcion == '3':
            # Laptop
            precioDcompra = float(input("Ingresa el precio de compra de la laptop: "))
            modelo = input("Escribe el modelo del portátil: ")
            memoria = input("Ingresa la memoria del portátil: ")
            pantalla = input("Ingresa el tamaño de pantalla del portátil: ")
            bateria = input("Ingresa la capacidad de la batería del portátil: ")
            portatil = Portatil(precioDcompra, modelo, memoria, pantalla, bateria)
            dispositivos.append(portatil)

        elif opcion == '4':
            visualizar_dispositivos(dispositivos)

        elif opcion == '5':
            break

        else:
            print("Opción no válida. Intenta nuevamente.")

    return dispositivos

def visualizar_dispositivos(dispositivos):
    print("\n--- Información de los dispositivos ---")
    if not dispositivos:
        print("No hay dispositivos registrados.")
    for dispositivo in dispositivos:
        print(dispositivo.mostrar_info())

if __name__ == "__main__":
    dispositivos = registrar_dispositivos()
    visualizar_dispositivos(dispositivos)
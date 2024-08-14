class Perro:
    def __init__(self, nombre, raza, edad, peso, color, nombre_dueño, telefonoDdueño, direccionDdueño):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.color = color
        self.nombre_dueño = nombre_dueño
        self.telefonoDdueño = telefonoDdueño
        self.direccionDdueño = direccionDdueño
        self.estado = 'NO ATENDIDO'
        self.tipo = 'Perro Grande' if peso >= 10 else 'Perro Pequeño'

    def registrar(self):
        self.estado = 'ATENDIDO'
        return self

    def mostrar_informacion(self):
        return f"""\
Información del Perro:
Nombre: {self.nombre}
Raza: {self.raza}
Edad: {self.edad} años
Peso: {self.peso} kg - {self.tipo}
Color: {self.color}
Dueño: {self.nombre_dueño}
Teléfono del Dueño: {self.telefonoDdueño}
Dirección del Dueño: {self.direccionDdueño}
Estado: {self.estado}
"""
def registrar_perro():
    nombre = input("Nombre del perro: ")
    raza = input("Raza del perro: ")
    edad = int(input("Edad del perro (en años): "))
    peso = float(input("Peso del perro (en kg): "))
    color = input("Color del perro: ")
    nombre_dueño = input("Nombre del dueño: ")
    telefonoDdueño = input("Teléfono del dueño: ")
    direccionDdueño = input("Dirección del dueño: ")

    perro = Perro(nombre, raza, edad, peso, color, nombre_dueño, telefonoDdueño, direccionDdueño)
    
    perro.registrar()
    
    print(perro.mostrar_informacion())

registrar_perro()

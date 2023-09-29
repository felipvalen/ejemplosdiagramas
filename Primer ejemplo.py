class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo_bruto):
        super().__init__(nombre, edad)
        self.sueldo_bruto = sueldo_bruto

class EmpleadoDirecto(Empleado):
    def __init__(self, nombre, edad, sueldo_bruto, categoria):
        super().__init__(nombre, edad, sueldo_bruto)
        self.categoria = categoria
        self.subordinados = []

    def agregar_subordinado(self, subordinado):
        self.subordinados.append(subordinado)

class Cliente(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

# Ejemplo de uso
cliente1 = Cliente("Cliente 1", 30)
empleado1 = Empleado("Empleado 1", 25, 50000)
empleado2 = EmpleadoDirecto("Director 1", 40, 80000, "Gerente")
empleado3 = Empleado("Empleado 2", 28, 45000)

empleado2.agregar_subordinado(empleado1)
empleado2.agregar_subordinado(empleado3)

# Mostrar datos
print("Datos del Cliente:")
print(f"Nombre: {cliente1.nombre}")
print(f"Edad: {cliente1.edad}")

print("\nDatos del Empleado:")
print(f"Nombre: {empleado1.nombre}")
print(f"Edad: {empleado1.edad}")
print(f"Sueldo Bruto: {empleado1.sueldo_bruto}")

print("\nDatos del Empleado Directo:")
print(f"Nombre: {empleado2.nombre}")
print(f"Edad: {empleado2.edad}")
print(f"Sueldo Bruto: {empleado2.sueldo_bruto}")
print(f"Categoria: {empleado2.categoria}")
print("Subordinados:")
for subordinado in empleado2.subordinados:
    print(f"- {subordinado.nombre}")

print("\nDatos del Empleado:")
print(f"Nombre: {empleado3.nombre}")
print(f"Edad: {empleado3.edad}")
print(f"Sueldo Bruto: {empleado3.sueldo_bruto}")

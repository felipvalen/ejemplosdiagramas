class Cliente:
    def __init__(self, dni, nombre, direccion, telefono, codigo):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.codigo = codigo
        self.avalador = None  # Cliente que avala a este cliente

    def asignar_avalador(self, cliente_avalador):
        self.avalador = cliente_avalador

class Coche:
    def __init__(self, matricula, modelo, color, marca, garaje):
        self.matricula = matricula
        self.modelo = modelo
        self.color = color
        self.marca = marca
        self.garaje = garaje

class Reserva:
    def __init__(self, cliente, agencia, fecha_inicio, fecha_final, coches, litros_gasolina, precio_total, entregado):
        self.cliente = cliente
        self.agencia = agencia
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self.coches = coches
        self.litros_gasolina = litros_gasolina
        self.precio_total = precio_total
        self.entregado = entregado

class Garaje:
    def __init__(self, nombre):
        self.nombre = nombre

class Agencia:
    def __init__(self, nombre):
        self.nombre = nombre

# Ejemplo de uso
garaje1 = Garaje("Garaje A")
garaje2 = Garaje("Garaje B")

agencia1 = Agencia("Agencia X")
agencia2 = Agencia("Agencia Y")

cliente1 = Cliente("12345678A", "Cliente 1", "Dirección 1", "123456789", "C001")
cliente2 = Cliente("98765432B", "Cliente 2", "Dirección 2", "987654321", "C002")
cliente2.asignar_avalador(cliente1)

coche1 = Coche("ABC123", "Modelo 1", "Rojo", "Marca 1", garaje1)
coche2 = Coche("XYZ789", "Modelo 2", "Azul", "Marca 2", garaje2)

reserva1 = Reserva(cliente1, agencia1, "2023-09-21", "2023-09-28", [coche1], 50, 500, False)
reserva2 = Reserva(cliente2, agencia2, "2023-09-25", "2023-10-02", [coche1, coche2], 80, True)

# Mostrar datos de la reserva
print("Datos de la Reserva:")
print(f"Cliente: {reserva1.cliente.nombre}")
print(f"Agencia: {reserva1.agencia.nombre}")
print(f"Fecha de Inicio: {reserva1.fecha_inicio}")
print(f"Fecha de Finalización: {reserva1.fecha_final}")
print("Coches:")
for coche in reserva1.coches:
    print(f"- Matrícula: {coche.matricula}")
print(f"Litros de Gasolina: {reserva1.litros_gasolina}")
print(f"Precio Total: {reserva1.precio_total}")
print(f"Entregado: {reserva1.entregado}")


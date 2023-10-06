#Realizado por Alvaro Felipe Valenzuela Martinez 
#6/10/2023
#Codido 842611

class Calculadora:
    def __init__(self):
        self.num1 = int(input("Ingrese un numero:"))
        self.num2 = int(input("Ingrese un segundo numero:"))
    
    def suma(self):
        return self.num1 + self.num2
    
    def resta(self):
        return self.num1 - self.num2
    
    def multiplicacion(self):
        return self.num1 * self.num2
    
    def division(self):
        if self.num2 == 0:
            return "Error: No se puede dividir por cero."
        else:
            return self.num1 / self.num2

# Crear la clase de la calculadora
calculadora = Calculadora()

# resultado de las operaciones
print("Suma:", calculadora.suma())
print("Resta:", calculadora.resta())
print("Multiplicación:", calculadora.multiplicacion())
print("División:", calculadora.division())

"""Enunciado: Crea una clase cuenta bancaria que permita depositar y retirar (impidiendo retirar más del saldo).
Requerimientos: Aplica POO básica, métodos, y condicionales lógicos (<=) para proteger el saldo."""

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Fondos insuficientes. No se puede retirar esa cantidad.")
        elif cantidad <= 0:
            print("La cantidad a retirar debe ser mayor que cero.")
        else:
            self.saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")
cuenta = CuentaBancaria("Juan Pérez", 1000)
cuenta.depositar(500) 
cuenta.retirar(200)    
cuenta.retirar(1500)   
cuenta.retirar(-100)   
cuenta.depositar(-50)  

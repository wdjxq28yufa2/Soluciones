class Cuenta:
    def __init__(self, saldo, tasa_interes):
        self.saldo = saldo
        self.tasa_interes = tasa_interes / 100 / 12

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        return False

    def calcular_interes(self, meses):
        return self.saldo * self.tasa_interes * meses


def main():
    saldo_inicial = float(input("Ingrese el saldo inicial de la cuenta: "))
    tasa_interes_anual = float(input("Ingrese la tasa de interés anual (%): "))
    cuenta = Cuenta(saldo_inicial, tasa_interes_anual)

    print("Saldo inicial:", cuenta.saldo)

    cantidad_deposito = float(input("Ingrese la cantidad a depositar: "))
    cuenta.depositar(cantidad_deposito)
    print("Saldo después del depósito:", cuenta.saldo)

    cantidad_retiro = float(input("Ingrese la cantidad a retirar: "))
    if cuenta.retirar(cantidad_retiro):
        print("Retiro exitoso. Saldo después del retiro:", cuenta.saldo)
    else:
        print("Fondos insuficientes. No se pudo realizar el retiro.")

    meses_transcurridos = int(input("Ingrese el número de meses para calcular el interés: "))
    print(f"Interés generado después de {meses_transcurridos} meses:", cuenta.calcular_interes(meses_transcurridos))


if __name__ == "__main__":
    main()
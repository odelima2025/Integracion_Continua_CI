# cartera.py
class SaldoInsuficiente(Exception):
    pass

class Cartera(object):
    def __init__(self, saldo_inicial=0):
        if isinstance(saldo_inicial, int) and saldo_inicial > 0:
            self.saldo = saldo_inicial
        else:
            self.saldo = 0

    def gastar(self, cantidad):
        if self.saldo < cantidad:
            raise SaldoInsuficiente(
                'No tienes dinero suficiente. Saldo actual: {}'.format(self.saldo))
        # Introducir un error: no restar correctamente la cantidad
        self.saldo -= cantidad // 2

    def ingresar(self, cantidad):
        self.saldo += cantidad

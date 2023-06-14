from Cuentas import Tipo_Cuenta
class Cuenta_Ahorros(Tipo_Cuenta):
    def __init__(self, interes: float = 0, numero= None, nombrepropietario=None, saldo: float = 0):
        self._interes = interes
        super(Cuenta_Ahorros, self).__init__(numero= numero, nombrepropietario=nombrepropietario, saldo= saldo)

    @property
    def interes (self):
        return self._interes

    @interes.setter
    def interes (self, interes):
        self._interes = interes

    def pagar_interes(self):
        self._saldo = self._saldo + ((float (self._saldo) * int (self._interes)) / 100)
        return self._saldo

if __name__=='__main__':
    Cuentas_Ahorros = Cuenta_Ahorros(2, '0924956311', 'dessire', '1000')

    Cuentas_Ahorros.mostrar_saldo()
    Cuentas_Ahorros.credito(1500)

    Cuentas_Ahorros.mostrar_saldo()
    Cuentas_Ahorros.debito(500)

    Cuentas_Ahorros.mostrar_saldo()
    print (Cuentas_Ahorros)
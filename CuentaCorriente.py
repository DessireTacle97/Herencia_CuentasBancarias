from Cuentas import Tipo_Cuenta
class Cuenta_Corriente(Tipo_Cuenta):
    def __init__(self, numero= None, nombrepropietario=None, saldo: float = 0, tieneChequera = bool):
        self._tieneChequera = tieneChequera
        super(Cuenta_Corriente, self).__init__(numero= numero, nombrepropietario=nombrepropietario, saldo= saldo)

    @property
    def tieneChequera(self):
        return self._tieneChequera

    @tieneChequera.setter
    def tienechequera(self, tieneChequera):
        self._tieneChequera = tieneChequera

    def pagar_cheque(self):
        self._saldo = self._saldo + ((float (self._saldo) - int (self._pagar_cheque)))
        return self._saldo

if __name__=='__main__':
    Cuentas_Corriente = Cuenta_Corriente('09249563111', 'dessire', '100', bool)

    Cuentas_Corriente.mostrar_saldo()
    Cuentas_Corriente.credito(150)

    Cuentas_Corriente.mostrar_saldo()
    Cuentas_Corriente.debito(50)

    Cuentas_Corriente.mostrar_saldo()
    print (Cuentas_Corriente)

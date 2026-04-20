class CuentaBancaria:
    def _init_(self, titular, numero_cuenta, saldo, tipo_cuenta, banco):
        self.__titular = titular
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo
        self.__tipo_cuenta = tipo_cuenta
        self.__banco = banco
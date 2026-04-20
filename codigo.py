class CuentaBancaria:
    def _init_(self, titular, numero_cuenta, saldo, tipo_cuenta, banco):
        self.__titular = titular
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo
        self.__tipo_cuenta = tipo_cuenta
        self.__banco = banco
    def get_titular(self):
        return self.__titular

    def get_numero_cuenta(self):
        return self.__numero_cuenta

    def get_saldo(self):
        return self.__saldo

    def get_tipo_cuenta(self):
        return self.__tipo_cuenta

    def get_banco(self):
        return self.__banco

    def set_titular(self, titular):
        self.__titular = titular

    def set_numero_cuenta(self, numero_cuenta):
        self.__numero_cuenta = numero_cuenta

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def set_tipo_cuenta(self, tipo_cuenta):
        self.__tipo_cuenta = tipo_cuenta

    def set_banco(self, banco):
        self.__banco = banco
        
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Fondos insuficientes")

    def info(self):
        print(f"Titular: {self._titular}, Cuenta: {self.numero_cuenta}, Saldo: {self.saldo}, Tipo: {self.tipo_cuenta}, Banco: {self._banco}")
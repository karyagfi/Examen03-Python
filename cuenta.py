class CuentaBancaria:
  def __init__(self, titular, saldo = 0):
    self.titular = titular
    self.__saldo = saldo
  
  # Recibe un valor cantidad y lo suma al atributo __saldo.
  def depositar(self, cantidad):
    self.__saldo += cantidad

  # Recibe un valor cantidad y lo resta al atributo __saldo.
  def retirar(self, cantidad):
    self.__saldo -= cantidad

  # Devuelve el valor de __saldo, permitiendo consultar el saldo de la cuenta sin modificarlo.
  def consultar_saldo(self):
    return self.__saldo
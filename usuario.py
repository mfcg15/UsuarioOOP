class Usuario :

    def __init__(self,name):
        self.name = name
        self.balance_cuenta = 0

    def hacer_depositio(self,amount):
        self.balance_cuenta += amount
    
    def hacer_retiro(self,amount):
        self.balance_cuenta -=amount

    def mostrar_balance_usuario(self):
        print("Usuario: "+self.name+", Balance: $ "+str(self.balance_cuenta))

    def transfer_dinero(self,other_user,amount):
        other_user.hacer_depositio(amount)
        self.balance_cuenta -=amount

usurio1 = Usuario("Adrien")
usurio2 = Usuario("Mr. Nibbles")
usurio3 = Usuario("Benny Bob")

usurio1.hacer_depositio(100)
usurio1.hacer_depositio(150)
usurio1.hacer_depositio(100)
usurio1.hacer_retiro(45)
usurio1.mostrar_balance_usuario()

usurio2.hacer_depositio(600)
usurio2.hacer_depositio(800)
usurio2.hacer_retiro(100)
usurio2.hacer_retiro(100)
usurio2.mostrar_balance_usuario()

usurio3.hacer_depositio(500)
usurio3.hacer_retiro(3000)
usurio3.hacer_retiro(2500)
usurio3.hacer_retiro(2500)
usurio3.mostrar_balance_usuario()

usurio2.transfer_dinero(usurio1,400)
usurio2.mostrar_balance_usuario()
usurio1.mostrar_balance_usuario()
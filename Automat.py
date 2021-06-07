from Monety import *

class Automat():
    suma = 0

    def init(self):
        super().init()

    def odejmijCene(self, cena):
        self.suma -= cena
        print('Odjęto bilet o wartości : ' + str(cena/100) + 'zł')

    def dodajCene(self, cena):
        self.suma += cena
        print('Dodano bilet o wartości : ' + str(cena/100) + 'zł')

    def pobierz_suma(self):
        return str(self.suma/100)

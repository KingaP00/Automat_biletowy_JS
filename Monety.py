from decimal import *

class Monety:
    lista_monet = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50]
    pass

    def __init__(self):
        self.automat_lista_monet = []
        self.wartosc = 0

    def dodaj(self,wartosc):
        if wartosc in self.automat_lista_monet:
            self. wartosc = wartosc
            self.automat_lista_monet.append(Decimal(str(wartosc)))

    def zabierz(self, wartosc):
        pass

    def suma(self):
        print('Suma', sum(self.automat_lista_monet))
        return sum(self.automat_lista_monet)

    def reszta(self, cena, ilosc):
        pass

    #TODO funkcja dodaje pieniadze do aktualnych
    # pieniadze w autoamcie lista--> automat
    # lista pieniedzy ktore wydam jako reszta
    # funkcja takemoney dla list od glownej listy
    #testy



class Monety:
    monety = {
        1: 0,
        2: 0,
        5: 0,
        10: 0,
        20: 0,
        50: 0,
        100: 0,
        200: 0,
        500: 0,
        1000: 0,
        2000: 0,
        5000: 0
    }

    def __init__(self):
        self.automat_lista_monet = {}
        self.reszta = {}
        self.wartosc = 0

    def dodaj(self, wartosc):
        self.monety[wartosc] += 1

    def suma(self):
        print('Suma', sum(self.automat_lista_monet))
        return sum(self.automat_lista_monet)

    def oblicz_reszte(self, suma, pieniadze):
        self.do_wydania = pieniadze - suma

        for key in sorted(self.monety.keys(), reverse=True):
            if key < self.do_wydania:
                self.wydaj_monete(key)
            elif key == self.do_wydania:
                self.wydaj_monete(key)
                break
        self.podglad_monet('Po wyliczeniu reszty')
        if self.do_wydania != 0:
            self.monety = {key: 0 for key in self.monety.keys()}
            self.podglad_monet('Błąd, nie ma z czego wydać')
            raise ValueError()

        return True

    def wydaj_monete(self, key):
        if (self.automat_lista_monet.get(key, 0) + self.monety[key] - self.reszta.get(key, 0)) != 0:
            self.reszta[key] = self.reszta.get(key, 0) + 1
            self.do_wydania -= key
            if key <= self.do_wydania:
                self.wydaj_monete(key)

    def zaakceptuj_monety(self):
        self.podglad_monet('Przed zaakceptowaniem')
        self.automat_lista_monet = {key: (self.automat_lista_monet.get(key, 0) + self.monety[key]) for key in
                                    self.monety.keys()}
        self.monety = {key: 0 for key in self.monety.keys()}
        if self.reszta:
            self.automat_lista_monet = {key: (self.automat_lista_monet[key] - self.reszta.get(key, 0)) for key in
                                        self.automat_lista_monet.keys()}
            self.reszta = {}
        self.podglad_monet('Po zaakceptowaniu')

    def podglad_monet(self, operacja):
        print("####################################################")
        print(operacja)
        print("W automacie:", self.automat_lista_monet)
        print("Monety:", self.monety)
        print("Reszta:", self.reszta)
        print("####################################################")


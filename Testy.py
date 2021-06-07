import unittest
from Interfejs import *


class testy(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.interfejs = Interfejs()


    def test_zakup_za_rowna_gotowke(self):
        bilet = self.interfejs.bilety['bilet20u']
        self.interfejs.suma.dodajCene(bilet['cena'])
        self.assertEqual(bilet['cena'], self.interfejs.suma.suma)

        self.interfejs.monety.dodaj(50)
        self.interfejs.monety.dodaj(100)

        self.assertEqual(self.interfejs.suma.suma, self.interfejs.monety.suma())

        self.interfejs.monety.zaakceptuj_monety()

        self.assertEqual(self.interfejs.monety.reszta, {})
        self.assertEqual(self.interfejs.monety.automat_lista_monet[50], 1)
        self.assertEqual(self.interfejs.monety.automat_lista_monet[100], 1)


    def test_bilet_za_wieksza_kwote_z_reszta(self):
        bilet = self.interfejs.bilety['bilet20u']
        self.interfejs.suma.dodajCene(bilet['cena'])
        self.assertEqual(bilet['cena'], self.interfejs.suma.suma)

        self.interfejs.monety.dodaj(50)
        self.interfejs.monety.dodaj(100)
        self.interfejs.monety.dodaj(100)
        self.interfejs.wrzucone(250)

        try:
            self.interfejs.monety.oblicz_reszte(150, self.interfejs.twojepieniadze)
        except Exception as e:
            self.assertEqual(ValueError, e.__class__)

        self.assertEqual(self.interfejs.monety.reszta[100], 1)
        self.interfejs.monety.zaakceptuj_monety()

        self.assertEqual(self.interfejs.monety.reszta, {})


    def test_bilet_za_wieksza_kwote_brak_reszty(self):
        bilet = self.interfejs.bilety['bilet20u']
        self.interfejs.suma.dodajCene(bilet['cena'])
        self.assertEqual(bilet['cena'], self.interfejs.suma.suma)

        self.interfejs.monety.dodaj(50)
        self.interfejs.monety.dodaj(200)
        self.interfejs.wrzucone(250)

        try:
            self.interfejs.monety.oblicz_reszte(150, self.interfejs.twojepieniadze)
        except Exception as e:
            self.assertEqual(ValueError, e.__class__)
        self.assertEqual(self.interfejs.monety.reszta, {})



    def test_zakup_biletu_placac_po_1gr(self):
        bilet = self.interfejs.bilety['bilet20u']
        self.interfejs.suma.dodajCene(bilet['cena'])
        self.assertEqual(bilet['cena'], self.interfejs.suma.suma)

        for i in range(0, 150):
            self.interfejs.monety.dodaj(1)
        self.interfejs.wrzucone(150)

        self.assertEqual(self.interfejs.suma.suma, self.interfejs.monety.suma())

        self.interfejs.monety.zaakceptuj_monety()

        self.assertEqual(self.interfejs.monety.reszta, {})
        self.assertEqual(self.interfejs.monety.automat_lista_monet[1], 150)


    def test_zakup_dwoch_roznych_biletow(self):
        bilet = self.interfejs.bilety['bilet20u']
        bilet2 = self.interfejs.bilety['bilet40u']
        self.interfejs.suma.dodajCene(bilet['cena'])
        self.interfejs.suma.dodajCene(bilet2['cena'])
        self.assertEqual(bilet['cena'] + bilet2['cena'], self.interfejs.suma.suma)

        self.interfejs.monety.dodaj(200)
        self.interfejs.monety.dodaj(200)
        self.assertEqual(self.interfejs.suma.suma, self.interfejs.monety.suma())

        self.interfejs.monety.zaakceptuj_monety()

        self.assertEqual(self.interfejs.monety.reszta, {})
        self.assertEqual(self.interfejs.monety.automat_lista_monet[200], 2)

    def test_dodanie_biletu_plus_monety_plus_bilet_plus_monety(self):
        bilet = self.interfejs.bilety['bilet20u']
        bilet2 = self.interfejs.bilety['bilet40u']

        self.interfejs.suma.dodajCene(bilet['cena'])
        self.interfejs.monety.dodaj(200)
        self.interfejs.suma.dodajCene(bilet2['cena'])
        self.interfejs.monety.dodaj(200)

        self.assertEqual(bilet['cena'] + bilet2['cena'], self.interfejs.suma.suma)

        self.assertEqual(self.interfejs.suma.suma, self.interfejs.monety.suma())

        self.interfejs.monety.zaakceptuj_monety()

        self.assertEqual(self.interfejs.monety.reszta, {})
        self.assertEqual(self.interfejs.monety.automat_lista_monet[200], 2)

    def tearDown(self) -> None: # Wywołuje się po każdym testem
        self.interfejs.monety.monety = {
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
        self.interfejs.monety.reszta = {}
        self.interfejs.monety.automat_lista_monet = {}
        self.interfejs.twojepieniadze = 0
        self.interfejs.suma.suma = 0


if __name__ == '__main__':
    unittest.main()

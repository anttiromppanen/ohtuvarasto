import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_tilavuus_palauttaa_nollan(self):
        negatiivinen_varasto = Varasto(-1)

        self.assertAlmostEqual(negatiivinen_varasto.tilavuus, 0)

    def test_negatiivinen_saldo_palauttaa_nollan(self):
        negatiivinen_saldo = Varasto(10, alku_saldo = -1)

        self.assertAlmostEqual(negatiivinen_saldo.saldo, 0)

    def test_negatiivinen_lisays_ei_mene_lapi(self):
        self.assertFalse(self.varasto.lisaa_varastoon(-1))

    def test_suurella_maaralla_ei_lisata_enempaa_kuin_mahtuu(self):
        varasto = Varasto(10)
        varasto.lisaa_varastoon(11)

        self.assertAlmostEqual(varasto.saldo, varasto.tilavuus)

    def test_varastosta_ottaminen_epaonnistuu_negatiivisella_maaralla(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0.0)

    def test_palautetaan_kaikki_kun_maara_on_suurempi_kuin_arvo(self):
        varasto = Varasto(10, alku_saldo = 5)
        otettava_maara = varasto.ota_varastosta(6)
        
        self.assertAlmostEqual(otettava_maara, 5)
        self.assertAlmostEqual(varasto.saldo, 0.0)

    def test_varaston_tulostus_toimii_oikein(self):
        varasto = Varasto(10, 5)
        
        self.assertEqual(str(varasto), f"saldo = {varasto.saldo}, vielä tilaa {varasto.paljonko_mahtuu()}")
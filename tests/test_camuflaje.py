import unittest
import os
from camuflaje import camuflar_texto, cargar_configuracion

class TestCamuflaje(unittest.TestCase):
    
    def test_redactar_ips_y_usuarios(self):
        entrada = "IP de origen: 192.168.1.50\nuser: admin"
        esperado = "IP de origen: 10.x.x.x\nuser: REDACTED"
        resultado = camuflar_texto(entrada)
        self.assertEqual(resultado, esperado)

    def test_patrones_configuracion(self):
        entrada = "hostname: srv-produccion-clientex\npath: /home/admin-clientex"
        patrones = ["srv-produccion-clientex", "/home/admin-clientex"]
        esperado = "hostname: REDACTED\npath: REDACTED"
        resultado = camuflar_texto(entrada, patrones)
        self.assertEqual(resultado, esperado)

if __name__ == '__main__':
    unittest.main()

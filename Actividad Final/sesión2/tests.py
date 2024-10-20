from funciones import clearFile, validateCreds, hashPassword, saveUser, checkUser
import unittest


class TestCases(unittest.TestCase):
    def test_Credentials(self) -> None:
        # Lo esperado es que diga que el usuario o contraseña es muy corto.
        result = validateCreds('A', '123')
        self.assertEqual(result, False, "FALLO: validando credenciales inseguras")

        # Lo esperado es que dé un resultado positivo al ser una credenciales seguras.
        result = validateCreds('User', 'securepassword')
        self.assertEqual(result, True, "FALLO: validando credenciales seguras")

        # Mediante regex verificamos que el hash que obtenemos cumple las características:
        # $2b$00$xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        result = hashPassword('password').decode('utf-8')
        self.assertRegex(result, r'\$2b\$([0-9][0-9])\$.{53}\Z', r'FALLO: el hash obtenido no cumple el regex: \$2b\$([0-9][0-9])\$.{53}\Z')

    def test_Users(self) -> None:
        # Lo esperado es que nos deje crear un primer usuario correctamente.
        result = saveUser('TestUser', 'securepassword')
        self.assertEqual(result, True, 'FALLO: durante la creación del primer usuario')

        # Lo esperado es que no nos deje crear un usuario con el mismo nombre.
        result = saveUser('TestUser', 'somepassword')
        self.assertEqual(result, False, 'FALLO: guardando un usuario con el mismo nombre')

        # Lo esperado es que nos deje iniciar sesión con el usuario creado con credenciales correctas.
        result = checkUser('TestUser', 'securepassword')
        self.assertEqual(result, True, 'FALLO: iniciando sesión con un usuario existente')

        # Lo esperado es que no nos deje crear un usuario con credenciales vacías.
        result = saveUser('', '')
        self.assertEqual(result, False, 'FALLO: creando un usuario con credenciales vacías')

        # Lo esperado es que no nos deje iniciar sesión con credenciales vacías.
        result = checkUser('', '')
        self.assertEqual(result, False, 'FALLO: iniciar sesión con credenciales vacías')
        clearFile()


if __name__ == '__main__':
    clearFile()
    unittest.main()

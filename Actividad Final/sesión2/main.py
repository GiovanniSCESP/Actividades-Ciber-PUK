import funciones, sys, signal, hashlib, base64


def signal_handler(sig, frame): # Añadimos una función para manejar la salida del usuario por CTRL + C sin que dé una excepción.
    print('Saliendo...')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


if __name__ == '__main__':
    try:
        while True:
            user_input = int(input('\nGestor de contraseñas\n[1] Iniciar sesión \n[2] Registrar nuevo usuario\n[3] Salir\n> '))

            match user_input:
                case 1: 
                    user = input('Introduzca el usuario: ')
                    passwd = input('Introduzca la contraseña: ')
                    if funciones.checkUser(user, passwd):
                        # Si el inicio de sesión es correcto creamos una clave para la encriptación a partir de la contraseña introducida por el usuario.
                        # Esto lo hacemos para que la clave de encriptación sea única por usuario y no se pueda acceder sus datos almacenados sin conocer su contraseña.
                        # Para que sea compatible con Fernet se necesita una clave en bytes de 32 caracteres codificada en base64.
                        key = base64.b64encode(hashlib.sha256(passwd.encode('utf-8')).digest()[:32])
                        funciones.main(user, key) # Ejecutamos el segundo menú para gestionar los datos del usuario.
                case 2:
                    user = input('Introduzca el usuario: ')
                    passwd = input('Introduzca la contraseña: ')
                    funciones.saveUser(user, passwd) # Intentamos guardar el usuario con los datos introducidos.
                case 3:
                    sys.exit(0) # Salimos con un código de estado correcto.
                case _:
                    print(f'La opción {user_input} no existe') # Aseguramos un caso no esperado.
    
    except Exception as e: # Gestionamos una posible excepción.
        print(e)
        sys.exit(1)

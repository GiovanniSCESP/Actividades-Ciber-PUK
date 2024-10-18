import funciones, sys


if __name__ == '__main__':
    try:
        while True:
            user_input = int(input('\nGestor de contraseñas\n[1] Iniciar sesión \n[2] Registrar nuevo usuario\n[3] Salir\n> '))

            match user_input:
                case 1: 
                    user = input('Introduzca el usuario: ')
                    passwd = input('Introduzca la contraseña: ')
                    if funciones.checkUser(user, passwd):
                        key = funciones.hashPassword(passwd)
                        funciones.main(user, key)
                case 2:
                    user = input('Introduzca el usuario: ')
                    passwd = input('Introduzca la contraseña: ')
                    funciones.saveUser(user, passwd)
                case 3:
                    sys.exit(0)
                case _:
                    print(f'La opción {user_input} no existe.')
    
    except:
        sys.exit(0)

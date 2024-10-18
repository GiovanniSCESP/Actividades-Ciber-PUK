import funciones


if __name__ == '__main__':
    while True:
        user_input = int(input('\nGestor de contraseñas\n[1] Registrar nuevo usuario\n[2] Iniciar sesión\n> '))

        match user_input:
            case 1: 
                user = input('Introduzca el usuario: ')
                passwd = input('Introduzca la contraseña: ')
                funciones.saveUser(user, passwd)
            case 2:
                user = input('Introduzca el usuario: ')
                passwd = input('Introduzca la contraseña: ')
                funciones.checkUser(user, passwd)
            case _:
                print(f'La opción {user_input} no existe.')

from cryptography.fernet import Fernet
import bcrypt, json


def loadFile() -> list:
    'Carga la lista y sus diccionarios de un archivo.'
    try:
        with open('user_db.json', 'r', encoding='utf-8') as f:
            try:
                return list(json.loads(f.read())) # Si hay datos en el archivo lo cargamos como lista con los datos de diccionario que contenga dentro con json.loads.
            except:
                return [] # Si no hay datos en el archivo de guardado o el archivo no existe devolvemos una lista vacía para comenzar.
    except FileNotFoundError:
        with open('user_db.json', 'w', encoding='utf-8') as f: f.write('')
        return []


def saveFile() -> None:
    'Guarda los datos de la lista `user_db` en un archivo.'
    with open('user_db.json', 'w', encoding='utf-8') as f:
        json.dump(user_db, f, ensure_ascii=False, indent=4) # Con json.dump guardamos los datos en el archivo.


user_db = loadFile() # Tendremos una lista con con los usuarios dentro como base de datos.
# Guardaremos una lista con un diccionario por cada usuario con el nombre, contraseña hasheada y contraseñas guardadas encriptadas usando la contraseña como clave para la encriptación.
# user_db = [
#   {'user': 'Usuario', 'password': b'$2b$12$qPBirVYVuBTLSSjwxd3EneLzRujwFB0k8DiOvwaM0NlsRKvrLabtG', 'saved_passwords': [{'title': 'Google', 'password': '...'}, {'title': 'YouTube', 'password': '...'}]}
#   {'user': 'Usuario2', 'password': b'$2b$12$GOh3K5Upco1I3U4/uAQlauaPbeJvSEzyueW8GPDtTQZvuxhj2ReH6'', 'saved_passwords': [{'title': 'YouTube', 'password': '...'}]}
# ]


def hashPassword(passwd: str) -> bytes:
    'Devuelve una string como hash de bcrypt con salt.'
    passwd_bytes = passwd.encode('utf-8')
    salt = bcrypt.gensalt()
    passwd_hash = bcrypt.hashpw(passwd_bytes, salt)
    # Creamos el hash con salt de la contraseña introducida y la devolvemos.
    return passwd_hash


def checkUser(user: str, passwd: str) -> bool:
    'Comprueba el inicio de sesión de un usuario.'
    # Si existen usuarios se selecciona la contraseña hasheada del usuario con el que tratamos iniciar sesión.
    db_passwd_hash = False
    if len(user_db): db_passwd_hash = [data['password'] for data in user_db if data['user'] == user][0] # No pueden existir dos usuarios con el mismo nombre.

    passwd_bytes = passwd.encode('utf-8')

    if db_passwd_hash and bcrypt.checkpw(passwd_bytes, db_passwd_hash.encode('utf-8')): 
        # Si la contraseña del usuario existe y la contraseña introducida coincide con la almacenada como hash se inicia sesión.
        print('Inicio de sesión correcto')
        return True
    else:
        print('El usuario o la contraseña son incorrectos')
        return False # Devolvemos True o False por si fuera necesario realizar alguna comprobación adicional.


def saveUser(user: str, passwd: str) -> bool:
    'Guarda los datos de creación del usuario.'
    # Verificamos si el usuario existe con un list comprehension, si existe tendremos una lista con un resultado.
    user_exists = [data['user'] for data in user_db if data['user'] == user]

    if not user_exists: # Si el usuario no existe podemos guardar un nuevo usuario con la contraseña introducida como hash.
        passwd_hash = hashPassword(passwd)
        user_db.append({"user": user, "password": passwd_hash.decode('utf-8'), "saved_passwords": []})
        saveFile()
        print('El usuario se ha guardado correctamente')
        return True
    else: # Si el usuario ya existe se lo comunicamos la usuario.
        print('El nombre de usuario ya existe')
        return False # Devolvemos True o False por si fuera necesario realizar alguna comprobación.


def encryptPassword(passwd: str, key: bytes) -> bytes:
    'Encripta la contraseña con la clave dada.'
    f = Fernet(key) # Iniciamos el objeto de Fernet con la clave
    token = f.encrypt(passwd.encode('utf-8')) # Encriptamos la contraseña introducida.
    return token


def decryptPassword(token: bytes, key: bytes) -> str:
    'Desencripta la contraseña con la clave dada.'
    f = Fernet(key) # Iniciamos el objeto de Fernet con la clave
    passwd = f.decrypt(token).decode('utf-8') # Desencriptamos la contraseña introducida.
    return passwd


def savePassword(user: str, title: str, passwd: str, key: bytes) -> None:
    'Guarda la contraseña encriptándola con la clave dada.'
    user_data = [data for data in user_db if data['user'] == user][0]
    passwd_enc = encryptPassword(passwd, key)
    
    user_data['saved_passwords'].append({'title': title, 'password': passwd_enc.decode('utf-8')})
    saveFile()
    print(f'Se ha guardado el elemento {title} correctamente')


def deletePassword(user: str, index: int) -> bool:
    'Borra la contraseña dado un índice.'
    user_data = [data for data in user_db if data['user'] == user][0]

    for i, pass_data in enumerate(user_data['saved_passwords']):
        if i == index:
            del user_data['saved_passwords'][i]
            saveFile()
            print(f'Se ha eliminado el elemento {i} {pass_data.get('title')} correctamente')
            return True
    
    print(f'No se ha encontrado ningún elemento con el índice {index}')
    return False


def getStoredPasswords(user: str, key: bytes) -> None:
    'Muestra todas la contraseñas de un usuario desencriptadas.'
    user_data = [data for data in user_db if data['user'] == user][0]

    if user_data['saved_passwords']:
        for i, pass_data in enumerate(user_data['saved_passwords']):
            print(i, pass_data['title'], decryptPassword(pass_data['password'].encode('utf-8'), key))
    else:
        print('No existen contraseñas guardadas')


def main(user: str, key: bytes) -> None:
    while True:
        user_input = int(input(f'\nGestor de contraseñas - {user} \n[1] Consultar contraseñas\n[2] Nueva contraseña\n[3] Eliminar contraseña\n[4] Cerrar sesión\n> '))
        
        match user_input:
            case 1:
                getStoredPasswords(user, key)
            case 2:
                title = input('Introduzca el título: ')
                passwd = input('Introduzca la contraseña: ')
                savePassword(user, title, passwd, key)
            case 3:
                getStoredPasswords(user, key)
                index = int(input('Introduzca el índice a eliminar: '))
                deletePassword(user, index)
            case 4:
                break
            case _:
                print(f'La opción {user_input} no existe.')

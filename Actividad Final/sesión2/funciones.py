import bcrypt, time


user_db = [] # Tendremos una lista con con los usuarios dentro como base de datos.
# Guardaremos una lista con un diccionario por usuario con el nombre, contraseña hasheada y contraseñas guardadas encriptadas usando la contraseña como clave.
# user_db = [
#   {'user': 'Usuario', 'password': b'$2b$12$qPBirVYVuBTLSSjwxd3EneLzRujwFB0k8DiOvwaM0NlsRKvrLabtG', 'saved_passwords': }
#   {'user': 'Usuario2', 'password': b'$2b$12$GOh3K5Upco1I3U4/uAQlauaPbeJvSEzyueW8GPDtTQZvuxhj2ReH6'', 'saved_passwords': }
#]


def hashPassword(passwd: str) -> bytes:
    passwd_bytes = passwd.encode('utf-8')
    salt = bcrypt.gensalt()
    passwd_hash = bcrypt.hashpw(passwd_bytes, salt)

    return passwd_hash


def checkUser(user: str, passwd: str) -> bool:
    db_passwd_hash = False
    if len(user_db): db_passwd_hash = [data['password'] for data in user_db if data['user'] == user][0]

    passwd_bytes = passwd.encode('utf-8')

    if db_passwd_hash and bcrypt.checkpw(passwd_bytes, db_passwd_hash): 
        # Si la contraseña del usuario existe y la contraseña introducida coincide con la almacenada como hash se inicia sesión.
        print('Inicio de sesión correcto')
        return True
    else:
        print('El usuario o la contraseña son incorrectos')
        return False # Devolvemos True o False por si fuera necesario realizar alguna comprobación.


def saveUser(user: str, passwd: str) -> bool:
    # Verificamos que el usuario exista con un list comprehension, si existe tendremos una lista con un resultado.
    user_exists = [data['user'] for data in user_db if data['user'] == user]

    if not user_exists: # Si el usuario no existe podemos guardar un nuevo usuario con la contraseña introducida como hash.
        passwd_hash = hashPassword(passwd)
        user_db.append({'user': user, 'password': passwd_hash})
        print('El usuario se ha guardado correctamente')
        return True
    else: # Si el usuario ya existe se lo comunicamos la usuario.
        print('El nombre de usuario ya existe')
        return False # Devolvemos True o False por si fuera necesario realizar alguna comprobación.

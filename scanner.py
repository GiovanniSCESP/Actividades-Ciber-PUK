import socket


def scan_port(target_IP, port_num):
    try:
        # Inicializamos un objeto con la clase de socket con los parámetros 
        # AF_INET para manejar direcciones IP estandar con puerto
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Configuramos un timeout de 0.5 segundos que dará excepción al ocurrir.
        sock.settimeout(0.5)
        # Realizamos una conexión configurando la IP objetivo y el puerto
        sock.connect((target_IP, port_num))

        print(f'Puerto {port_num} abierto')

    except Exception as e:
        # AL ocurrir la excepción por timeout la ignoramos.
        pass


def main():
    target_IP = '172.20.1.223'
    port_min = 70
    port_max = 82

    for port in range(port_min, port_max+1):
        scan_port(target_IP, port)


main()

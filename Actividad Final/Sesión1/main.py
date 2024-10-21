import scapy.all

packet_list = []

def savePacket(packet) -> None:
    packet_list.append(packet)


def main(protocol: str, count: int):
    """Escanea la red y caputra una cantidad determinada de paquetes.

    Args:
        protocol (str): describe el protocolo a filtrar basado en el [Berkeley Packet Filter](https://www.ibm.com/docs/es/qsip/7.5?topic=queries-berkeley-packet-filters#c_forensics_bpf__prot_operators__title__1)
        count (int): Número de paquetes a capturar antes de salir.
    """
    print('[+] Escaneando la red...')
    capture = scapy.all.sniff(filter=protocol, count=count)

    with open('scapy_log.txt', 'w') as f:
        f.write(str(capture))
    
    capture.summary()


if __name__ == '__main__':
    protocol = 'tcp'
    count = 5
    main(protocol, count)

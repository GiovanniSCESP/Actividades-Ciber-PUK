# import scapy.all


# def main(protocol: str, count: int):
#     '''
#     Args:

#     protocol (str): describe el protocolo a filtrar basado en el [Berkeley Packet Filter](https://www.ibm.com/docs/es/qsip/7.4?topic=queries-berkeley-packet-filters)
#     count (int): Número de paquetes a capturar antes de salir.
#     '''
#     print('[+] Escaneando la red...')
#     capture = scapy.all.sniff(filter=protocol, count=count)
#     capture.summary()


# if __name__ == '__main__':
#     protocol = 'tcp'
#     count = 5
#     main(protocol, count)

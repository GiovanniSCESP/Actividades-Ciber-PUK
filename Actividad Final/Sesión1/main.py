# import scapy.all


# def main(protocol):
#     '''
#     Args:

#     protocol (str): describe el protocolo a filtrar basado en el [Berkeley Packet Filter](https://www.ibm.com/docs/es/qsip/7.4?topic=queries-berkeley-packet-filters)
#     '''
#     print('[+] Escaneando la red...')
#     capture = scapy.all.sniff(filter=protocol, count=5)
#     capture.summary()


# if __name__ == '__main__':
#     protocol = 'tcp'
#     count = 5
#     main(protocol=protocol)

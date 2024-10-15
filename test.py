num_list = input('Introduzca una lista de números separado por espacios: ').split()
num_list = [int(x) for x in num_list]
num_list.sort()
print(num_list)
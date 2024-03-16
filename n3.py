'''
Функции:
@bubble - функция, сортировки пузырьком
Аргументы:
@f - входящий массив 
'''

def bubble(f):
    for i in range(len(f)):
        for j in range(len(f)-i-1):
            if f[j][-1] < f[j+1][-1]:
                f[j], f[j+1] = f[j+1], f[j]
    return f

f = open('devices.txt').readlines()
n = open('devices.txt').readline().split('*')

data = []
for i in range(1, len(f)):
    data.append(f[i].split('*'))
data = bubble(data)

k = 0
search = ''
while search != '=':
    search = input()
    for i in data:
        if i[0] == search:
            print('По вашему запросу:', search, 'найдены следующие варианты:')
            print(i[0], i[1], '- тип устройства:', str(i[2])+';', 'Разрешение экрана -', str(i[3])+';', 'Цена -', i[-1])
            k = 1
            break
    if k == 0 and search != '=':
        print('У нас нет данного устройства')
    k = 0

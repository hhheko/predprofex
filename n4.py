'''
Функции:
@bubble - функция, сортировки пузырьком по второму значению
@normal - функция, которая нормально считает стоимость товара, в формате float
Аргументы:
@f - входящий массив, на выходе отсортированный массив по второму элементу
@fo - входящее число, содержащее запятую
@itog - нормальное число стоимости в формате float
'''

def normal(fo):
    aaa = fo.split(',')
    itog = float(aaa[0] + '.' + aaa[1])
    return itog

def bubble(f):
    for i in range(len(f)):
        for j in range(len(f)-i-1):
            if f[j][-1] < f[j+1][-1]:
                f[j], f[j+1] = f[j+1], f[j]
    return f

f = open('devices.txt').readlines()
n = open('devices.txt').readline().split('*')

data = []
data_company = set()
for i in range(1, len(f)):
    data.append(f[i].split('*'))
for i in data:
    data_company.add(i[0])

s = 0
total = []
data_company = sorted(data_company)
for i in data_company:
    for j in data:
        if j[0] == i:
            s += normal(j[-1])
    total.append([i, s])

total1 = bubble(total)

for i in total1:
    print('Если продать все ноутбуки', i[0], 'можно заработать', i[1])

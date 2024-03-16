'''
Функции:
@bubble_ord - функция, сортировки пузырьком на основе ord, функция сортирует в обрантном алфавитном порядке
Аргументы:
@f - входящий массив 
'''

def bubble_ord(f):
    for i in range(len(f)):
        for j in range(len(f)-i-1):
            if ord(f[j][0][0]) < ord(f[j+1][0][0]):
                f[j], f[j+1] = f[j+1], f[j]
    return f

f = open('devices.txt').readlines()
n = open('devices.txt').readline()

data = []
for i in range(1, len(f)):
    data.append(f[i].split('*'))

data = bubble_ord(data)
for i in range(5):
    print(data[i][0], '-', data[i][1], '-', data[i][-1])


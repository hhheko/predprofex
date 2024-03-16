'''
Функции:
@hashy - функция, создающая хэш на основе "Компания" + "Продукт", и возвращающая хэш, стоимость, компанию, продукт.
Аргументы:
@f - входной массив данных, содержащий всю информацию о ноутбуке
'''


def hashy(f):
    company = f[0]
    product = f[1]
    price = f[-1][:-1]
    total = f[0]+f[1]
    s = 0
    p = 67
    k = 0
    mod = 10**9+9
    for i in range(0, len(total)):
        s += ord(total[i])*p**k
        k += 1
    hashy = s % mod
    return hashy, price, company, product
        
f = open('devices.txt').readlines()
n = open('devices.txt').readline()

data = []
for i in range(1, len(f)):
    data.append(f[i].split('*'))

data_hash = []
for i in data:
    data_hash.append(hashy(i))
data_hash = sorted(data_hash)

k = 0
for i in data_hash:
    print(i[-2], i[-1], i[-3])
    k += 1
    if k == 10:
        break

    

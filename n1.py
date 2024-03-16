f = open('devices.txt').readlines()
n = open('devices.txt').readline()

data = []
for i in range(1, len(f)):
    data.append(f[i].split('*'))

models = ['Ultrabook', 'Notebook', 'Netbook']
Ultrabook = []
Ultrabooks = set()
itog1 = []
Notebook = []
Notebooks = set()
itog2 = []
Netbook = []
Netbooks = set()
itog3 = []
for i in data:
    if i[2] in models:
        if i[2] == 'Ultrabook':
            Ultrabook.append(i[5])
            Ultrabooks.add(i[5])
        if i[2] == 'Notebook':
            Notebook.append(i[5])
            Notebooks.add(i[5])
        if i[2] == 'Netbook':
            Netbook.append(i[5])
            Netbooks.add(i[5])
        
for i in Ultrabooks:
    itog1.append([i, Ultrabook.count(i)])
for i in Notebooks:
    itog2.append([i, Notebook.count(i)])
for i in Netbooks:
    itog3.append([i, Netbook.count(i)])

Netbooks = sorted(Netbooks)
Notebooks = sorted(Notebooks)
Ultrabooks = sorted(Ultrabooks)

with open('count_company.txt', 'w') as fo:
    print('Ultrabook', file = fo)
    for i in itog1:
        print(i[0], '-', i[1], file = fo)
    print('Notebook', file = fo)
    for i in itog2:
        print(i[0], '-', i[1], file = fo)
    print('Netbook', file = fo)
    for i in itog3:
        print(i[0], '-', i[1], file = fo)

'''
Создайте программу «Встань в строй». Дан список содержащий рост людей (уже есть кто-то кто встал в строй), пользователь
вводит рост нового человека. Ваша задача разместить всех по росту (от большего к меньшему), вывести этот список и
порядковый номер нового человека. Встать в строй может несколько человек, но только по одному, команда «все построены»
выводит весь общий список и завершает работу.
'''

rost = [168, 170, 190, 165, 172]
a = input('Введите рост нового человека (если хотите закончить, введите "Все построены"): ')
rost.sort(reverse=True)
while a not in ('Все построены', 'все построены', ''):
    rost.append(int(a))
    rost.sort(reverse=True)
    ind = rost.index(int(a))
    print(f'Текущий список: {rost}. Порядковый номер нового человека: {ind+1}.')
    a = input('Введите рост нового человека (если хотите закончить, введите "Все построены"): ')
print('Общий список роста людей в строю:', rost)
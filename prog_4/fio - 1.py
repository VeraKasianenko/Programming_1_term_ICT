'''
Создайте программу, заменяющую введенный пользователем текст в формате «Фамилия Имя Отчество» на текст в формате «Фамилия И.О.».
'''

name = list(map(str, input('Введите Фамилию, имя и отчество: ').split()))
print('ФИО в новом формате: ' + name[0] + ' ' + name[1][0] + '.' + name[2][0] + '.')
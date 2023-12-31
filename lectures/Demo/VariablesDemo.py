# Неизменяемые типы

a = 1
b = 2
c = "start"
print(a)
# идентификатор – это некоторое целочисленное значение, посредством которого
# уникально адресуется объект
print(id(a))
a = b
b = b + 1
print(id(a))
print(a)
print(type(a))
a = c
print(id(a))
print(a)
print(type(a))


# Изменяемые типы

list1 = [2, 3, 4]
print(id(list1))
list2 = list1
print(id(list2))
list1[1] = 33
print(list1)    # Переменная list1 изменилась
print(list2)    # Переменная list2 также изменилась
print(id(list1))

list3 = list1[:] # создается копия списка - получение среза от начала и до конца списка
list1[1] = 333
print(list1)    # Переменная list1 изменилась
print(list3)    # Переменная list3 не изменилась
print(id(list1))
print(id(list3))

list1 = list1 * 2
print(list1)
print(id(list1))

list1 = 8
print(list1)    # Переменная list1 изменилась
print(list2)    # Переменная list2 не изменилась
print(id(list1))
print(id(list2))


mylist = [11,22,33,44,55,66]
mylist.append(77) # функция, выполняющая непосредственные изменения в объектах
                  # следует вызывать без присваивания возвращаемого значения
print(mylist)
mylistnew = mylist.append(88) # возвращает None
print(mylistnew)              # None
print(mylist)

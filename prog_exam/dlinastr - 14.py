'''
Свяжите переменную с любой строкой, состоящей не менее чем из 8 символов. Извлеките из строки первый символ,
затем последний, третий с начала и третий с конца. Измерьте длину вашей строки.
'''

stroka = '123456780'
ln = len(stroka)
print(f'{stroka[0]+stroka[-1]+stroka[2]+stroka[ln-3]}\n'
      'Длина:', ln)
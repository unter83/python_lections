## Типы данных и переменные
# int, float, booleat, str, list, None
# value = None
a = 123 #int
b = 1.23 #float
s = 'hello world' #str    hello world
s = 'hello "world"' #str    hello "world"
s = "hello 'world'" #str    hello 'world'
l = [1,2,3] #list - список
value = None #Неизвестный тип данных
type(value) # Возвращает тип данных
k = list(range(10)) # Строка элементов от 0 до 9
k = list(range(2, 10)) # Строка элементов от 2 до 9
k = list(range(1, 10, 2)) # Строка элементов  1, 3, 5, 7, 9

for i in l:
    i *= 2
    print(i)       #2 4 6
print(l)             #1 2 3        

l.append(4)     #l = [1,2,3,4]
l.remove(2)     #l = [1,3,4]
del l[0]        #l = [3,4]


## Вывод данных

print(a) # Печатает в консоли содержимое переменной a
print(a, b, s) # Печатает в консоли содержимое переменных a, b, s
print('{1} {2} {0}'.format(a,b,s)) # Печатает в консоли содержимое переменных b, s, a
print(f'{a} * {b} * {s}') # Печатает в консоли содержимое переменных a, b, s в формате "a * b * s"

## Вывод данных и преобразование типов

a = input() # Запрос от пользователя ввода данных для переменной "a" в символьном формате
b = int(input()) # Запрос от пользователя ввода данных для переменной "b" в целочисленном формате
c = float(input()) # Запрос от пользователя ввода данных для переменной "c" в формате рационального числа

## Арифместические операции

c = a + b # Сложение
c = a - b # Вычитание
c = a * b # Умножение
c = a / b # Деление
c = a // b # Целочисленное деление
c = a % b # Остаток от деления
c = a ** b # Возведение a в степень b

a += 5 # a = a + 5
a -= 5 # a = a - 5
a /= 5 # a = a / 5
a *= 5 # a = a * 5

c = round(a / b) # Округление деления a / b до целого числа
c = round(a / b, 5) # Округление деления a / b до 5 знаков после запятой

## Логические операции

a = 1 > 3 # a = False
a = 3 == 3 # a = True
a = 9 != 3 # a = True
a = 1 < 3 < 5 < 10 # a = True


a = 1 < 4 and 5 > 2 # a = True
a = 1 > 2 or 4 < 6 # a = True

f = [1, 2, 3, 4]
print(2 in f) # Выведет True
print(not 2 in f) # Выведет False

is_odd = f[0] % 2 == 0
print(is_odd) # Выведет False

is_odd = not f[0] % 2
print(is_odd) # Выведет False

## Управляющие конструкции if if - else

# if (conditions):
    # operator 1
    # ...
    # operator n
# else:
    # operator n+1
    # operator ...
    # operator n+k

username = input('Введите имя')
if(username == 'Маша'):
    print('Ура это Маша!')
else:
    print('Привет,', username)

# if (conditions):
    # operator 1
    # ...
    # operator n
# elif:
    # operator n+1
    # operator ...
    # operator n+k
# elif:
    # operator n+k+1
    # operator ...
    # operator n+k+m
# else:
    # operator n+k+m+1
    # operator ...
    # operator n+k+m+t


## Управляющие конструкции while

# while (conditions):
    # operator 1
    # ...
    # operator n
# else:
    # operator n+1
    # ...
    # operator n+k
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Хватит')
print(inverted)

## Управляющие конструкции for

# for i in enumiration:
    # operator 1
    # ...
    # operator n4 

for i  in 1,2,3,4,5:
    print(i)
# 1 2 3 4 5
for i  in range(1,6):
    print(i)
# 1 2 3 4 5
for i  in range(1,10,2):
    print(i)
# 1 3 5 7 9
for i  in 'qwerty':
    print(i)
# q w e r t y

## Функции

# def function_name(x):
#     body line1
#     ...
#     body line_n
#     return

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

text = 'съешь ещё этих мягких французских булок'

print(len(text))                # 39
print('ещё' in text)            # True
print(text.isdigit())           # False
print(text.islower)             # True
print(text.replace('ещё', 'ЕЩЁ')) #съешь ЕЩЁ этих мягких французских булок

print(text[0])                  #с
print(text[1])                  #ъ
print(text[len(text)])          #IndexError
print(text[len(text)-1])        #к
print(text[-5])                 #б
print(text[:])                  #print(text)
print(text[:2])                 #съ
print(text[6:-18])              #ещё этих мягких



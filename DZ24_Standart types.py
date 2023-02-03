"""
Создать свой класс String на базе стандартного класса str.
В нём необходимо:
переопределить стандартный метод отвечающий за сложение
написать отсутствующий в классе str метод отвечающий за вычитание
Принцип работы сложения в новом классе String:
объект типа String можно складывать как друг с другом, так и с любым другим типом,
который может быть приведён к строковому типу.
"Под капотом" оба операнда приводятся к строковому типу и происходит конкатенация двух строк.
Результатом сложения будет объект нового класса String.
Примеры выполнения:
String('New') + String(890)    ->    'New890'
String(1234) + 5678            ->    12345678
String('New') + 'castle'       ->    'Newcastle'
String('New') + 77             ->    'New77'
String('New') + True           ->    'NewTrue'
String('New') + ['s', ' ', 23] ->    "New['s', ' ', 23]"
String('New') + None           ->    'NewNone'

Принцип работы вычитания в новом классе String:
из объекта типа String можно вычесть значение любого другого типа,
которое может быть приведёно к строковому типу.
"Под капотом" оба операнда приводятся к строковому типу и затем из первого операнда
убирается первое вхождение второго операнда, если таковое имеется.
Результатом вычитания будет объект нового класса String.
Если в первом операнде не находится значение второго операнда,
то результатом вычитания будет первый операнд без изменений.
Примеры выполнения:
String('New bala7nce') - 7               ->    'New balance'
String('New balance') - 'bal'            ->    'New ance'
String('New balance') - 'Bal'            ->    'New balance'
String('pineapple apple pine') - 'apple' ->    'pine apple pine'
String('New balance') - 'apple'          ->    'New balance'
String('NoneType') - None                ->    'Type'
String(55678345672) - 7                  ->    '5568345672'

*Важно! Результатом сложения или вычитания всегда будет объект типа String.
"""


class String(str):

    def __add__(self, other):
        adding = str(self) + str(other)
        return adding

    def __sub__(self, other):
        reduce = str(self).replace(str(other), '', 1)
        return reduce


c1 = String('New') + String(890)
c2 = String(1234) + 5678
c3 = String('New') + 'castle'
c4 = String('New') + 77
c5 = String('New') + True
c6 = String('New') + ['s', ' ', 23]
c7 = String('New') + None

print('result: ', c1, type(c1))
print('result: ', c2, type(c2))
print('result: ', c3, type(c3))
print('result: ', c4, type(c4))
print('result: ', c5, type(c5))
print('result: ', c6, type(c6))
print('result: ', c7, type(c7))
print('*' * 50)
k1 = String('New bala7nce') - 7
k2 = String('New balance') - 'bal'
k3 = String('New balance') - 'Bal'
k4 = String('pineapple apple pine') - 'apple'
k5 = String('New balance') - 'apple'
k6 = String('NoneType') - None
k7 = String(55678345672) - 7

print('result: ', k1, type(k1))
print('result: ', k2, type(k2))
print('result: ', k3, type(k3))
print('result: ', k4, type(k4))
print('result: ', k5, type(k5))
print('result: ', k6, type(k6))
print('result: ', k7, type(k7))
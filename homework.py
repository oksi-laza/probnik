print('Числа')
print(5)
print(type(5))    # 'int' - integer - целое число - неизменяемый тип данных
print(5 + 5)      # сложение чисел
print(5 - 5)      # вычитание чисел
print(5 * 5)      # умножение чисел
print(5 / 5)      # деление чисел. Возвращает ответ в виде дробного числа (число с плавающей точкой)
print(5 // 5)     # целочисленное деление чисел
print(5 % 5)      # остаток от деления
print(5 % 2)      # остаток от деления, можно проверить четное число или нет, при делении на 2.
print(5 ** 5)     # возведение в степень

print(2.0)
print(type(2.0))  # 'float' - дробное число (число с плавающей точкой) - неизменяемый тип данных
print(2.0 + 2.0)  # сложение чисел, получим тип 'float'
print(2.0 + 2)    # сложение чисел типа 'float' и 'int', получим тип 'float'. Также и с другими математическими действиями.


print('Строка')
print('Hello, World!')
print(type('Hello, World!'))    # 'str' - string - строка
print('Hello,' + ' World!')     # сложение строк. Единственная допустимая математическая операция для строк.
print('1' + '1')                # 'str' можно сложить (склеить) только с 'str'


print('Логический тип данных')
print(True, False)
print(type(True), type(False))  # 'bool' - boolean - логический тип данных или булевый тип данных(булеан)
print('1', 5 > 10)              # проверка выражения на истинность или ложность (верно/не верно)
print('2', 10 > 5)              # проверка выражения на истинность или ложность (верно/не верно)
print('3', 5 > 10, 10 > 5)      # print поддерживает множественный вывод через запятую, допустимо вводить значения разных типов данных
print('4', 5 <= 15)             # "<=" означает меньше или равно. Проверка выражения на истинность или ложность
print('5', 5 >= 15)             # ">=" означает больше или равно. Проверка выражения на истинность или ложность
print('6', 5 == 5)              # "==" означает равенство объектов. Проверка выражения на истинность или ложность
print('7', 5 != 5)              # "!=" означает НЕравенство объектов. Проверка выражения на истинность или ложность
print('8', 5 != 5 and 5 < 10)   # команда "and" подразумевает, что для "True" должны быть истинны оба выражения
print('9', 5 == 5 and 5 < 10)   # команда "and" подразумевает, что для "True" должны быть истинны оба выражения
print('10', 5 != 5 or 5 < 10)   # команда "or" подразумевает, что для "True" должны быть истинным хотя бы одно выражение


print('Изменение типа данных')
print(type(int('5')))           # сложная конструкция - первым делом срабатывает внутренняя команда 'int' - перевод типа данных в число, затем отображение типа данных 'type', а затем команда 'print'
# 1. Дано целое число (int). Определить сколько нулей в этом числе.
m_int = 3405607
m_int = str(m_int)
number = "0"
counted = m_int.count(number)

# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля
value = 1002000
value = str(value)
number = 0
for symbol in value:
    if int(symbol) == 0:
        number = number + 1
    else:
        number = 0

# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.

my_list_1 = "jpjppmp"
my_list_2 = "okapis"
my_result = my_list_1[::2] + my_list_2[1::2]

# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
my_list = "python"
new_list = my_list[1:] + my_list[:1]

# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

my_list = [1, 2, 3, 4]
value = my_list.pop(0)
my_list.append(value)

# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)
my_str = "43 больше чем 34 но меньше чем 56"
new_str = my_str.split()
sum1 = 0
for symbol in new_str:
    if symbol.isdigit():
        sum1 = sum1 + int(symbol)

#
# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin". (rfind, find - методы строк)
my_str = "My long string"
l_limit = "o"
r_limit = "g"
l_index = my_str.find(l_limit) + 1
r_index = my_str.rfind(r_limit)
sub_str = my_str[l_index: r_index]

# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)
my_str = "abcde"
result = []
for index, value in enumerate(my_str):
    if index % 2 == 0:
        couple = my_str[index:index + 2]
        if len(couple) > 1:
            result.append(couple)
        else:
            result.append(value + "_")

# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
my_list = [2, 4, 1, 5, 3, 9, 0, 7]
counter = 0
for index in range(1, len(my_list) - 1):
    if my_list[index] > sum([my_list[index - 1], my_list[index + 1]]):
        counter = 1 + counter

# 10. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33]
# Создать новый список в который поместить только строки из my_list.
my_list = [1, 2, 3, "11", "22", 33]
result_list = []
for value in my_list:
    if isinstance(value, str):
        result_list.append(value)

#
# 11. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке ТОЛЬКО ОДИН раз.
my_str = "trollo"
my_list = []
my_set = set(my_str)
for symbol in my_set:
    amount = my_str.count(symbol)
    if amount == 1:
        my_list.append(symbol)


#
# 12. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
my_str_1 = "qwerty"
my_str_2 = "qryip"
my_list = []
for symb_1 in my_str_1:
    for symb_2 in my_str_2:
        if symb_1 == symb_2:
            my_list.append(symb_1)
my_list = list(set(my_list))

#
# 13. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой ТОЛЬКО ПО ОДНОМУ разу.
# Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"], т.к. эти символы есть в каждой строке по одному разу
my_str1 = "aaaasdf1"
my_str2 = "asdfff2"
common_elements = list(set(my_str1) & set(my_str2))
unique_common_elements = []

for element in common_elements:
    if my_str1.count(element) == 1 and my_str2.count(element) == 1:
        unique_common_elements.append(element)

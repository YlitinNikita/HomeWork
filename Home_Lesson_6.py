# 1) У вас есть список my_list с значениями типа int.
# Распечатать те значения, которые больше 100.
# Задание выполнить с помощью цикла for.

# my_list = [120, 110, 90, 80]
# for number in my_list:
#     if number > 100:
#         print(number)
# # # # # # # # # # # # # # # # # # # # # # #


# 2) У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results.
# Задание выполнить с помощью цикла for.


# my_list = [120, 110, 90, 80]
# my_results = []
# for number in my_list:
#     if number > 100:
#         my_results.append(number)
# print(my_results)
# # # # # # # # # # # # # # # # # # # # # # #


# 3) У вас есть список my_list с значениями типа int.
# Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
# Количество элементов в списке можно получить с помощью функции len(my_list)

#
# my_list = [1,2,3,4]
# if len(my_list) < 2:
#     my_list.extend({0})
# else:
#     my_list.append(sum(my_list[-2:]))
# print(my_list)
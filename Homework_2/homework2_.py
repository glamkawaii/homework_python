
# 1 Перевести число, введенное пользователем, в байты или килобайты в зависимости от его выбора
# user_number = int(input('Add number: '))
# local_copy = user_number
# while (local_copy):
#     print(local_copy & 1)
#     local_copy = local_copy >> 1

# 2
# def get_sum_and_product(number):
#     sum_ = 0
#     product_ = 1
#     divisor = 10
#     remains = number
#
#     while remains:
#         next_num = remains % divisor  # getting remains of division
#         sum_ += next_num              # summing - sugar for sum_ = sum_ + next_num
#         product_ *= next_num
#         remains = remains // divisor  # integer division
#         print(next_num)
#
#     return (sum_, product_)
#
#
# print(get_sum_and_product(1234))

# 3 Вывести таблицу значений функции y = -1.24x2 + x. Значения аргумента (x) задаются минимумом, максимумом и шагом
# ? func params: min - max - step - a cycle inside

# 4 Является ли число палиндромом
# is_palindrome_or_not = int(input('Input number: '))
#
# def ispalindrome(number):
#     number_list = []
#     divisor = 10
#     remains = number
#     while remains:
#         next_num = remains % divisor  # getting remains of division
#         remains = remains // divisor  # integer division
#         number_list.append(next_num)
#     x = 0
#     while x < len(number_list)//2:
#         if number_list[x] != number_list[-x-1]:
#             return (False)
#         x += 1
#
#
#     return (True)
#
# print(ispalindrome(is_palindrome_or_not))



# 5 Найти среднее арифметическое положительных элементов линейного массива

# def positive_average(num_list):
#     positives = [x for x in num_list if x > 0]  # my big love, list comprehension
#     return sum(positives) / len(positives)
#
# print(positive_average([1, -1, 2]))

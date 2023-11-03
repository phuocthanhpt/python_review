import random
import string
import os

# def random_string_using_choices():
#     domain = "email.com"
#     N = 10
#     random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))
#     random_email = random_str + "@" + domain
#     print(random_email)
#
#
# random_string_using_choices()


# directory = os.getcwd()
# print(directory)

# summation = 0
# for i in range(1, 6):
#     summation = summation + i
# print(summation)

# for k in range(1, 10, 2):
#     print(k)


# for i in range(10):
#     print(i)

# obj = [2, 4, 6, 7, 9, 22]
# for i in obj:
#     print(i)


it = 10
while it > 1:
    if it == 9:
        it = it - 1
        continue
    if it == 3:
        break
    print(it)
    it = it - 1


def add_number():
    pass

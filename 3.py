#21
print("==============================")
def custom_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result
print(custom_map(lambda x: x * 2, [1, 2, 3]))
#22
print("==============================")

def custom_zip(list1, list2):
    result = []

    min_length = min(len(list1), len(list2))

    for i in range(min_length):
        result.append((list1[i], list2[i]))

    return result
print(custom_zip([1,2,3], ["a", "b", "c"]))
#23
print("==============================")
def custom_reversed(sequence):
    result = []
    for i in range(len(sequence) - 1, -1, -1):
        result.append(sequence[i])
    return result
print(custom_reversed([1, 2, 3]))

#24
print("=============================")

def custom_sorted(iterable, reverse=False):

    lst = list(iterable)
    n = len(lst)

    for i in range(n):
        for j in range(0, n - i - 1):

            if not reverse:
                condition = lst[j] > lst[j + 1]
            else:
                condition = lst[j] < lst[j + 1]

            if condition:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst
print(custom_sorted([1, 2, 3,9,7,3]))

#25
print("=============================")


def sum_digits(n):
    n = abs(n)
    total_sum = 0

    while n > 0:
        total_sum += n % 10
        n //= 10

    return total_sum
print(sum_digits(10789))

#26
print("=============================")

def count_vowels(text):
    vowels = 'aeiouAEIOU'
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count
print(count_vowels("Hello World") )

#27
print("=============================")
def power(base, exp):
    result = 1

    for _ in range(exp):
        result *= base
    return result
print(power(2, 9))

#28
print("=============================")


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
print(is_prime(19))

#29
print("=============================")
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(6))

#30
print("=============================")


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b
print(fibonacci(6))
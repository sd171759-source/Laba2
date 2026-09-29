
Задание 1

```python
def convert_types(data):
    result = []
    for item in data:
        if isinstance(item, bool):
            result.append(str(item))

        elif isinstance(item, (int, float)):
            result.append(str(item))

        elif isinstance(item, str):
            try:
                result.append(int(item))
            except ValueError:
                result.append(item)

        else :
            result.append(str(item))
    return result
print(convert_types([1, "2", 'Yammo', 5.6]))
```
Вывод : ['1', 2, 'Yammo', '5.6']
#
Задание 2

```python
def swap_values(a, b):
  
    a, b = b, a
    return (a, b)

print(swap_values(5, 10))
```
Вывод: (10, 5)
#
Задание 3

````python
def bool_transform(value):
    if value:
        return True
    else:
        return False
print(bool_transform(5))
print(bool_transform(0))
print(bool_transform(""))
````
Вывод: True
False
False
#
Задание 4

````python
def compound_operations(a, b):
    results = []

    x = a; x += b;results.append(round(x, 2) if isinstance(x, float) else x)

    x = a;x -= b;results.append(round(x, 2) if isinstance(x, float) else x)

    x = a;x *= b;results.append(round(x, 2) if isinstance(x, float) else x)

    x = a;  x /= b;results.append(round(x, 2) if isinstance(x, float) else x)

    x = a;x //= b;results.append(round(x, 2) if isinstance(x, float) else x)

    x = a; x %= b;results.append(round(x, 2) if isinstance(x, float) else x)

    x = a;x **= b;results.append(round(x, 2) if isinstance(x, float) else x)

    return results


print(compound_operations(78, 4))
````
Вывод: [82, 74, 312, 19.5, 19, 2, 37015056]
#
Задание 5

````python
def check_type(value, expected_type):
    return type(value).__name__ == expected_type
print(check_type(6, 'int'))
print(check_type('9', 'int'))
````
Вывод: True False
#
Задание 6
````python
def logical_and(a, b, c):
    if a:
        if b:
            if c:
                return True
    return False
print(logical_and(True, 5, "t"))
print(logical_and(True, 0, "x"))
````
Вывод: True False
# 
Задание 7
````python
def logical_or(a, b, c):
    if a:
        return True
    if b:
        return True
    if c:
        return True
    return False

print(logical_or(0, "", False))  
print(logical_or(0, 5, False))  
````
Вывод:False True
#
Задание 8
````python
def is_between(value, low, high):
    if value >= low and value <= high:
        return True
    else:
        return False

print(is_between(15, 1, 10))
````
Вывод:True False
#
Задание 9
````python
def print_even_numbers(n):
    
    for i in range(2, n + 1, 2):
        print(i)

print_even_numbers(10)
````
Вывод:2
4
6
8
10

#
Задание 10
````python
def countdown_while(n):
    while n > 0:
        print(n)
        n -= 1

countdown_while(5)
````
Вывод: 5
4
3
2
1
#
Задание 11
````python
def skip_multiples(n, multiple):
    for i in range(1, n + 1):
        if i % multiple == 0:
            continue
        print(i)
skip_multiples(10, 3)
````
Вывод:1
2
4
5
7
8
10
#
Задание 12
````python
def if_elif_else_chain(x):
    if x > 0:
        return "positive"
    elif x < 0:
        return "negative"
    else:
        return "zero"

result1 = if_elif_else_chain(5)
print(result1)
````
Вывод:positive
#
Задание 13
````python
def abs_value(x):
    if x < 0:
        return -x
    return x
a=abs_value(-10)
print(a)
````
Вывод:10
#
Задание 14
````python
def binary_representation(n):
    if n == 0:
        return "0"

    result = ""
    while n > 0:
        remainder = n % 2
        result = str(remainder) + result
        n //= 2
    return result
print(binary_representation(10))
print(binary_representation(0))
````
Вывод:1010
0
#
Задание 15
````python
def custom_round(number, ndigits):
    factor = 10 ** ndigits

    shifted = number * factor
    if shifted >= 0:
        rounded = int(shifted + 0.5)
    else:
        rounded = int(shifted - 0.5)

    result = rounded / factor

    return float(result) if ndigits == 0 else result
print(custom_round(3.14159, 2) )
print(custom_round(9.5, 0) )
````
Вывод:3.14
10.0
#
Задание 16
````python
def find_max_min(numbers):
    if not numbers:
        return None

    max_value = numbers[0]
    min_value = numbers[0]

    for num in numbers:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num

    return (max_value, min_value)
print(find_max_min([ 2, 3, 5, 7, 8, 1]))
````
Вывод:(8, 1)
#
Задание 17
````python
def all_true(iterable):
    for item in iterable:
        if not item:
            return False
    return True
print(all_true([1, 2, 3, 4, 5]))
print(all_true([0,1,2]))
````
Вывод:True
False
#
Задание 18
````python
def any_true(iterable):
    for item in iterable:
        if item:
            return True
    return False
print(any_true([0,'',False]))
print(any_true([0,5,False]))
````
Вывод:False
True
#
Задание 19
````python
def custom_enumerate(sequence, start=0):
    result = []
    current_index = start
    for element in sequence:
        result.append((current_index, element))
        current_index += 1
    return result
print(custom_enumerate(['a', 'b', 'c'], start=1))
````
Вывод:[(1, 'a'), (2, 'b'), (3, 'c')]
#
Задание 20
````python
def custom_filter(func, iterable):
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result
print(custom_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) )
````
Вывод:[2, 4]
#
Задание 21
````python
def custom_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result
print(custom_map(lambda x: x * 2, [1, 2, 3]))
````
Вывод:[2, 4, 6]
#
Задание 22
````python
def custom_zip(list1, list2):
    result = []

    min_length = min(len(list1), len(list2))

    for i in range(min_length):
        result.append((list1[i], list2[i]))

    return result
print(custom_zip([1,2,3], ["a", "b", "c"]))
````
Вывод:[(1, 'a'), (2, 'b'), (3, 'c')]
#
Задание 23
````python
def custom_reversed(sequence):
    result = []
    for i in range(len(sequence) - 1, -1, -1):
        result.append(sequence[i])
    return result
print(custom_reversed([1, 2, 3]))
````
Вывод:[3, 2, 1]
#
Задание 24
````python
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
````
Вывод:[1, 2, 3, 3, 7, 9]
#
Задание 25
````python
def sum_digits(n):
    n = abs(n)
    total_sum = 0

    while n > 0:
        total_sum += n % 10
        n //= 10

    return total_sum
print(sum_digits(10789))
````
Вывод:25
#
Задание 26
````python
def count_vowels(text):
    vowels = 'aeiouAEIOU'
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count
print(count_vowels("Hello World") )

````
Вывод:3
#
Задание 27
````python
def power(base, exp):
    result = 1

    for _ in range(exp):
        result *= base
    return result
print(power(2, 9))
````
Вывод:512
#
Задание 28
````python
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
print(is_prime(19))

````
Вывод:True
#
Задание 29
````python
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(6))
````
Вывод:720
#
Задание 30
````python
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
````
Вывод:8
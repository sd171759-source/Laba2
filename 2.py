#11
print("==============================")
def skip_multiples(n, multiple):
    for i in range(1, n + 1):
        if i % multiple == 0:
            continue
        print(i)
skip_multiples(10, 3)
print("==============================")
#12
def if_elif_else_chain(x):
    if x > 0:
        return "positive"
    elif x < 0:
        return "negative"
    else:
        return "zero"

result1 = if_elif_else_chain(5)
print(result1)
print("==============================")
#13
def abs_value(x):
    if x < 0:
        return -x
    return x
a=abs_value(-10)
print(a)
print("==============================")
#14
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
print("==============================")
#15
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
print("==============================")
#16
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
print("==============================")
#17
def all_true(iterable):
    for item in iterable:
        if not item:
            return False
    return True
print(all_true([1, 2, 3, 4, 5]))
print(all_true([0,1,2]))
print("==============================")
#18
def any_true(iterable):
    for item in iterable:
        if item:
            return True
    return False
print(any_true([0,'',False]))
print(any_true([0,5,False]))
print("==============================")
#19
def custom_enumerate(sequence, start=0):
    result = []
    current_index = start
    for element in sequence:
        result.append((current_index, element))
        current_index += 1
    return result
print(custom_enumerate(['a', 'b', 'c'], start=1))
print("==============================")
#20
def custom_filter(func, iterable):
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result
print(custom_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) )
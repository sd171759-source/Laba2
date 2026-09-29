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


def swap_values(a, b):

    a, b = b, a
    return (a, b)

print(swap_values(5, 10))

def bool_transform(value):
    if value:
        return True
    else:
        return False
print(bool_transform(5))
print(bool_transform(0))
print(bool_transform(""))


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


def check_type(value, expected_type):
    return type(value).__name__ == expected_type
print(check_type(6, 'int'))
print(check_type('9', 'int'))

def logical_and(a, b, c):
    if a:
        if b:
            if c:
                return True
    return False
print(logical_and(True, 5, "t"))
print(logical_and(True, 0, "x"))


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

def is_between(value, low, high):
    if value >= low and value <= high:
        return True
    else:
        return False

print(is_between(15, 1, 10))

def print_even_numbers(n):

    for i in range(2, n + 1, 2):
        print(i)

print_even_numbers(10)

def countdown_while(n):
    while n > 0:
        print(n)
        n -= 1

countdown_while(5)
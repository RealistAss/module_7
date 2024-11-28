def add_everything_up(a, b):
    try:
        i = (a + b)
    except TypeError:
        i = str(a) + str(b)
    return i

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
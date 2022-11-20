def is_factor(a, b):
    if b % a == 0:
        return True
    else:
        return False


z = input('Enter a number: ')
x = input('Enter the number factor: ')

print(is_factor(int(x), int(z)))

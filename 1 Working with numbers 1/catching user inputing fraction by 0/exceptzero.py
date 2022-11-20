from fractions import Fraction


try:
    a = Fraction(input('Enter a fraction: \n'))
except ZeroDivisionError:
    print('Invalid fraction')

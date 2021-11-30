from main import Complex

first_num = complex(input("Введіть перше число: "))
operator = input("Введіть знак: ")
second_num = complex(input("Введіть друге число: "))
number1 = Complex(first_num)
number2 = Complex(second_num)

if operator == '+':
    print(number1 + number2)
elif operator == '-':
    print(number1 - number2)
elif operator == '*':
    print(number1 * number2)
elif operator == '/':
    print(number1 / number2)
elif operator == '+=':
    number1 += number2
    print(number1)
elif operator == '-=':
    number1 -= number2
    print(number1)
elif operator == '*=':
    number1 *= number2
    print(number1)
elif operator == '/=':
    number1 /= number2
    print(number1)

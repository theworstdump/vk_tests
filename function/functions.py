from MyException.MyError import MyError


def func_1(x: int):
    return x * x

def func_2(text: str) -> str:
    return text.upper()

def func_3(number: int) -> int:
    return number % 3

#Функция возвращает True, если переданная строка написана с заглавной буквы, и False, если первая буква строчная
def func_4(text: str) -> bool:
    if (text[0] == text[0].upper()):
        return True
    else:
        return False

def func_5(number: int) -> bool:
    if (number <= 0) or (number == 1):
        raise MyError('Wrong input. Enter natural numbers starting from number 2')
    k = 0
    for i in range(2, number-1):
        if number % i == 0:
            k = k + 1
    if k == 0:
        return True
    else:
        return False

def f():
    raise SystemExit(1)

if __name__ == '__main__':
    print(func_3(7))
    print(func_3(-100))
    print(func_4('Abc'))
    print(func_4('bc'))
    print(func_5(1))


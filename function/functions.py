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


if __name__ == '__main__':
    print(func_3(7))
    print(func_3(-100))
    print(func_4('Abc'))
    print(func_4('bc'))


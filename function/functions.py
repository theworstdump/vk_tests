def func_1(x: int):
    return x * x

def func_2(text: str):
    return text.upper()

def func_3(number: int) -> int:
    return number % 3

if __name__ == '__main__':
    print(func_3(7))
    print(func_3(-100))


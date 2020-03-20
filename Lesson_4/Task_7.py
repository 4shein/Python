""""
Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение.  При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fibo_gen().
Функция отвечает за получение факториала числа, а в цикле необходимо выводить
только первые 15 чисел.
Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
def fibo_gen():
    for el in range(1, 15, 1):
        yield el


def recursiveFactorial(n):
    if (n == 0):
        return 1
    else:
        return recursiveFactorial(n - 1) * n


for el in fibo_gen():
    print(recursiveFactorial(el))
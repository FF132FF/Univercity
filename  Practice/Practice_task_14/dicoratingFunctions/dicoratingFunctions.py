import time


def test_time(fn):
    def wrapper(*args):
        st = time.time()
        fn(*args)
        dt = time.time() - st
        print(f"Время работы: {dt} сек")

    return wrapper


N = int(input("Введите любой целое число: "))
num_list: list = []
num_list_comprehension: list = []


@test_time
def get_list(n):
    for i in range(n):
        if i % 2 == 0:
            num_list.append(i)

    return num_list


@test_time
def get_list_comprehension(n):
    num_list_comprehension = [i for i in range(n) if i % 2 == 0]
    return num_list_comprehension


print("       Вывод функции get_list():\n")
print(get_list(N))

print("  =================================")
print("       Вывод функции get_list():\n")
print(get_list_comprehension(N))

print("  =================================")
first_test = test_time(get_list)
print("       Для функции get_list():\n")
first_test(N)

print("  =================================")
second_test = test_time(get_list_comprehension)
print("       Для функции get_list_comprehension():\n")
second_test(N)
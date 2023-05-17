import time

def testTime(fn):
    def wrapper(*args):
        st = time.time()
        fn(*args)
        dt = time.time() - st
        print(f"Время работы: {dt} сек")

    return wrapper

@testTime
def getList(n):
    numList: list = []
    for i in range(n):
        if i % 2 == 0:
            numList.append(i)
    return numList

@testTime
def getListComprehension(n):
    numListComprehension = [i for i in range(n + 1) if i % 2 == 0]
    return numListComprehension


N = int(input("Введите число: "))

print("  ============================================")
print("        Для функции get_list():")
getList(N)

print("  ============================================")
print("        Для функции get_list_comprehension():")
getListComprehension(N)
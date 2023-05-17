def cachingDecorator(fn):
    cache = {}

    def wrapper(N):

        if N in cache:
            return cache[N]

        if not cache:
            for i in range(min(2, N + 1)):
                cache[i] = i

        for i in range(len(cache), N + 1):
            cache[i] = cache[i-1] + cache[i-2]

        print(f"last cached number is {cache[N]}")
        return cache[N]

    return wrapper


@cachingDecorator
def fibCaching(N):
    return N if N == 0 or N == 1 else fibCaching(N - 1) + fibCaching(N - 2)

N = int(input("Введите число: "))
oldN = int(input("Введите то же число, что и в первый раз: "))
newN = int(input("Введите число, которое превышает первое по значению: "))

print("  ===========")
print(fibCaching(N))
print("  ===========")
print(fibCaching(oldN))
print("  ===========")
print(fibCaching(newN))
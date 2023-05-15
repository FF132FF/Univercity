import re
import ssl
import urllib.request

ssl._create_default_https_context: str = ssl._create_unverified_context

url: str = "https://quke.ru/shop/smartfony/apple?page-size=72"
response: str = urllib.request.urlopen(url).read().decode()

namePattern: str = r"(?:\d\"\,\s+\"name\"\:\s\")([^\"]*)"
name: list = re.findall(namePattern, response)

pricePattern: str = r"(?:\"price\"\:\s)([^\n]*)"
price: list = re.findall(pricePattern, response)

namePriceList: list = []

for i in range(len(name) - 1):
    namePriceList.append([name[i], int(price[i])])

print(namePriceList)

numOfPhones: int = 0
sumOfPrices: int = 0
minPrice: int = 1000000
maxPrice: int = 0

for i in namePriceList:

    if i[1] > maxPrice:
        maxPrice = i[1]

    if i[1] < minPrice:
        minPrice = i[1]

    numOfPhones += 1
    sumOfPrices += i[1]

averagePrice: float = sumOfPrices / numOfPhones
print("  ===========")
print(f"Средняя цена всех смартфонов: {round(averagePrice, 1)}")

for i in namePriceList:

    if i[1] == maxPrice:
        print("  ===========")
        print(f"Самый дорогой смартфон: {i}")

    if i[1] == minPrice:
        print("  ===========")
        print(f"Самый дешевый смартфон: {i}")

print("  ===========")
print(namePriceList)


catalog = open("catalog.txt", "w")

for i in namePriceList:
    catalog.write(' | '.join(str(s) for s in i) + '\n')

catalog.close()

main: list = [["Название смартфона", "Цена в рублях"]]
namePriceListCsv: list = main + namePriceList
print("  ===========")
print(namePriceListCsv)

catalogCsv = open("catalog.csv", "w", encoding='utf-8')

for i in namePriceListCsv:
    catalogCsv.write(' | '.join(str(s) for s in i) + '\n')

catalogCsv.close()
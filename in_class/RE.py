# . - любой одиночный символ
# [ ] - любой из них, диапазон
# $ - конец строки
# ^ - начало строки
# \ - экранирование
# \d - любая цифра
# \D - все что угодно, кроме цифр
# \s - пробелы
# \S - все кроме пробелов
# \w - буквы
# \W - все кроме букв
# \b - граница слова
# \B - не граница
#
# Квантификация
# n{4} - искать n подряд 4 раза
# n{4,6} - искать n от 4 до 6
# * от нуля и выше
# * от 1 и выше
# ? - нуль или 1 раз

import re
import ssl
import urllib.request


ssl._create.default_https_context = ssl._create_unverified_context
tel_nums = urllib.request.urlopen("https://www.summet.com/dmsi/html/codesamples/addresses.html").read().decode()
#tel_nums = "(900) 151-6230 asdfsfjsagas (514) 444-7777"
print(tel_nums)

pattern = (r"\(\d+\)\s\d+-\d+")
match = re.findall(pattern, tel_nums)

print(match)
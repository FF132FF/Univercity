import re

# re.search(pattern, string) pattern;


string = 'РўРµР»РµС„РѕРЅ 123-12-12'
pattern = r'\d\d\D\d\d'

match = re.search(pattern, string)
print(match[0] if match else 'Not found')

string = 'РўРµР»РµС„РѕРЅ 1231212'
pattern = r'\d\d\D\d\d'
match = re.search(pattern, string)
print(match[0] if match else 'Not found')


# re.fullmatch(pattern, string) pattern;

string = '12-12'
pattern = r'\d\d\D\d\d'

match = re.fullmatch(pattern, string)
print('YES' if match else 'NO')

string = 'Рў. 12-12'
pattern = r'\d\d\D\d\d'

match = re.fullmatch(pattern, string)
print('YES' if match else 'NO')


# re.split(pattern, string, maxsplit=0) str.split(), pattern;

string = 'РЇ РїРѕРјРЅСЋ С‡СѓРґРЅРѕРµ РјРіРЅРѕРІРµРЅСЊРµ'
pattern = r'\W+'

print(re.split(pattern, string))


# re.findall(pattern, string)	string,

string = 'Р­С‚Р° СЃС‚СЂРѕРєР° РЅР°РїРёСЃР°РЅР° 19.01.2018, Р° РјРѕРіР»Р° Р±С‹ Рё 01.09.2017'
pattern = r'\d\d\.\d\d\.\d{4}'

print(re.findall(pattern, string))


# re.sub(pattern, repl, string, count=0) string pattern repl;

string = 'Р­С‚Р° СЃС‚СЂРѕРєР° РЅР°РїРёСЃР°РЅР° 20.11.2022, Р° РјРѕРіР»Р° Р±С‹ Рё 22.11.2022'
pattern = r'\d\d\.\d\d\.\d{4}'

print(re.sub(pattern, r'DD.MM.YYYY', string))
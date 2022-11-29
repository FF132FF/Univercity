# РџРѕРґСЂРѕР±РЅРѕ Рѕ СЂРµРіСѓР»СЏСЂРЅС‹С… РІС‹СЂР°Р¶РµРЅРёСЏС…: https://clck.ru/H3xmB
# РћС‚Р»Р°РґРєР° https://regex101.com/

# РћСЃРЅРѕРІС‹:
# . - Р»СЋР±РѕР№ РѕРґРёРЅРѕС‡РЅС‹Р№ СЃРёРјРІРѕР»
# [ ] - Р»СЋР±РѕР№ РёР· РЅРёС…, РґРёР°РїР°Р·РѕРЅС‹
# $ - РєРѕРЅРµС† СЃС‚СЂРѕРєРё
# ^ - РЅР°С‡Р°Р»Рѕ СЃС‚СЂРѕРєРё
# \ - СЌРєСЂР°РЅРёСЂРѕРІР°РЅРёРµ
# \d - Р»СЋР±СѓСЋ С†РёС„СЂСѓ
# \D - РІСЃРµ С‡С‚Рѕ СѓРіРѕРґРЅРѕ, РєСЂРѕРјРµ С†РёС„СЂ
# \s - РїСЂРѕР±РµР»С‹
# \S - РІСЃРµ РєСЂРѕРјРµ РїСЂРѕР±РµР»РѕРІ
# \w - Р±СѓРєРІР°
# \W - РІСЃРµ РєСЂРѕРјРµ Р±СѓРєРІ
# \b - РіСЂР°РЅРёС†Р° СЃР»РѕРІР°
# \B - РЅРµ РіСЂР°РЅРёС†Р°
#
# РљРІР°РЅС‚РёС„РёРєР°С†РёСЏ
# n{4} - РёСЃРєР°С‚СЊ n РїРѕРґСЂСЏРґ 4 СЂР°Р·Р°
# n{4,6} - РёСЃРєР°С‚СЊ n РѕС‚ 4 РґРѕ 6
# * РѕС‚ РЅСѓР»СЏ Рё РІС‹С€Рµ
# + РѕС‚ 1 Рё РІС‹С€Рµ
# ? - РЅСѓР»СЊ РёР»Рё 1 СЂР°Р·

import re
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

tel_nums = urllib.request.urlopen("https://www.summet.com/dmsi/html/codesamples/addresses.html").read().decode()
print(tel_nums)


# match = pattern.findall(tel_nums)
# print(match)

#
#
# pattern = r"(?:<li>)(?P<names>[^<]*)(?:<[^>]*>)(?P<street>[^<]*)(?:<[^>]*>)(?P<state>[^<]*)(?:<[^>]*>)(?P<numbers>[^<]*)"

# name_pattern = r"(?:(?:<li>)(\w+ \w+\b[^<]*))
# street_pattern = r"(?:>)((?:P.O.|Ap|\d+)[^<]*)"
# state_pattern = r"(?:/>)([^(?:P.O.|Ap|\d+)][^<]*)"
# or
# state_pattern = r"((?:[^>]*)(?:\b[\d]{5}\b))"
# num_pattern = r"(\(\d{3}\) \d{3}-\d{4})"

# match = re.findall(pattern, tel_nums)
# match = re.finditer(pattern, tel_nums)

# match = ["".join(x) for x in pattern.findall(tel_nums)]

#
# response = urllib.request.urlopen("https://msk.spravker.ru/avtoservisy-avtotehcentry").read().decode()
# print(response)

# pattern = r"(?:class=\"org-widget\-header__title-link\">[^\w]*|<span class=\"org-widget\-header__meta org-widget\-header__meta\--location\">[^\w]*|<dt class=\"spec__index\"><span class=\"spec__index-inner\">РўРµР»РµС„РѕРЅ</span></dt>\n*\s*<dd class=\"spec__value\">[^\w]*|<dt class=\"spec__index\"><span class=\"spec__index-inner\">Р§Р°СЃС‹ СЂР°Р±РѕС‚С‹</span></dt>\n*\s*<dd class=\"spec__value\"[^\w]*>)(?P<value>[^<]*\b)"
# match = re.findall(pattern, response)
# match = [match[i:i+4] for i in range(0, len(match), 4)]
# print(match)
import re
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context
response: str = urllib.request.urlopen("https://msk.spravker.ru/avtoservisy-avtotehcentry").read().decode()

title_pattern: str = r"(?:title-link\">)([^<]*)"
location_pattern: str = r"(?:location\">\n+\s+)([^\n]+)"
tel_num_pattern: str = r"(?:Телефон.+\s+<dd class=\"spec__value\">)([^<]+)"
open_time_pattern: str = r"(?:\">Часы работы.+\s+<dd class=\"spec__value\">)([^<]+)"

match_name: list = re.findall(title_pattern, response)
match_location: list = re.findall(location_pattern, response)
match_tel_num: list = re.findall(tel_num_pattern, response)
match_open_time: list = re.findall(open_time_pattern, response)

result_list: list = []

for i in range(len(match_name) - 1):
    result_list.append([match_name[i], match_location[i], match_tel_num[i], match_open_time[i]])

for i in range(len(result_list) - 1):
    print(result_list[i])

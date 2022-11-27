import Getter

new_list: list = Getter.get_name("Python")
Getter.printlist(new_list)

newer_list: list = Getter.get_list(new_list)
print(newer_list)

newest_list = Getter.get_totals(newer_list)
print(newest_list)
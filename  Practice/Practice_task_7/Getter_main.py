import Getter

print("\n==== File name with converted data : ")
print(Getter.converter())

print("\n==== Generated list of book elements: ")
print(Getter.creating_a_list_of_books_elements())

keyword: str = "python"     #str(input("\n==== Write the keyword in lowercase for which you want to find matches: "))
print("\n==== Keyword matches found in this lists: ")
print(Getter.get_books(keyword))

print("\n==== Create a new format list (isbn, quantity * price): ")
print(Getter.get_totals(Getter.creating_a_list_of_books_elements()))
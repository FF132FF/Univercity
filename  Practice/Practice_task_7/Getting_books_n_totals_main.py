import Getting_books_n_totals

print("\n==== Generated list of book elements: ")
print(Getting_books_n_totals.get_list())

keyword: str = "Python"  # str(input("\n==== Write the keyword in lowercase for which you want to find matches: "))
print("\n==== Keyword matches found in this lists ( Keyword ->", keyword, "): ")

print(Getting_books_n_totals.get_books(keyword))

print("\n==== Create a new format list ( Format -> [(isbn, quantity * price)] ): ")
print(Getting_books_n_totals.get_totals(Getting_books_n_totals.get_list()))

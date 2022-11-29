a = set()

print(a)
print(type(a))

b = {}
print(type(b))

b = {"self", 1, (1,2, 3)}
print(b)
print(type(b))

b = set(("self", 1, (1,2, 3)))
print(b)
print(type(b))

a.add(2)
print(a)

a.update((3,4,5,6))
print(a)


list_1 = [1,2,3]
dict = {"one": 1}

#a.add(list)
#print(a)

#a.add(dict)
#print(a)


print(set(list_1))
print(set(dict))


set1 = {1, 2, 3, 4, 'a', 'p'}
print(set1)

set1.remove(2)
print(set1)



set1 = {1, 3, 4, 'a', 'p'}
print(set1)

set1.discard('a')
print(set1)

set1.discard(6)
print(set1)


set1 = {1, 2, 3, 4}
set1.pop()
a = set1.pop()
print(set1, a)



num_set = {1 ,3, 5, 7, 9, 10}
print(num_set)

print(7 in num_set)
print(1 not in num_set)


print(len(num_set))

new_set = num_set.copy()
print(len(new_set))

num_set.clear()
print(num_set)

del num_set


A = {1, 2, 3}
B = {2, 3, 4, 5}
C = A | B
C = A.union(B)
print(C)


A = {1, 2, 3, 4}
B = {3,4,5,6}
C = A & B
C = A.intersection(B)
print(C)

A = {1, 2, 3, 4}
B = {3,4,5,6}
C = A - B
C = A.difference(B)
print(C)


C = A ^ B
C = A.symmetric_difference(B)
print(C)


A = {1, 2, 3, 4, 5}
B = {2,3,4}
print(B <= A)
print(B.issubset(A))


A = {1, 2, 3, 4, 5}
B = {2,3,4}
print(A >= B)
print (A.issuperset(B))



List1 = [1, 2, 3, 5, 3, 2, 4, 7]
print(List1)

List_without_duplicate = set(List1)
List1 = list(List_without_duplicate)
print(List1)


List1 = list(set(List1))
print(List1)
v={'A', 'C', 4, False}
list_v = ['A', 'C', 4, False, 'A']
another_v = set(list_v)
print(list_v)
list_vv = list(another_v)
print(list_vv)
print(list(set(list_v)))
print(len(another_v))
print(False in v)
first_set = {1,2,3,4,5}
second_set = {3,4,5,6,7}
third_set = {3,4,5}
print(first_set.isdisjoint(second_set))
print(third_set.issubset(first_set))
print(third_set<=first_set)
print(second_set.issuperset(third_set)) # >=
print(v.issuperset(another_v))
fourth_set = first_set.intersection(second_set)
print(fourth_set)
fifth_set = first_set.union(second_set)
print(fifth_set)
sixth_set = fifth_set.difference(fourth_set)
print(sixth_set)
seventh_set = fifth_set.symmetric_difference(fourth_set)
print(seventh_set)
eight_set = seventh_set.copy()
print(eight_set)
eight_set.update(v)
print(eight_set)
third_set.intersection_update(v)
print(third_set)
fifth_set.difference_update(v)
print(fifth_set)
second_set.symmetric_difference_update(v)
print(second_set)
second_set.add(17)
second_set.remove(False)
print(second_set)
second_set.discard(11)
print(second_set)
exactly_new_set = second_set.pop()
print(exactly_new_set)
second_set.clear()
print(second_set)
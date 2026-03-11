"""
New and Useful Methods for List, Tuple, Set, and Dictionary in Python
Focusing on methods from Python 3.8+ and some less commonly known ones
"""

print("=" * 60)
print("DICTIONARY METHODS (Python 3.8+)")
print("=" * 60)

# 1. Dictionary Merge Operator | (Python 3.9+)
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = dict1 | dict2  # New merge operator
print(f"1. Merge with |: {merged}")

# 2. Dictionary Update Merge Operator |= (Python 3.9+)
dict1 |= {'e': 5}  # In-place merge
print(f"2. Update merge with |=: {dict1}")

# 3. Reversed Dictionary (Python 3.8+)
my_dict = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = dict(reversed(my_dict.items()))
print(f"3. Reversed dict: {reversed_dict}")

# 4. Dictionary get() with default (useful method)
value = my_dict.get('x', 'Not found')
print(f"4. get() with default: {value}")

# 5. Dictionary setdefault() - sets if key doesn't exist
my_dict.setdefault('new_key', 'default_value')
print(f"5. setdefault(): {my_dict}")

# 6. Dictionary popitem() - removes and returns last item (Python 3.7+ maintains order)
item = my_dict.popitem()
print(f"6. popitem(): removed {item}, remaining: {my_dict}")

# 7. Dictionary fromkeys() - create dict from iterable
keys = ['x', 'y', 'z']
new_dict = dict.fromkeys(keys, 0)
print(f"7. fromkeys(): {new_dict}")

# 8. Dictionary update() with keyword arguments
my_dict.update({'key1': 'value1', 'key2': 'value2'})
print(f"8. update() with kwargs: {my_dict}")

print("\n" + "=" * 60)
print("LIST METHODS")
print("=" * 60)

# 1. List clear() - removes all items (Python 3.3+)
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(f"1. clear(): {my_list}")

# 2. List copy() - shallow copy
original = [1, 2, 3]
copied = original.copy()
print(f"2. copy(): {copied}")

# 3. List extend() - add multiple items
my_list = [1, 2]
my_list.extend([3, 4, 5])
print(f"3. extend(): {my_list}")

# 4. List insert() - insert at specific index
my_list.insert(2, 'inserted')
print(f"4. insert(): {my_list}")

# 5. List pop() - remove and return item at index
popped = my_list.pop(2)
print(f"5. pop(2): removed '{popped}', list: {my_list}")

# 6. List remove() - remove first occurrence
my_list.remove(3)
print(f"6. remove(3): {my_list}")

# 7. List reverse() - reverse in place
my_list.reverse()
print(f"7. reverse(): {my_list}")

# 8. List sort() with key parameter
words = ['apple', 'pie', 'banana', 'cherry']
words.sort(key=len)  # Sort by length
print(f"8. sort(key=len): {words}")

# 9. List index() - find index of first occurrence
index = words.index('pie')
print(f"9. index('pie'): {index}")

# 10. List count() - count occurrences
numbers = [1, 2, 2, 3, 2, 4]
count = numbers.count(2)
print(f"10. count(2): {count}")

print("\n" + "=" * 60)
print("SET METHODS")
print("=" * 60)

# 1. Set union() - returns union of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1.union(set2)
print(f"1. union(): {union}")

# 2. Set intersection() - common elements
intersection = set1.intersection(set2)
print(f"2. intersection(): {intersection}")

# 3. Set difference() - elements in set1 but not in set2
difference = set1.difference(set2)
print(f"3. difference(): {difference}")

# 4. Set symmetric_difference() - elements in either set but not both
sym_diff = set1.symmetric_difference(set2)
print(f"4. symmetric_difference(): {sym_diff}")

# 5. Set update() - update set with union
set1.update({6, 7})
print(f"5. update(): {set1}")

# 6. Set intersection_update() - update set with intersection
set1.intersection_update({2, 3, 8})
print(f"6. intersection_update(): {set1}")

# 7. Set difference_update() - remove elements present in other set
set1.difference_update({2})
print(f"7. difference_update(): {set1}")

# 8. Set symmetric_difference_update() - update with symmetric difference
set1.symmetric_difference_update({3, 9})
print(f"8. symmetric_difference_update(): {set1}")

# 9. Set add() - add single element
set1.add(10)
print(f"9. add(10): {set1}")

# 10. Set remove() vs discard() - remove() raises error if not found, discard() doesn't
set1.discard(99)  # No error if not found
print(f"10. discard(99): {set1}")

# 11. Set pop() - remove and return arbitrary element
popped = set1.pop()
print(f"11. pop(): removed {popped}, remaining: {set1}")

# 12. Set isdisjoint() - check if sets have no common elements
set_a = {1, 2}
set_b = {3, 4}
print(f"12. isdisjoint(): {set_a.isdisjoint(set_b)}")

# 13. Set issubset() - check if all elements are in other set
set_c = {1, 2}
set_d = {1, 2, 3, 4}
print(f"13. issubset(): {set_c.issubset(set_d)}")

# 14. Set issuperset() - check if contains all elements of other set
print(f"14. issuperset(): {set_d.issuperset(set_c)}")

print("\n" + "=" * 60)
print("TUPLE METHODS")
print("=" * 60)

# Note: Tuples are immutable, so they have fewer methods

# 1. Tuple count() - count occurrences
my_tuple = (1, 2, 2, 3, 2, 4)
count = my_tuple.count(2)
print(f"1. count(2): {count}")

# 2. Tuple index() - find index of first occurrence
index = my_tuple.index(3)
print(f"2. index(3): {index}")

# 3. Tuple unpacking (useful feature)
a, b, *rest = my_tuple
print(f"3. Unpacking: a={a}, b={b}, rest={rest}")

# 4. Tuple concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
combined = tuple1 + tuple2
print(f"4. Concatenation: {combined}")

# 5. Tuple repetition
repeated = tuple1 * 3
print(f"5. Repetition: {repeated}")

print("\n" + "=" * 60)
print("ADVANCED EXAMPLES")
print("=" * 60)

# Dictionary comprehension with conditions
dict_comp = {k: v**2 for k, v in {'a': 1, 'b': 2, 'c': 3}.items() if v > 1}
print(f"Dict comprehension: {dict_comp}")

# Set comprehension
set_comp = {x**2 for x in range(5)}
print(f"Set comprehension: {set_comp}")

# List comprehension with walrus operator (Python 3.8+)
data = [1, 2, 3, 4, 5]
filtered = [x for x in data if (square := x**2) > 10]
print(f"List comprehension with walrus: {filtered}")

# Dictionary merge with | operator (Python 3.9+)
config = {'host': 'localhost'} | {'port': 8080} | {'debug': True}
print(f"Multiple dict merges: {config}")

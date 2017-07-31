'''
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example

sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
'''


import sys


def sort_array(source_array):
    print(source_array)
    # Traverse through all array elements
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            min_idx = i
            for j in range(i, len(source_array)):
                if source_array[j] % 2 != 0:
                    if source_array[min_idx] > source_array[j]:
                        min_idx = j
                    else:
                        continue
            # Swap the found minimum element with the first element
            source_array[i], source_array[min_idx] = source_array[min_idx], source_array[i]
    print(source_array)
    return source_array


sort_array([64, 25, 12, 22, 11, 5, 8, 3])
print()
sort_array([4, 25, 1, 2, 10, 7, 8, 3])
print()
sort_array([5, 3, 1, 8, 0])
print()
sort_array([5, 3, 2, 8, 1, 4])
print()
sort_array([])

'''----other solutions----'''


def sort_array(arr):
    odds = sorted((x for x in arr if x % 2 != 0), reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in arr]


def sort_array(source_array):
    odds = iter(sorted(v for v in source_array if v % 2))
    return [next(odds) if i % 2 else i for i in source_array]


def sort_array(numbers):
    evens = []
    odds = []
    for a in numbers:
        if a % 2:
            odds.append(a)
            evens.append(None)
        else:
            evens.append(a)
    odds = iter(sorted(odds))
    return [next(odds) if b is None else b for b in evens]


from collections import deque


def sort_array(array):
    odd = deque(sorted(x for x in array if x % 2))
    return [odd.popleft() if x % 2 else x for x in array]


def sort_array(source_array):
    return [] if len(source_array) == 0 else list(map(int, (','.join(['{}' if a % 2 else str(a) for a in source_array])).format(*list(sorted(a for a in source_array if a % 2 == 1))).split(',')))


def sort_array(source_array):
    odd = sorted(list(filter(lambda x: x % 2, source_array)))
    l, c = [], 0
    for i in source_array:
        if i in odd:
            l.append(odd[c])
            c += 1
        else:
            l.append(i)
    return l


def sort_array(source_array):
    # retrieve the odd values
    sorted_array = sorted([value for value in source_array if value % 2 != 0])
    # insert the even numbers in the original place
    for index, value in list(enumerate(source_array)):
        if value % 2 == 0:
            sorted_array.insert(index, value)
    return sorted_array


'''
----tests-----
Test.assert_equals(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
Test.assert_equals(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
Test.assert_equals(sort_array([]),[])
'''

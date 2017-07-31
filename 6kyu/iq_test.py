'''
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

##Examples :

iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd

'''


def iq_test(numbers):
    numbers = numbers.split(' ')
    numbers = [int(i) for i in numbers]
    even = [i for i in numbers if i % 2 == 0]
    odd = [i for i  in numbers if i % 2 != 0]
    
    if len(even) < len(odd):
        l = numbers.index(even[0]) + 1
    else:
        l = numbers.index(odd[0]) + 1
    return l


def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1


def iq_test(n):
    n = [int(i)%2 for i in n.split()]
    if n.count(0)>1:
        return n.index(1)+1
    else:
        return n.index(0)+1


def iq_test(numbers):
    eo = [int(n)%2 for n in numbers.split()]
    return eo.index(1 if eo.count(0)>1 else 0)+1


def iq_test(numbers):
    odds = [i for i in numbers.split(" ") if int(i) % 2 != 0]
    even = [i for i in numbers.split(" ") if int(i) % 2 == 0]
    ans = [odds,even][len(even)==1][0]
    return numbers.split(" ").index(ans)+1


def iq_test(numbers):
    nums = map(int, numbers.split())
    odd_filter = filter(lambda x: x % 2 > 0, nums) 
    if len(odd_filter) == 1:
        return nums.index(odd_filter[0]) + 1
    else:
        even_filter = filter(lambda x: x % 2 == 0, nums) 
        return nums.index(even_filter[0]) + 1


def iq_test(numbers):
  digits = [int(x) for x in numbers.split()]
  even = [x % 2 for x in digits]
  if sum(even) == 1:
    return even.index(1) + 1
  else:
    return even.index(0) + 1


def iq_test(numbers): 
    mod = [int(n) % 2 for n in numbers.split()]
    if sum(mod) == 1:
        return mod.index(1) + 1
    else:
        return mod.index(0) + 1


def iq_test(numbers):
    e = []
    o = []
    numbers = numbers.split(' ')
    for i, k in enumerate(numbers):
        if int(k) % 2 == 1:
            o.append(int(i) + 1)
        else:
            e.append(int(i) + 1)
    if len(e) > len(o):
        return(int(o[0]))
    else:
        return(int(e[0]))



def iq_test(numbers):
    nums = [int(n) % 2 for n in numbers.split()]
    if sum(nums) == 1:
      return nums.index(1) + 1
    else:
      return nums.index(0) + 1


def iq_test(numbers):
    odd = [i for i in range(len(numbers.split())) if int(numbers.split()[i]) % 2]
    even = [i for i in range(len(numbers.split())) if int(numbers.split()[i]) % 2 == 0]
    return odd[0] + 1 if len(odd) == 1 else even[0] + 1

'''
---tests----
Test.assert_equals(iq_test("2 4 7 8 10"),3)
Test.assert_equals(iq_test("1 2 2"), 1)
'''

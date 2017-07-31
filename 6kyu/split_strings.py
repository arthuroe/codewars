'''Description:

Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']

'''

def solution(s):
    o = []
    if s == '':
	    return []
    while s:
        o.append(s[:2])
        s = s[2:]

    for i in range(len(o)):
        if len(o[i]) < 2:
          i = o.insert(i,(o[i] + '_'))
          o.remove(o[-1]) 
    return o

'''---other solutions----'''
def solution(s):
    return [(s + "_")[i:i + 2] for i in range(0, len(s), 2)]

import re

def solution(s):
    return re.findall(".{2}", s + "_")

def solution(s):
    return [s[x:x+2] if x < len(s) - 1 else s[-1] + "_" for x in range(0, len(s), 2)]

def solution(s):
    return [''.join(a) for a in izip_longest(s[::2], s[1::2], fillvalue='_')]


def solution(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result

'''---Tests---'''
test.describe("Basic Tests")

tests = (
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"]),
)

for inp, exp in tests:
    test.assert_equals(solution(inp), exp)
    
test.describe("Random Tests")

from random import randint, choice
from string import ascii_lowercase

reference = lambda s, n=2: [''.join(e) for e in zip(*[iter(s + ['', '_'][len(s) % 2])]*2)]

for _ in range(100):
    test_case = "".join(choice(ascii_lowercase) for _ in range(randint(0, 100)))
    test.assert_equals(solution(test_case), reference(test_case))

'''
Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

Examples:

to_weird_case('String'); # => returns 'StRiNg'
to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'
'''


def to_weird_case(string):
    index = 0
    new = ''
    for word in string:
        if word == ' ':
            index = -1
            new += word
        elif index % 2 == 0:
            new += word.upper()
        else:
            new += word.lower()
        index += 1
    return new


def to_weird_case(string):
    ans = []
    string = string.split()
    for j in string:
        i = 0
        temp = ''
        while i < len(j):
            if i % 2 == 0:
                temp += j[i].upper()
            else:
                temp += j[i].lower()
            i += 1
        ans.append(temp)
    return ' '.join(ans)


def to_weird_case(string):
    def recase(s): return "".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])
    return " ".join([recase(word) for word in string.split(" ")])


def to_weird_case(string):
    return ' '.join([''.join([x[n].upper() if n % 2 == 0 else x[n].lower() for n in range(len(x))]) for x in string.split()])


def to_weird_case(s): return " ".join(
    ["".join([w[x].lower() if x % 2 else w[x].upper() for x in range(len(w))]) for w in s.split(' ')])


def to_weird_case(string):
    return ' '.join(
        map(
            lambda w: ''.join(l.lower() if i % 2 else l.upper() for i, l in enumerate(w)),
            string.split()
        )
    )


def to_weird_case(string):
    return ' '.join(''.join(x[i].upper() if i % 2 == False else x[i] for i in range(len(x))) for x in string.split())

#####


def to_weird_case_word(string):
    return "".join(c.upper() if i % 2 == 0 else c for i, c in enumerate(string.lower()))


def to_weird_case(string):
    return " ".join(to_weird_case_word(str) for str in string.split())
####


'''
----tests-----
test.describe('to_weird_case')

test.it('should return the correct value for a single word')
test.assert_equals(to_weird_case('This'), 'ThIs')
test.assert_equals(to_weird_case('is'), 'Is')

test.it('should return the correct value for multiple words')
test.assert_equals(to_weird_case('This is a test'), 'ThIs Is A TeSt')

'''

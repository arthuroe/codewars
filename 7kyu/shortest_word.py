def find_short(s):
    l = [len(i) for i in s.split(' ')]
    return min(l)
	

def find_short(s):
    return min([len(i) for i in s.split(' ')])
	
	
def find_short(s):
    return len(min(s.split(' '), key=len))
	
	
def find_short(s):
    return min(map(len, s.split(' ')))
	

def find_short(s):
    return len(reduce((lambda x, y: x if len(x) < len(y) else y), s.split()))
	
	
'''	
------tests--------
test.describe("Basic Tests")
test.assert_equals(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
test.assert_equals(find_short("turns out random test cases are easier than writing out basic ones"), 3)
test.assert_equals(find_short("lets talk about javascript the best language"), 3)
test.assert_equals(find_short("i want to travel the world writing code one day"), 1)
test.assert_equals(find_short("Lets all go on holiday somewhere very cold"), 2)
'''
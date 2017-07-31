def disemvowel(string):
    #filter function to sort out the string
    string = list(filter(lambda x: x not in 'aeiouAEIOU', string))
    #formatting filter function output back to a string
    string = ''.join(string)
    return string
'''
-----------tests-----------
test.assert_equals(disemvowel("This website is for losers LOL!"),
                              "Ths wbst s fr lsrs LL!")
							  '''
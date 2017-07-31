def tickets(people):
    b_25, b_50, b_100 = 0, 0, 0
    for i in range(len(people)):
        if people[i] == 25:
            b_25 += 1
        elif people[i] == 50:
            if b_25 == 0:
                return 'NO'
            b_50 += 1
            b_25 -= 1
        else:
            b_100 += 1
            if b_25 >= 1 and b_50 >= 1:
                b_25 -= 1
                b_50 -= 1
            elif b_25 >= 3:
                b_25 -= 3
            else:
                return 'NO'
    return 'YES'


''''others code''''
def tickets(people):
  till = {100.0:0, 50.0:0, 25.0:0}

  for paid in people:
    till[paid] += 1
    change = paid-25.0
    
    for bill in (50,25):
      while (bill <= change and till[bill] > 0):
        till[bill] -= 1
        change -= bill

    if change != 0:
      return 'NO'
        
  return 'YES'


def tickets(a):
    n25 = n50 = n100 = 0
    for e in a:
        if   e==25            : n25+=1
        elif e==50            : n25-=1; n50+=1
        elif e==100 and n50>0 : n25-=1; n50-=1
        elif e==100 and n50==0: n25-=3
        if n25<0 or n50<0:
            return 'NO'
    return 'YES'


def tickets(people):
    a = people.count(25)
    b = people.count(50)
    c = people.count(100)
    if (b-a <= 0) and ((a-b-min(b,a-b))/3 + min(b,a-b) >= c):
        return 'YES'
    else:
        return 'NO'


def tickets(people):
    cashRegister = {25: 0, 50: 0, 100: 0};
    ticketPrice = 25;
    for paid in people:
        cashRegister[paid] += 1;
        while paid > ticketPrice:
            changeGiven = False;
            """ Check if we have a bill in the register that we use as change """
            for bill in sorted(cashRegister.keys(), reverse=True):
                """ Hand out hhange if possible and still needed """
                if (paid - ticketPrice >= bill) and (cashRegister[bill] > 0):
                    paid = paid - bill;
                    cashRegister[bill] -= 1;
                    changeGiven = True;
            """ Return "NO" if we were unable to give the change required """
            if (paid > ticketPrice) and (changeGiven == False):
                    return "NO";
    return "YES";

'''
---tests---
test.assert_equals(tickets([25, 25, 50]), "YES")
test.assert_equals(tickets([25, 100]), "NO")
'''

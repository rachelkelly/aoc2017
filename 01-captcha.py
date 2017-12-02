# Day 1 of Advent of Code - Dec 1 2017
# The captcha requires you to review a seqqq of digits (your puzzle
# input [my? their? whose?] and find the sum of all digits that match
# the next digit in the list.  The list is circular, so the digit after
# the last digit is the fist digit in the list.

# 1122 produces a sum of 3 because the second 1 matches the first and
# the second 2 matches the one before it too: 1 _1_ 2 _2_ = 3

# 1111 produces 4 - circularly, each number matches the last so the
# total of all is 4 ( 1 + 1 + 1 + 1 )

# 1234 produces 0 because no digit matches the next (/previous)

# 9121212129 produces 9 because only the first and last digit are sequential

def captchor(numble):
    stringed = str(numble)
    seqqq = []
    total = 0
    for i in stringed:
        seqqq.append(int(i))

    while len(seqqq) > 0:

        # last'ns
        if len(seqqq) == 1:
            print "Only one left.  And the total is ...", total
            break
        elif len(seqqq) == 2:
            if seqqq[0] == seqqq[1]:
                total = total + seqqq[0]
            del seqqq[0]
       
        while len(seqqq) > 2: 
            if seqqq[-1] == seqqq[0]:
                total = total + seqqq[0]
                seqqq.pop()
            elif seqqq[0] == seqqq[1]:
                total = total + seqqq[0]
            del seqqq[0]

    if len(seqqq) == 0:
        print "total:", total

print "11234"
captchor(11234)
print "\n1234:"
captchor(12341)
print "\n1111"
captchor(1111)
print "\n112233"
captchor(112233)
print "\n9121212129"
captchor(9121212129)

# Day 1 of Advent of Code - Dec 1 2017
# The captcha requires you to review a sequence of digits (your puzzle
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
    sequence = []
    total = 0
    for i in stringed:
        sequence.append(int(i))

    for j in sequence:

        # last'n
        if len(sequence) == 0:
            print "And the total is ...", total
            break
        elif len(sequence) == 1:
            print "And the total is ...", total
            break
        elif len(sequence) == 2:
            if sequence[0] == sequence[1]:
                total = total + sequence[0]
                del sequence[0]
                del sequence[0]
            else:
                print "totally total:", total
                break
        
        # first/last
        if sequence[0] == sequence[-1]:
#            print "sequence[i-1] should be '1':", sequence[j-1]
            total = total + sequence[0]
            del sequence[-1]
            del sequence[0]

        elif sequence[0] == sequence[1]:
            total = total + sequence[0]
            del sequence[0]
            del sequence[0]
            print "total at this time is", total

        else:
            del sequence[0]

print "11234"
captchor(11234)
print "\n1234:"
captchor(12341)
print "\n112233"
captchor(112233)
print "\n912121212129"
captchor(912121212129)

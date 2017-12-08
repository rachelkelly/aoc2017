# "checksums"
# For each row, determine the difference between the largest value and the smallest value; the checksum is the sum of all of these differences.
#
# For example, given the following spreadsheet:
#
# 5 1 9 5
# 7 5 3
# 2 4 6 8
#
# In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

def summee():
    f = open("02-input.txt", "r")
    totalis = 0
    for line in f:
        limenate = []
        for i in line.split():
            limenate.append(int(i))
        diff = max(limenate) - min(limenate)
        totalis += diff
    print totalis
    f.close()
        
summee()

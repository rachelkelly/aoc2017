# Advent of Code day 4.1
# A valid passphrase must contain no duplicate words.
# For example:
# - aa bb cc dd ee is valid
# - aa bb cc dd aa is not valid - the word aa appears more than once.
# - aa bb cc dd aaa is valid - aa and aaa count as different words.

def phrase_eater():
    f = open("04-input.txt", "r")

    biggerall = []
    craigerall = [] # what even am variable name
    for line in f:
        words = line.split()

        # part 2
        parttwo = []
        comptor = ""
        for i in words:
            parttwo = []
            for j in i:
                parttwo.append(j)
                settwo = set(parttwo)
            if settwo == comptor:
                continue
            else:
                craigerall.append(words)
        #

        wordset = set(words)
        if len(words) == len(wordset):
            biggerall.append(line)

    f.close()
    print "uniques:", len(biggerall)
    print "craigs:", len(craigerall)
    
phrase_eater()

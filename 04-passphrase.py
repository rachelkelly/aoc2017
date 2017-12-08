# Advent of Code day 4.1
# A valid passphrase must contain no duplicate words.
# For example:
# - aa bb cc dd ee is valid
# - aa bb cc dd aa is not valid - the word aa appears more than once.
# - aa bb cc dd aaa is valid - aa and aaa count as different words.

def phrase_eater():
    f = open("04-input.txt", "r")

    biggerall = []
    for line in f:
        words = line.split()
        wordset = set(words)
        if len(words) == len(wordset):
            biggerall.append(line)

    f.close()
    print "uniques:", len(biggerall)

phrase_eater()

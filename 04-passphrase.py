# Advent of Code day 4.1
# A valid passphrase must contain no duplicate words.
# For example:
# - aa bb cc dd ee is valid
# - aa bb cc dd aa is not valid - the word aa appears more than once.
# - aa bb cc dd aaa is valid - aa and aaa count as different words.

def phrase_eater():
    list_of_crunch = []
    name = raw_input("filename? \n> ")
    f = open(name, "r")

    for line in f:
        words = line.split(" ")
        for word in words:
            list_of_crunch.append(word)

    set_of_crunch = set(list_of_crunch)
    f.close()
    print "uniques:", len(set_of_crunch)

phrase_eater()

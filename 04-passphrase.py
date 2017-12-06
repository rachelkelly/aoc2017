# Advent of Code day 4.1
# A valid passphrase must contain no duplicate words.
# For example:
# - aa bb cc dd ee is valid
# - aa bb cc dd aa is not valid - the word aa appears more than once.
# - aa bb cc dd aaa is valid - aa and aaa count as different words.

def phrase_eater():
    list_of_crunch = []
    FLAVOR_LESS = []
    name = raw_input("filename? \n> ")
    f = open(name, "r")
    for line in f:
        words = line.split(" ")
        for word in words:
            if word in list_of_crunch:
#                print "this shit is already in crunchtown:", word
                FLAVOR_LESS.append(word)
                pass
            elif word not in list_of_crunch:
                print "adding", word
                list_of_crunch.append(word)
    if '\n' in list_of_crunch:
        list_of_crunch.remove('\n')
    f.close()
    print "re-to-three-peats", len(FLAVOR_LESS)
    print "uniques:", len(list_of_crunch)

phrase_eater()

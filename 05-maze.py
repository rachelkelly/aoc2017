# Day 5
# Get out of the maze!  Each value tells you how many to move.  2 moves forward
#  2 spots, and -3 moves back 3 spots.  Each time a number is landed upon, it 
# increments up after executing.  How many steps to exit?

def mazeloser(filette):
    f = open(filette, "r")
    yomp = []
    for item in f:
        yomp.append(item.strip())

    print yomp

    for i in yomp:
        

mazeloser("05-input-headzo.txt")
#mazeloser("05-input.txt")

# Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward. For example, the first few squares are allocated like this:
#
# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23---> ...
# While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1 (the location of the only access port for this memory system) by programs that can only move up, down, left, or right. They always take the shortest path: the Manhattan Distance between the location of the data and square 1.
#
# For example:
#
# Data from square 1 is carried 0 steps, since it's at the access port.
# Data from square 12 is carried 3 steps, such as: down, left, left.
# Data from square 23 is carried only 2 steps: up twice.
# Data from square 1024 must be carried 31 steps.
# How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?

def spiralizer(the_ins):
    """
    repeatedly iterate direction to go: e, n, w, s
    if no direction, take first direction in list ^^
    if neighbor on two sides, use same direction as before
    if neighbor on only one side, "corner" assumed and iterate to next direction

    questions:
    1 - how build awareness of a matrix, does python have matrix builtin, is just lists in lists?
    2 - ???? traversal ????
    """
    
    incrementor = 3 # the spiralization doesn't begin til later
    row_H1 = "" # lower-one
    row = """  1  """ # as in "main row," row that 1 is in
    while the_ins > 0:
        sec = row, """  2  """
        for i in row:
            row_H1 += " "
        row.replace("  ", "")
        row_H1 += str(incrementor) + "  "
        incrementor += 1
        the_ins -= 1

    def e(current):
        new = current, """  %d  """

    def n():
        pass

    def w():
        pass

    def s():
        pass

    def which_way():
        pass

    final = """ """
    final = '"""', '\n' row_L1,  row, '"""'
    print final

spiralizer(10)

nonogram = [
    [None, None, None, None, None],
    [None, None, None, None, None],
    [None, None, None, None, None],
    [None, None, None, None, None],
    [None, None, None, None, None],
]
# A 5x5 nonogram

clue_dict = {
    'row0': (3,),
    'row1': (3,),
    'row2': (1,),
    'row3': (2,),
    'row4': (2, 2),  # From left to right (2, 2)

    'col0': (2, 1),  # From top to bottom (2, 1)
    'col1': (2, 1),  #
    'col2': (2,),
    'col3': (2,),
    'col4': (3,)
}

alpha = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"
]


def solve_by_line(nonogram, clue_dict, width, height):
    """Solves nonogram puzzle using the line-solve strategy"""
    global alpha

    # Solving for all rows
    for row in range(height):
        clue_key = "row" + str(row)
        clue = clue_dict[clue_key]

        num_of_clues = len(clue)
        clue_sum = sum(clue)

        if clue_sum * 2 > width:
            index = 0

            left_extreme = [None] * width  # Left extreme scenario;
            right_extreme = [None] * width  # Right extreme scenario

            right_i = width - (clue_sum + (num_of_clues - 1))  # Right extreme starts right_i ahead of left_extreme

            for i in range(0, num_of_clues):  # Loops through for each clue;
                start = index

                for j in range(index, index + clue[i]):  # Loop fills up both extreme cases at the same time
                    left_extreme[index] = alpha[i]  # Use alphabet to know which clue belongs to which box
                    right_extreme[right_i + index] = alpha[i]

                    if j == (start + clue[i]) - 1:
                        index += 2
                    else:
                        index += 1

            for i in range(0, width):
                if left_extreme[i] == right_extreme[i] and left_extreme[i] is not None:
                    nonogram[row][i] = "1"
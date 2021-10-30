import os


# clean console screen
def clear():

    # for linux and mac
    if os.name == "posix":
        _ = os.system("clear")

    # for windows
    else:
        _ = os.system("cls")


a = [' ', ' ', ' ']
b = [' ', ' ', ' ']
c = [' ', ' ', ' ']

# for print layout
grid = [a, b, c]
# for check and print the rows coordinate axis with the fStr
row_topic = ["A", 'B', "C"]


def print_playground():
    '''Print the checkerboard'''

    # print columns coordinate axis
    print("   1   2   3")
    for i in range(0, 3):
        print(f"{row_topic[i]}  {grid[i][0]} | {grid[i][1]} | {grid[i][2]}")
        if i < 2:
            print("  -----------")


def turn(sign):
    '''Prompt user to choose a position'''

    # prompt user to choose position
    pos = input(f'Now\'s "{sign}"\'s turn, please select a position. (e.g A3)')
    row = pos[0].upper()
    col = int(pos[1]) - 1

    # check if the user input is out of bound
    if row not in row_topic or col < 0 or col > 2:
        retry(sign, "wrong_pos")
    else:
        if row == 'A':
            if a[col] == " ":
                a[col] = sign
            else:
                retry(sign, "pos_taken")
        elif row == 'B':
            if b[col] == " ":
                b[col] = sign
            else:
                retry(sign, "pos_taken")
        elif row == 'C':
            if c[col] == " ":
                c[col] = sign
            else:
                retry(sign, "pos_taken")


def retry(sign, status):
    '''Prompt user to input the valid value when they type wrong.'''

    clear()
    if status == "wrong_pos":
        print("Invalid position, please try again.")
    elif status == "pos_taken":
        print("This position is already taken, please try another.")
    print_playground()
    turn(sign)


def not_end():
    pass


while True:
    clear()
    print_playground()
    turn("O")
    clear()
    print_playground()
    turn("X")

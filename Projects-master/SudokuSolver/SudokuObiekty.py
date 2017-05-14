import math
from FieldClass import Field, Colors, Grid  # (self, row, column, square)
# SUDOKU :) 053000100064005000900000040008000030605400090040500070000704000710003000000000860
fields = []
grid = Grid()


def re_calc(row, column, square, number):
    for x in range(81):
        if fields[x].row == row:
            try:
                fields[x].vanish(number)
            except ValueError:
                pass
        if fields[x].column == column:
            try:
                fields[x].vanish(number)
            except ValueError:
                pass
        if fields[x].square == square:
            try:
                fields[x].vanish(number)
            except ValueError:
                pass


def check():
    for doesnt_matter in range(81):
        for x in range(81):
            if fields[x].n_possi == 1:
                t = fields[x].possi[0]
                fields[x].place(t)
                re_calc(fields[x].row, fields[x].column, fields[x].square, fields[x].number)


def show():
    for x in range(0, 81, 9):
            if x in range(27, 46):
                print(
                    Colors.HEADER +
                    fields[x].number + fields[x+1].number + fields[x+2].number, fields[x+3].number + fields[x+4].number
                    + fields[x+5].number, fields[x+6].number + fields[x+7].number + fields[x+8].number +
                    Colors.ENDC)
            else:
                print(
                    fields[x].number + fields[x + 1].number + fields[x + 2].number,
                    fields[x + 3].number + fields[x + 4].number +
                    fields[x + 5].number, fields[x + 6].number + fields[x + 7].number + fields[x + 8].number)
    print('@@@@@@@@@@@@@@@')


def start():
    row, column = 0, 0
    for x in range(81):  # Create every field and grid
        fields.append(Field(row, column, math.floor(column/3) + 3*(math.floor(row/3))))
        grid.rows[row].append(x)
        grid.columns[column].append(x)
        grid.squares[math.floor(column/3) + 3*(math.floor(row/3))].append(x)
        if (x + 1) % 9 == 0:
            row += 1
        if column != 8:
            column += 1
        else:
            column = 0

    my_input = '030907000040000070500200190100000580820003900007040023410000000000000000082010040'  # input()
    if len(my_input) == 81:
        print('Valid length of input')
    else:
        print('Invalid length of input')
    row, column = 0, 0
    for x in range(81):  # Input handling
        if my_input[x] != '0':
            fields[x].place(my_input[x])
            re_calc(fields[x].row, fields[x].column, fields[x].square, my_input[x])
        if (x + 1) % 9 == 0:
            row += 1
        if column == 8:
            column = 0
        column += 1


def same_two():
    ind = [grid.rows, grid.columns, grid.squares]
    same = []
    for h in range(3):
        for x in range(9):  # dla kazdego rzedu
            indexes = ind[h][x]  # indexy pol calego rzedu
            for y in range(9):  # Dla kazdego pola porownaj do
                for z in range(y+1, 9):  # do czego prowonuje
                    if y != z:  # dla pewnosci xD
                        if (fields[indexes[y]].n_possi == 2) and (fields[indexes[z]].n_possi == 2):  # jesli maja po 2
                            if fields[indexes[y]].possi == fields[indexes[z]].possi:  # Tu następuje wykrrycie pary
                                same.append(fields[indexes[y]].possi[0])
                                same.append(fields[indexes[y]].possi[1])
                                for i in indexes:
                                    if (i != indexes[y]) and (i != indexes[z]):
                                        try:
                                            fields[i].vanish(same[0])
                                        except ValueError:
                                            pass
                                        try:
                                            fields[i].vanish(same[1])
                                        except ValueError:
                                            pass


def obvious():
    pass
start()  # Start the machine!

show()
check()
show()
same_two()
show()
check()
show()

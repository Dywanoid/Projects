import math
from FieldClass import Field, Colors, Grid  # (self, row, column, square)
# SUDOKU :) 030907000040000070500200190100000580820003900007040023410000000000000000082010040
fields = []
grid = Grid()


def re_calc(row, column, square, number):
    for x in range(81):
        if fields[x].row == row and number in fields[x].possi:
            fields[x].vanish(number)
        if fields[x].column == column and number in fields[x].possi:
            fields[x].vanish(number)
        if fields[x].square == square and number in fields[x].possi:
            fields[x].vanish(number)


def check():
    for doesnt_matter in range(81):
        for x in range(81):
            if fields[x].n_possi == 1 and not fields[x].placed:
                fields[x].place(fields[x].possi[0])
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


def start():  # takes input and puts some of numbers deleting possibilities
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

    my_input = '000010090000005200010300074300000005000004080000000910000502030007040809003100700'  # input()
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
                                        if same[0] in fields[i].possi:
                                            fields[i].vanish(same[0])
                                        if same[1] in fields[i].possi:
                                            fields[i].vanish(same[1])
                    same = []


def obvious():
    for x in range(1, 10):  # dla kazdej z cyfr szukam miejsc
        for h in range(3):
            ind = [grid.rows, grid.columns, grid.squares]
            for z in range(9):  # dla kazdego z rzedow, kolumn, kwadratow
                indexes = ind[h][z]
                how_many = 0
                i = 0
                for field in range(9):  # dla kazdego z pol
                    if fields[indexes[field]].possi.count(str(x)) == 1:
                        how_many += 1
                        i = indexes[field]
                if how_many == 1:
                    fields[i].place(str(x))
                    re_calc(fields[i].row, fields[i].column, fields[i].square, str(x))

start()  # Start the machine!
check()
obvious()
check()
obvious()
check()
obvious()
check()
obvious()
check()
obvious()
check()
obvious()
same_two()
check()
obvious()
show()

import math
from FieldClass import Field, Colors, Grid  # (self, row, column, square)
# SUDOKU :) 200000105000300072030056400360170009000090000790005010610000320000000000500000940
# nierozwiazane 059000008000008000007000026010600070020100030700092000001000300500001200302007690
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
                # fields[x].show()
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

    my_input = input('Input sudoku:')
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


def triplets_counter(a, b, c):  # a, b and c are lists of length 3 or 2 containing numbers as strings
        # together = a # why is this thing here causing weird stuff wtf

        together = []
        for x in a:
            if x not in together:
                together.append(x)

        for y in b:
            if y not in together:
                together.append(y)

        for z in c:
            if z not in together:
                together.append(z)
        return [True, together] if len(together) == 3 else [False, []]


def triplets():
    ind = [grid.rows, grid.columns, grid.squares]
    for h in range(3):
        for x in range(9):
            indexes = ind[h][x]
            for A in range(7):
                if fields[indexes[A]].n_possi < 4 and not fields[indexes[A]].placed:
                    for B in range(A + 1, 8):
                        if fields[indexes[B]].n_possi < 4 and not fields[indexes[B]].placed:
                            for C in range(B + 1, 9):
                                if fields[indexes[C]].n_possi < 4 and not fields[indexes[C]].placed:
                                    temp = triplets_counter(fields[indexes[A]].possi,
                                                            fields[indexes[B]].possi,
                                                            fields[indexes[C]].possi)
                                    if temp[0]:
                                        for i in indexes:
                                            if i != indexes[A] and i != indexes[B] and i != indexes[C]:
                                                if temp[1][0] in fields[i].possi:
                                                    fields[i].vanish(temp[1][0])
                                                if temp[1][1] in fields[i].possi:
                                                    fields[i].vanish(temp[1][1])
                                                if temp[1][2] in fields[i].possi:
                                                    fields[i].vanish(temp[1][2])


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
check()
triplets()
check()
obvious()
check()
obvious()
check()
obvious()
check()
same_two()
check()
obvious()
check()
triplets()
check()
obvious()
check()
show()

import math
from FieldClass import Field, Colors # (self, row, column, square)
# SUDOKU :) 007040000005003000301900000000200000080395070000078040000530000079081024000009080
fields = []
row, column = 0, 0

def re_calc(row, column, square, number):
    for x in range(81):
        if fields[x].row == row:
            try:
                fields[x].possi.remove(number)
            except ValueError:
                pass
        if fields[x].column == column:
            try:
                fields[x].possi.remove(number)
            except ValueError:
                pass
        if fields[x].square == square:
            try:
                fields[x].possi.remove(number)
            except ValueError:
                pass

def check():
    for x in range(81):
        if len(fields[x].possi) == 1:
            t = fields[x].possi[0]
            fields[x].place(t)
            re_calc(fields[x].row, fields[x].column, fields[x].square, fields[x].number)

def show():
    for x in range(0,81,9):
            if( x >= 27 and x <= 45):
                print(Colors.HEADER +
                fields[x].number + fields[x+1].number + fields[x+2].number, fields[x+3].number + fields[x+4].number +
                  fields[x+5].number, fields[x+6].number + fields[x+7].number + fields[x+8].number +
                Colors.ENDC)
            else:
                print(fields[x].number + fields[x + 1].number + fields[x + 2].number,
                      fields[x + 3].number + fields[x + 4].number +
                      fields[x + 5].number, fields[x + 6].number + fields[x + 7].number + fields[x + 8].number)

for x in range(81):
    fields.append(Field(row, column, math.floor(column/3) + 3*(math.floor(row/3))))
    if (x + 1) % 9 == 0:
        row += 1
    if column != 8:
        column += 1
    else:
        column = 0


my_input = input('Wprowadź sudoku: ')
row, column = 0, 0
for x in range(81):
    if my_input[x] != '0':
        fields[x].place(my_input[x])
        re_calc(fields[x].row, fields[x].column, fields[x].square, my_input[x])
    if (x + 1) % 9 == 0:
        row += 1
    if column == 8:
        column = 0
    column += 1

show()
for x in range(25):
    check()
print('@@@@@@@@@@@@@@@')
show()

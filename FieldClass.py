class Field:
    def __init__(self, row, column, square):
        self.row = row
        self.column = column
        self.square = square
        self.possi = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.placed = False
        self.number = '0'


    def show(self):
        print('Row:',self.row, 'Col:', self.column, 'Squ:', self.square, 'Pos:', self. possi,'Placed?', self.placed,
              '#:', self.number)


    def place(self, n):
        self.number = n
        self.placed = True
        self.possi = [n]


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
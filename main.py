from dis import dis
import time
from checkBlock import checkBlock
#Link to sudoku image - https://images.template.net/wp-content/uploads/2016/07/02084544/Basic-Easy-Sudoku-Template.jpg

sudoku = [
    [1, 4, 2, 0, 9, 0, 0, 0, 5],
    [7, 0, 0, 4, 0, 0, 0, 8, 9],
    [8, 0, 5, 0, 0, 0, 0, 2, 4],
    [2, 0, 0, 0, 0, 4, 8, 0, 0],
    [0, 3, 0, 0, 0, 1, 2, 6, 0],
    [0, 8, 0, 0, 7, 2, 9, 4, 1],
    [0, 5, 0, 2, 0, 6, 0, 0, 0],
    [0, 2, 8, 0, 0, 9, 4, 1, 0],
    [0, 7, 9, 1, 0, 8, 5, 3, 0],
]
#To be Generated automatically #Done :D
# sudokuFormatBlock = [
#     [1, 4, 2, 7, 0, 0, 8, 0, 5],
#     [0, 9, 0, 4, 0, 0, 0, 0, 0],
#     [0, 0, 5, 0, 8, 9, 0, 2, 4],
#     [2, 0, 0, 0, 3, 0, 0, 8, 0],
#     [0, 0, 4, 0, 0, 1, 0, 7, 2],
#     [8, 0, 0, 2, 6, 0, 9, 4, 1],
#     [0, 5, 0, 0, 2, 8, 0, 7, 9],
#     [2, 0, 6, 0, 0, 9, 1, 0, 8],
#     [0, 0, 0, 4, 1, 0, 5, 3, 0]
# ]
sudokuFormatBlock = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

inRow = []
inCol = []
inBlock = []

solved = False

def emptyCellToFill(sudoku = sudoku):
    for x in range(9):
        for y in range(9):
            if (sudoku[x][y]==0):
                 return x, y
    return 404, 404

def generateBlockSudoku(sudoku = sudoku, sudokuFormatBlock = sudokuFormatBlock):
    startIndex = 0
    endIndex = 3
    currentBlock = 0
    row = 0
    index = 1
    for block in range(9):
        firstThree = sudoku[row][startIndex:endIndex]
        secondThree = sudoku[row + 1][startIndex:endIndex]
        thirdThree = sudoku[row + 2][startIndex:endIndex]

        allThree = firstThree + secondThree + thirdThree

        sudokuFormatBlock[currentBlock]+=allThree

        startIndex +=3
        endIndex +=3
        index+=1
        currentBlock+=1
        if(index%3==1):
            row+=3
            startIndex = 0
            endIndex = 3

def isSudokuValid(sudoku = sudoku, inRow = inRow, inCol = inCol, inBlock = inBlock):
    # 1. Check for not same number in a Row
    for row in range(9):
        for col in range(9):
            if(sudoku[row][col]!=0):
                if(sudoku[row][col] in inRow):
                    return False
                else:
                    inRow.append(sudoku[row][col])
        inRow = []

    # 2. Check for not same number in a Column
    currentCol = 0
    while currentCol < 9:
        for row in range(9):
            if(sudoku[row][currentCol]!=0):
                if(sudoku[row][currentCol] in inCol):
                    return False
                else:
                    inCol.append(sudoku[row][currentCol])
        inCol = []
        currentCol+=1

    # 3. Check for same number in the same 3X3 Block
    for block in range(9):
        for blockelement in range(9):
            if(sudokuFormatBlock[block][blockelement]!=0):
                if(sudokuFormatBlock[block][blockelement] in inBlock):
                    return False
                else:
                    inBlock.append(sudokuFormatBlock[block][blockelement])
        inBlock = []
    return True

def isMoveValid(sudoku, i, j, e):
    rowOk = all([e != sudoku[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != sudoku[x][j] for x in range(9)])
        if columnOk:
            sudoku[i][j] = e
            generateBlockSudoku()
            if(checkBlock(sudokuFormatBlock)):
                sudoku[i][j] = e
                return True
            else:
                sudoku[i][j] = 0
        return False
    return False
# def isMoveValid(x, y, val, sudoku = sudoku):
#     rowOk = all([val != str(sudoku[x][a] for a in range(9))])
#     colOk = all([val != str(sudoku[b][y] for b in range(9))])
#     # 1. Check for not same number in the Row x is located
#     if rowOk:
#         # 2. Check for not same number in the Column y is located
#         if colOk:
#             # sudoku[x][y] = val
#             # # 3. Check for same number in the same 3X3 Block as x,y
#             # if(checkBlock(sudokuFormatBlock)):
#             #     return True
#             # sudoku[x][y] = 0
#             return True
#     return False

# def solveSudoku(sudoku = sudoku, solved = solved):
#     x, y = emptyCellToFill()
#     if(x!=404):
#         for val in range(1, 10):
#             print(x, y, val)
#             if(isMoveValid(x, y, val)):
#                 sudoku[x][y] = val
#                 displaySudoku()
#     else:
#         solved = True
def solveSudoku(sudoku, i=0, j=0):
    i, j = emptyCellToFill(sudoku)
    if i == 404:
        return True
    for e in range(1, 10):
        if isMoveValid(sudoku, i, j, e):
            sudoku[i][j] = e
            if solveSudoku(sudoku, i, j):
                return True
            sudoku[i][j] = 0
    return False

def displaySudoku():
    print("\n\n\n\n\n")
    for i in range(len(sudoku)):
        line = ""
        if i == 3 or i == 6:
            print("---------------------")
        for j in range(len(sudoku[i])):
            if j == 3 or j == 6:
                line += "| "
            line += str(sudoku[i][j])+" "
        print(line)

if __name__=="__main__":
    print("Welcome to sudoku solver\nStarting to Solve your sudoku in 5 seconds\n")
    # time.sleep(5)
    print("Sudoku validity check has been started\nWait for few seconds until the check gets complete")

    generateBlockSudoku()

    if(isSudokuValid() == False):
        print("\nYour sudoku is invalid try using another one")
    else:
        print("\nSudoku validity check complete. Your sudoku is now starting to be solved")

    # print(isMoveValid(2, 4, 4))
    # print(isMoveValid(1, 4, 2))
    # print(isMoveValid(0, 3, 7))

    # displaySudoku()
    # while not solved:
    #     solveSudoku()
    displaySudoku()
    solveSudoku(sudoku)
    displaySudoku()

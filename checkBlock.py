def checkBlock(sudokuFormatBlock, inBlock=[]):
    for block in range(9):
        for blockelement in range(9):
            if(sudokuFormatBlock[block][blockelement]!=0):
                if(sudokuFormatBlock[block][blockelement] in inBlock):
                    return False
                else:
                    inBlock.append(sudokuFormatBlock[block][blockelement])
        inBlock = []
    return True
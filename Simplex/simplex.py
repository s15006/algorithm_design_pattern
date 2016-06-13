#!/usr/bin/python3

def data_generate(priceA, partsA1, partsA2, priceB, partsB1, partsB2, maxA, maxB):
    arrays = []
    arrays.append([partsA1, partsA2, 1, 0, maxA])
    arrays.append([partsB1, partsB2, 0, 1, maxB])
    arrays.append([priceA * -1, priceB * -1, 0, 0, 0])

    return arrays

def showTable(arrays):
    import sys

    for r in range(len(arrays)):
        for c in range(len(arrays[r])):
            sys.stdout.write("{}| ".format(arrays[r][c]))
            pass
        print()

def selectColumn(arrays):
    min = arrays[len(arrays) - 1][0]
    selColumn = 0

    for c in range(1, len(arrays[0])):
        if(min > arrays[len(arrays) - 1][c]):
            min = arrays[len(arrays) - 1][c]
            selColumn = c
    return selColumn

def selectRow(arrays, selColumn):
    min = arrays[0][len(arrays[selColumn]) - 1] / arrays[0][selColumn]
    selRow = 0
    for r in range(1, len(arrays) - 1):
        if min > arrays[r][len(arrays[selColumn]) - 1] / arrays[r][selColumn]:
            min = arrays[r][len(arrays[selColumn]) - 1] / arrays[r][selColumn]
            selRow = r
    return selRow

def toPivot(arrays, selRow, selColumn):
    pivot = arrays[selRow][selColumn]
    print(pivot)
    for c in range(len(arrays[selColumn])):
        arrays[selRow][c] /= pivot
    return pivot

def subColumn(arrays, pivot, selRow, selColumn):
    for r in range(len(arrays)):
        if (r == selRow):
            continue
        mul = arrays[r][selColumn]
        for c in range(len(arrays[selColumn])):
            arrays[r][c] -= arrays[selRow][c] * mul

if __name__ == "__main__":
    #引数は左から
    #品物Aの値段、部品Mの個数、部品Nの個数
    #品物Bの値段、部品Mの個数、部品Nの個数
    #部品Mの総数、部品Nの総数となっています
    arrays = data_generate(600, 6, 3, 400, 2, 4, 360, 240)
    showTable(arrays)
    while(True):
        selColumn = selectColumn(arrays)
        selRow = selectRow(arrays, selColumn)
        pivot = toPivot(arrays, selRow, selColumn)
        subColumn(arrays, pivot, selRow, selColumn)
        showTable(arrays)
        if arrays[len(arrays) - 1][0] >= 0 and arrays[len(arrays) - 1][1] >= 0:
            break
    print("目的関数の最大値 = {}".format(arrays[len(arrays) - 1][len(arrays[0]) - 1]))



def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


list = [1, 2, 3, 4, 5]
pos1 = 0
pos2 = 4
print(swapPositions(list, pos1, pos2))

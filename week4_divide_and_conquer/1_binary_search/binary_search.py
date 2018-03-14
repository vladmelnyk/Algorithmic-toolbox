# Uses python3
import sys


def binary_search(array, fromIndex, toIndex, searchableNumber):
    if toIndex < fromIndex:
        return - 1

    midIndex = fromIndex + (toIndex - fromIndex) // 2

    if searchableNumber == array[midIndex]:
        return midIndex
    elif searchableNumber < array[midIndex]:
        return binary_search(array, fromIndex, midIndex - 1, searchableNumber)
    else:
        return binary_search(array, midIndex + 1, toIndex, searchableNumber)


def find_in_initial_array(initalArray, targetArray):
    initalArray.sort()

    array_of_indexes = []
    for searchableNumber in targetArray:
        array_of_indexes.append(str(binary_search(initalArray, 0, len(initalArray) - 1, searchableNumber)))
    return array_of_indexes


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    x = data[n + 2:]
    # replace with the call to binary_search when implemented
    print(' '.join(find_in_initial_array(a, x)))

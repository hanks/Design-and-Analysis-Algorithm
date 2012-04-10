import random

comparisons = 0

def quicksort(array, left, right):
    if left < right:
        #pivotIndex = pickPivotRandom(left, right)
        #pivotIndex = pickPivotFirstIndex(left, right)
        #pivotIndex = pickPivotEndIndex(left, right)
        pivotIndex = pickPivotMedianOfThree(array, left, right)
        newPivotIndex = partition(array, left, right, pivotIndex)
        quicksort(array, left, newPivotIndex - 1)
        quicksort(array, newPivotIndex + 1, right)

def partition(array, left, right, pivotIndex):
    global comparisons
    
    # count comparisons
    comparisons += (right - left)
    
    pivot = array[pivotIndex]
    swap(array, left, pivotIndex)
    i = left + 1
    j = left + 1
    while j < len(array):
        if array[j] < pivot:
            swap(array, i, j)
            i += 1
        j += 1
    swap(array, left, i - 1)
    return i - 1
    

def pickPivotFirstIndex(left, right):
    return left

def pickPivotEndIndex(left, right):
    return right

def pickPivotRandom(left, right):
    return random.randint(left, right)

def pickPivotMedianOfThree(array, left, right):
    middle = (left + right) / 2
    if (array[left] > array[middle] and array[left] < array[right]) or (array[left] > array[right] and array[left] < array[middle]):
        return left
    elif (array[right] > array[left] and array[right] < array[middle]) or (array[right] > array[middle] and array[right] < array[left]):
        return right
    else:
        return middle

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
    
def buildListFromFile(filename):
    intList = []
    f = open(filename, 'r')
    for line in f:
        token = line.strip()
        intList.append(int(token))
    f.close()
    return intList

if __name__ == "__main__":
    #l = [2,3,1,5,4,6,7,9,8,19,16,13]
    arr = buildListFromFile("QuickSort.txt")
    quicksort(arr, 0, len(arr) - 1)
    print comparisons

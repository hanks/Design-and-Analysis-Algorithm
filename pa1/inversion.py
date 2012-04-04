inversion_count = 0

def mergeSort(array):
    if len(array) > 1:
        middle = len(array) / 2
        left = array[:middle]
        right = array[middle:]
        left = mergeSort(left)
        right = mergeSort(right)
        return merge(left, right)
    else:
        return array
    

def merge(arr1, arr2):
    global inversion_count
    result = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            inv_index = i
            while inv_index < len(arr1):
                inversion_count += 1
                inv_index += 1
            j += 1
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    return result

def buildListFromFile(filename):
    intList = []
    f = open(filename, 'r')
    for line in f:
        token = line.strip()
        intList.append(int(token))
    f.close()
    return intList
    
if __name__ == "__main__":
    arr = buildListFromFile("IntegerArray.txt")
    mergeSort(arr)
    print inversion_count
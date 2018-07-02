

### This program implements the following sorting algorithms
## 1. Bubble Sort
## 2. Insertion Sort
## 3. Selection Sort
## 4. Quick Sort

def BubbleSort(array):

    array_len = len(array)

    for i in xrange(array_len):
        for j in xrange(array_len - 1):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp         
    return array

def SelectionSort(array):
    
    array_len = len(array)
    
    for i in xrange(array_len):
        for j in xrange(i+1, array_len):
            if array[i] > array[j]:
                temp = array[j]
                array[j] = array[i]
                array[i] = temp
    return array

def InsertionSort(array):

    array_len = len(array)
    
    for i in xrange(array_len-1):
        for j in xrange(i+1, 0, -1):
            if array[j] < array[j-1]:
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
    return array

def QuickSort(array):
    
    if len(array) <= 1:
        return array
    
    pivot = int(len(array) / 2)
    left = []
    right = []
    mid = []
    
    for i in xrange(len(array)):
        if  array[i] < array[pivot]:
            left.append(array[i])
        elif array[i] > array[pivot]:
            right.append(array[i])
        else :# array[i] == array[pivot]:
            mid.append(array[i])   
    return  QuickSort(left) + mid + QuickSort(right)

## implementation

check = [1, 12, 5, 26, 7, 14, 3, 7, 2, 34, 56, 1 , 0 , 6, 7, -8, 10, -4 ,5 ,6, -2, 67, 89]

print 'Before Sort:\n', check
print 'After Bubble Sort:\n', BubbleSort(check)
#print 'After Selection Sort:\n', SelectionSort(check)
#print 'After Insertion Sort:\n', InsertionSort(check)
#print 'After QuickSort:\n', QuickSort(check)





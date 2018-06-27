

### Different sorting algorithm

def BubbleSort(array):

    array_len = len(array)
    for i in xrange(array_len):
        for j in xrange(i+1, array_len):
            if array[i] > array[j]:
                temp = array[j]
                array[j] = array[i]
                array[i] = temp

    return array

def SelectionSort(array):
    
    array_len = len(array)
    for i in xrange(array_len):
        index_min = i
        for j in xrange(i+1, array_len):
            if array[i] > array[j]:
                j = index_min
        if i != j:
            temp = array[index_min]
            array[index_min] = array[i]
            array[i] = temp
            
    return array

def InsertionSort(array):

    array_len = len(array)
    for i in xrange(1, array_len):
        index_min = i
        for j in xrange(i+1, array_len):
            if array[i] > array[j]:
                j = index_min
        if i != j:
            temp = array[index_min]
            array[index_min] = array[i]
            array[i] = temp
        if array[i-1] > array[i]:
            temp1 = array[i]
            array[i] = array[i-1]
            array[i-1] = temp1

    return array

def QuickSort(array):
    
    pivot = int(len(array)/2)
    if pivot <= 1:
        return array
    leftArry = [i for i in array if array[pivot] > i]
    rghtArry = [i for i in array if array[pivot] < i]
    middle = [i for i in array if array[pivot] == i]
    #print QuickSort(leftArry)+ middle + QuickSort(rghtArry)
    return QuickSort(leftArry)+ middle + QuickSort(rghtArry)

def MergeSort(arry):

    print 'given Array', arry
    if len(arry) > 1:

        halfLen = int(len(arry)/2)
        
        lftArry = arry[:halfLen]
        rghtArry = arry[halfLen:]

        MergeSort(lftArry)
        MergeSort(rghtArry)

        print 'leftarray', lftArry
        print 'RightArray', rghtArry

        i=0
        j=0
        k=0
        while (i < len(lftArry)) and (j < len(rghtArry)):
            print '1_________________'
            if lftArry[i] < rghtArry[j]:
                arry[k]=lftArry[i]
                #print'first  if while', arry[k], k,'iterartion in left', lftArry[i], i
                i=i+1
            else:
                arry[k]=rghtArry[j]
                #print 'first else while', arry[k], k,'iterartion in right', rghtArry[j], j
                j=j+1
            k=k+1
        while i < len(lftArry):
            #print '2_________________'
            arry[k]=lftArry[i]
            #print 'second while', arry[k], k,'iterartion in left', lftArry[i], i
            i=i+1
            k=k+1
        while j < len(rghtArry):
            #print '3________________'
            arry[k]=rghtArry[j]
            #print 'third while', arry[k], k,'iterartion in right', rghtArry[j], j
            j=j+1
            k=k+1
        return arry
    #return MergeSort(lftArry), MergeSort(rghtArry)

## Main implementation

num = [2 ,3 ,4, 0, 34, -3, 14, 56,12,0,23,4,5,5,-4,6,10]

check2 = [34, 56, 1 , 0 , 6, 7, -8, 10]

check3 = [-4 ,5 ,6, -2, 67, 89]

check4 = [1, 12, 5, 26, 7, 14, 3, 7, 2]

#Bubble sort
print BubbleSort(num)
#inserstion sort
print InsertionSort(num)
print MergeSort(check2)
print SelectionSort(check3)
print QuickSort(check4)

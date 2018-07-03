

## This program implements the Merge Sort Algorthim
## Input: unsorted array

def MergeSort(arry):

    if len(arry) == 1:
        return arry
    mid = int(len(arry) / 2)
    lfthalf =  arry[:mid]
    rghthalf =  arry[mid:]
    
    MergeSort(lfthalf)
    MergeAndCheck(lfthalf, rghthalf, arry)
    
    MergeSort(rghthalf)
    MergeAndCheck(lfthalf, rghthalf, arry)

    return arry

# This function is used to check the Merge Sort condition
# and merging the array elements
def MergeAndCheck(lftArry, rghtArry, arry):

    i=0
    j=0
    k=0

    while (i < len(lftArry)) and (j < len(rghtArry)):
        if lftArry[i] < rghtArry[j]:
            arry[k] = lftArry[i]
            i = i + 1
        else:
            arry[k]=rghtArry[j]
            j = j + 1
        k = k + 1

    while i < len(lftArry):
        arry[k] = lftArry[i]
        i = i + 1
        k = k + 1

    while j < len(rghtArry):
        arry[k] = rghtArry[j]
        j = j + 1
        k = k + 1

    return arry

## implementation

num = [2 ,3 ,4, 0, 34, -3, 14, 56,12,0,23,4,5,5,-4,6,10]

print 'Before sort', num
print'After Merge sort', MergeSort(num)

#print MergeSort([45, 12])


    



## This program implements the Counting sort algorithm
## Input: 1. Unsorted array and
## 2. Max value till or lesser than the values till in that array

def CountingSort(array, maxValue):

    count = [0]*(maxValue +1)
    sortedArry = [0]*len(array)

    for i in array:
        count[i] =  count[i] + 1
    for i in xrange(1, len(count)):
        count[i] = count[i] + count[i -1]
    for i in array:
        sortedArry[count[i]-1] = i
        count[i] = count[i] - 1
    return sortedArry

## Implementation

check = [1, 4 ,1, 2, 7,5, 2, 6,7,8,9,1,0,2]

print 'Befor Sort', check
print 'After Counting Sort', (CountingSort(check, 9))



        

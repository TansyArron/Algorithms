data = [line.strip() for line in open("IntegerArray.txt", 'r')]
data = [int(i) for i in data]

def mergeSort(alist):
    # if length of alist is greater than one, split it 
    # in half
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        # mergeSort each half
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0     # current index of left half
        j=0     # current index of right half
        k=0     # index of complete list
        
        while i<len(lefthalf) and j<len(righthalf):
            # iterate through both halves of the list, 
            # adding the next lowest value to aList.
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i += 1
            else:
                alist[k]=righthalf[j]
                j += 1
            k=k+1
        # deal with stragglers: 
        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

# mergeSort(data)

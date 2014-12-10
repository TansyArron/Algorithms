arr10 = [line.strip() for line in open("10.txt", 'r')]
arr10 = [int(i) for i in arr10]

arr100 = [line.strip() for line in open("100.txt", 'r')]
arr100 = [int(i) for i in arr100]

arr1000 = [line.strip() for line in open("1000.txt", 'r')]
arr1000 = [int(i) for i in arr1000]

def quickSortFirst(array):
	# quickSort using first element of array as pivot.
	if len(array) <= 1:
		return array
	else:
		# iterate through array[1:]
		# if x is smaller than array[0], move it to the front
		# of the list by swapping its position with the smallest
		# x larger than array[0].
		pivot = array[0]
		j = 1  		# index of first number larger than pivot
		for i in range(1, len(array)):
			if array[i] < pivot:
				array[i], array[j] = array[j], array[i]
				j += 1
			if array[i] > pivot:
				pass
		# move array[0] to array[j-1]
		array[0], array[j-1] = array[j-1], array[0]
		# quickSortFirst each half of the list and reassemble.
		return quickSortFirst(array[:j-1]) + [pivot] + quickSortFirst(array[j:])

quickSortFirst(arr10)

quickSortFirst(arr100)

quickSortFirst(arr1000)

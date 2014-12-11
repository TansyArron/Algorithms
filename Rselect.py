arr10 = [line.strip() for line in open("10.txt", 'r')]
arr10 = [int(i) for i in arr10]

arr100 = [line.strip() for line in open("100.txt", 'r')]
arr100 = [int(i) for i in arr100]

arr1000 = [line.strip() for line in open("1000.txt", 'r')]
arr1000 = [int(i) for i in arr1000]

import random

def rSelect(array, orderStatistic):
	# select the i-th smallest or largest element in an unsorted array.
	if len(array) == 1:
		return array[0]
	else:
		# choose pivot at random from array.
		# move pivot to front of array.
		pivotIndex = random.randrange(len(array))
		pivot = array[pivotIndex]
		array[0], array[pivotIndex] = array[pivotIndex], array[0]
		print 'start', array
		# iterate through array[1:]
		# if x is smaller than pivot, move it to the front
		# of the list by swapping its position with the smallest
		# x larger than pivot.
		j = 0  		# index of first number larger than pivot
		for i in range(1, len(array)):
			if array[i] < pivot:
				array[i], array[j + 1] = array[j + 1], array[i]
				j += 1
			if array[i] > pivot:
				pass
		# move pivot to array[j]
		array[0], array[j] = array[j], array[0]
		print "pivot", pivot, "array[0]", array[0]
		print'ordered', array 
		# check new pivot position against orderStatistic
		if j == orderStatistic:
			return pivot
		if j > orderStatistic:
			return rSelect(array[:j], orderStatistic)
		if j < orderStatistic:
			return rSelect(array[j:], orderStatistic - j)


print rSelect(arr10, 3)



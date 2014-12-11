arr10 = [line.strip() for line in open("10.txt", 'r')]
arr10 = [int(i) for i in arr10]

arr100 = [line.strip() for line in open("100.txt", 'r')]
arr100 = [int(i) for i in arr100]

arr1000 = [line.strip() for line in open("1000.txt", 'r')]
arr1000 = [int(i) for i in arr1000]

import random
from mergesort import mergeSort


def dSelect(array, orderStatistic):
	# select the i-th smallest or largest element in an unsorted array.
	if len(array) == 1:
		return array[0]
	else:
		# split array in to arrays of length 5.
		n = len(array)
		fifths = []
		medians = []
		for i in range(0, n, 5):
			fifths.append(array[i:i+5])
		# choose pivot as median of medians.
		for x in fifths:
			mergeSort(x)
		 	medians.append(x[len(x)/2])		
		pivot = dSelect(medians, len(medians)/2)
		pivotIndex = array.index(pivot)		
		
		# move pivot to front of array.
		
		array[0], array[pivotIndex] = array[pivotIndex], array[0]
		# print 'start', array
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
		# print "pivot", pivot, "array[0]", array[0]
		# print'ordered', array 
		# check new pivot position against orderStatistic
		if j == orderStatistic:
			return pivot
		if j > orderStatistic:
			return dSelect(array[:j], orderStatistic)
		if j < orderStatistic:
			return dSelect(array[j:], orderStatistic - j)


print dSelect(arr1000, 9)



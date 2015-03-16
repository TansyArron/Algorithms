arr100 = [line.strip() for line in open("100.txt", 'r')]
arr100 = [int(i) for i in arr100]

def quicksort(unsorted_list, lower=0, upper=None):
	print('current list: {}'.format(unsorted_list[lower:upper]))
	if upper == None:
		upper = len(unsorted_list)
	if upper - lower < 2:
		print('STOPPING BRANCH')
		return
	else:
		pivot = unsorted_list[lower]
		first_larger_index = lower + 1
		for index in range(lower + 1, upper):
			if unsorted_list[index] < pivot:
				temp = unsorted_list[first_larger_index]
				unsorted_list[first_larger_index] = unsorted_list[index]
				unsorted_list[index] = temp
				first_larger_index += 1
			else:
				pass
		temp = unsorted_list[first_larger_index - 1]
		unsorted_list[first_larger_index - 1] = pivot
		unsorted_list[lower] = temp
		print('moving pivot {} to correct location: {}'.format(pivot, unsorted_list))
		print('left half:', unsorted_list[lower:first_larger_index - 1])
		print('right half:', unsorted_list[first_larger_index:upper])
		#unsorted_list[:first_larger_index - 1] = quicksort(unsorted_list[:first_larger_index - 1])
		quicksort(unsorted_list, lower, first_larger_index-1)
		quicksort(unsorted_list, first_larger_index, upper)
	
print(arr100)
quicksort(arr100)
print(arr100)
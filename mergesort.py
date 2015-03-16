arr100 = [line.strip() for line in open("100.txt", 'r')]
arr100 = [int(i) for i in arr100]

def mergesort(unsorted_list):

	if len(unsorted_list) > 1:
		mid = len(unsorted_list)//2
		left = mergesort(unsorted_list[:mid])
		right = mergesort(unsorted_list[mid:])
		left_index = 0
		right_index = 0
		merged = []
		while left_index < len(left) and right_index < len(right):
			if left[left_index] < right[right_index]:
				merged.append(left[left_index])
				left_index += 1
			else:
				merged.append(right[right_index])
				right_index += 1
		if left_index < len(left):
			merged.extend(left[left_index:])
		else:
			merged.extend(right[right_index:])
		return merged
	else:
		return(unsorted_list)

print(mergesort(arr100))

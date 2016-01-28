from test_data.sorted_list import sorted_list

def binary_search(sorted_list, element):
	''' find given element in a sorted sorted_list
	'''
	upper = len(sorted_list)
	lower = 0
	while upper - lower > 0:
		mid = (upper - lower)// 2 + lower
		if sorted_list[mid] == element:
			return mid
		elif sorted_list[mid] < element:
			lower = mid + 1
		else:
			upper = mid
	return None

test = sorted_list(30)
print(binary_search(test, 3))





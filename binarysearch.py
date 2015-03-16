
def binary_search(sorted_list, element):
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

sorted_list = [1,2,3,4,5]
print(binary_search(sorted_list, 3))





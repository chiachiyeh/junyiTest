def reverseByword(x):
	arr = x.split()
	reverse_arr = [data[::-1] for data in arr]
	return ' '.join(reverse_arr)

reverseByword(x)
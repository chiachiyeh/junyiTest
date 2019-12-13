def trimNum(x):
	ret = [i for i in range(1, x+1)]
	for num in range(1,x+1):

		if num >= 3 and num % 3 == 0:
			ret.remove(num)
		elif num >= 5 and num %5 == 0:
			ret.remove(num)

		if num>=15 and num%15==0:
			ret.append(num)

	#print(ret)
	return len(ret)

print(trimNum(15))



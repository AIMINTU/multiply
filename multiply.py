my_list=[8,2,3,-1,7]#problem number is 7
another_list=[5, 8, 82, 21]

def rita(l):
	total=1
	for x in l:
		total*=x      
	return total
	print(total)

print(rita(my_list))

print(rita(another_list))
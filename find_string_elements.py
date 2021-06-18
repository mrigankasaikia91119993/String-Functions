###The function find_alphanum(a, b) find if a given string's elements occured in n another string, takes two arguments , a is the string where elements are to be find and b is the string who's elements are to be find. This function is not case sensitive.###

def find_alphanum(A, B):
	A.upper()
	B.upper()
	c = False 
	for i in B:
		ses = A.find(i)
		if ses > 0:
			c = True
	if int(c) == 1:
		print("Yes the elements of string B are found in string A")
	else:
		print("No the elements of string B aren't found in string A")

	
# my_split() function take two arguments one as a string an another string as an delimiter and return a list of substrings separated by the delimiter much like the .split() method.
def my_split(b, c):
	Lis = []
	ses = ""
	for i in b:
		if i == c:
			Lis.append(ses)
			ses = ""
			continue
		ses += i
	Lis.append(ses)
	return Lis



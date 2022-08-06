def max (a,b):
	if a > b:
		return a
	else: 
		return b
a = 4
b = 5
print(max(a, b))

print('----------------------------------------------------')

def printme(str):
	print(str)
	return

printme('123')
printme('abc')

print('----------------------------------------------------')

def printinfo(arg1, *vartuple):
	print(arg1)
	print(vartuple)

printinfo(70,60,50)

print('----------------------------------------------------')

def printinfo(arg1, **vartuple):
	print(arg1)
	print(vartuple)

printinfo(70,a=60,b=50)
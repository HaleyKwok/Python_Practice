list = [1,2,3,4]
it = iter(list)  #create iteration
print(next(it))  # output the next elemnt 
print(next(it))

#####
list = [1,2,3,4]
it = iter(list)
for x in it:
	print(x, end=" ")
print()

######
import sys

list = [1,2,3,4]
it = iter(list)

while True:
	try:
		print(next(it))
	except StopIteration:
		sys.exit()



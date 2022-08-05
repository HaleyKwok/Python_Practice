def this_fails():
	x = 1/0
try: 
	this_fails()
except ZeroDivisionError as err:
	print('Handling run-time error:', err)


print('----------------------------------------------------')

def functionName( level ):
    if level < 1:
        raise Exception("Invalid level!", level) # after raising an error, no execution afterwards

print('----------------------------------------------------')
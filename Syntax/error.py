# try/except
while True: 
	try: 
		x = int(input('Please input a number.'))
		break
	except ValueError:
		print('Error!')

print('----------------------------------------------------')

# try/except...else
import sys
for arg in sys.argv[1:]:
    try:
        fh = open("testfile", "w")
        fh.write("This is a test file for testing for exceptions!!!")
    except IOError:
        print("Error: file not found or failed to read file")
    else:
        print("Content was written to file successfully")
        fh.close()

# try-finally
try:
    fh = open("testfile", "w")
    fh.write("testing")
finally:
    print("Error!")

print('----------------------------------------------------')

# func()
def this_fails():
	x = 1/0
try: 
	this_fails()
except ZeroDivisionError as err:
	print('Handling run-time error:', err)


print('----------------------------------------------------')


# raise
def functionName(level):
    if level < 1:
        raise Exception("Invalid level!", level) # after raising an error, no execution afterwards

print('----------------------------------------------------')
class MyNumbers:
	def __iter__(self):
		self.a = 1
		return self
	
	def __next__(self):
		x = self.a
		self.a += 1
		return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#####

class MyNumbers:
	def __iter__(self):
		self.a = 1
		return self
	
	def __next__(self):
            if self.a <= 20:
                x = self.a
                self.a += 1
                return x
            else:
                raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
	print(x)



#####
import sys 
def fibonacci(n):
	a,b,counter = 0, 1, 0
	while True: 
		if (counter > n):
			return 
		yield a
		a,b = b, a+b
		counter += 1
f = fibonacci(10)

while True:
	try:
		print(next(f), end=" ")
	except StopIteration:
		sys.exit()

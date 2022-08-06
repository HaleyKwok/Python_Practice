n = 100
sum = 0
counter = 1
while counter <= n:
	sum = sum + counter 
	counter += 1
print(f'{sum}')

print('----------------------------------------------------')

count = 0
while count < 5:
	print(count, " is smaller than 5")
	count = count + 1
else: 
	print(count, " is larger or equal to 5")

print('----------------------------------------------------')

n = 0
sum = 0
for n in range(0,101):
    sum += n
print(sum)

print('----------------------------------------------------')

sites = ['Baidu', 'Google', 'Meta', 'Taobao']
for site in sites: 
	if site == 'Meta':
		print('Facebook')
		break
	print('looping ' + site)
else: 
	print('no looping data')
print('Finish!')

print('----------------------------------------------------')

for i in range(1,6):
	for j in range(1, i+1):
		print("*",end='')
	print('\r')

print('----------------------------------------------------')

#外边一层循环控制行数
#i是行数
i=1
while i<=9:
     #里面一层循环控制每一行中的列数
     j=1
     while j<=i:
          multiple =j*i
          print("%d*%d=%d"%(j,i,multiple), end="  ")
          j+=1
     print("")
     i+=1

print('----------------------------------------------------')

sites = ['Baidu', 'Google', 'Meta', 'Taobao']
for site in sites:
	if len(site) != 4:
		print(f'hello, {site}')
		continue 
	if site == 'Taobao':
		break
print('Done!')

print('----------------------------------------------------')

for letter in 'Google':
	if letter == 'o':
		pass
		print('pass')
	print('the letter is', letter)
print('Goodbye!')
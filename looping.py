n = 100

sum = 0
counter = 1
while counter <= n:
	sum = sum + counter 
	counter += 1
print(f'{sum}')


count = 0
while count < 5:
	print(count, " is smaller than 5")
	count = count + 1
else: 
	print(count, " is larger or equal to 5")


n = 0
sum = 0
for n in range(0,101):
    sum += n
print(sum)

sites = ['Baidu', 'Google', 'Meta', 'Taobao']
for site in sites: 
	if site == 'Meta':
		print('Facebook')
		break
	print('looping ' + site)
else: 
	print('no looping data')
print('Finish!')

sites = ['Baidu', 'Google', 'Meta', 'Taobao']
for site in sites:
	if len(site) != 4:
		print(f'hello, {site}')
		continue 
	if site == 'Taobao':
		break
print('Done!')
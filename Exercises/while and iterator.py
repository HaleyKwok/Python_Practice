from re import I


exp = [2340, 2500, 2100, 2340, 3100] # 0 1 2 3 4
total = 0  # define total
for i in range(len(exp)):
    print('Month:', (i+1), 'Expense:', exp[i])
    total = total + exp[i]
print('the total amount is:', total)

print('------------------------------------')

key_location ='chair'
location = ['garage', 'living room', 'chair', 'closet']
for i in location:
    if i == key_location:
        print('you find the key in', i)
        break
    else:
        print('find it again!')

print('------------------------------------')

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0
for item in result:
    if item == 'heads':
        count += 1
print('heads is', count)

print('------------------------------------')

expense_list = [2340, 2500, 2100, 3100, 2980]
month_list = ["January", "February", "March", "April", "May"]

month = -1 # define month
expense = int(input('input your expense: '))

for i in expense_list:
    if i == expense:
        month = expense_list.index(i)
        break
if month == -1:
    print('Expense not found! Error!')
else:
    print('you have expense in',month_list[month], ', it is', expense_list[month])

print('------------------------------------')

for i in range(5):
    print(f"You ran {i+1} miles") # i starts with zero hence adding 1
    tired = input("Are you tired? ")
    if tired == 'yes':
        break

if i == 4: # 4 because the index starts from 0
    print("Hurray! You are a rock star! You just finished 5 km race!")
else:
    print(f"You didn't finish 5 km race but hey congrats anyways! You still ran {i+1} miles")

print('------------------------------------')

for i in range(1,6):
    s = '' #name 's' is not defined
    for j in range(i):  #cannot write for j in i
        s += '*'
    print(s)

print('------------------------------------')

for i in range(1,6):
    for j in range(i):
        print('*', end='')
    print()

print('------------------------------------')

print('*')
print('**')
print('***')
print('****')
print('*****')

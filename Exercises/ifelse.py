indian = ['samosa', 'daal', 'naan']
chinese = ['egg role', 'pot sticker', 'fried rice']
italian = ['pizza', 'pasta', 'risotta']

foodstyle = str(input('enter the food style:'))

'''
list name
'''
if foodstyle == 'indian':
    print(indian)
elif foodstyle == 'chinese':
    print(chinese)
elif foodstyle == 'italian':
    print(italian)



# return 
# enter the food style: chinese 
# ['egg role', 'pot sticker', 'fried rice']

print('--------------------------------------------------------')

indian = ['samosa', 'daal', 'naan']
chinese = ['egg role', 'pot sticker', 'fried rice']
italian = ['pizza', 'pasta', 'risotta']

dish = str(input('enter the dish:'))

'''
element
'''
if dish in indian:
    print('indian')
    
elif dish in chinese:
    print('chinese')
elif dish in italian:
    print('italian')
else:
    print('Error! Please enter again!')

print('--------------------------------------------------------')

# return
# enter the dish:samosa
# indian

## Exercise: Python If Condition
# 1. Using following list of cities per country,
#     ```
#     india = ["mumbai", "banglore", "chennai", "delhi"]
#     pakistan = ["lahore","karachi","islamabad"]
#     bangladesh = ["dhaka", "khulna", "rangpur"]
#     ```
# Write a program that asks user to enter a city name and it should tell which country the city belongs to

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = input("Enter city name: ")

if city in india:
    print(f"{city} is in india")
elif city in pakistan:
    print(f"{city} is in pakistan")
elif city in bangladesh:
    print(f"{city} is in bangladesh")
else:
    print(f"I won't be able to tell you which country {city} is in! Sorry!")


print('--------------------------------------------------------')



## Exercise: Python If Condition
# 1. Using following list of cities per country,
#     ```
#     india = ["mumbai", "banglore", "chennai", "delhi"]
#     pakistan = ["lahore","karachi","islamabad"]
#     bangladesh = ["dhaka", "khulna", "rangpur"]
#     ```
#Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city1 = input("Enter city 1: ")
city2 = input("Enter city 2: ")

if city1 in india and city2 in india:
    print("Both cities are in india.")
elif city1 in pakistan and city2 in pakistan:
    print("Both cities are in pakistan.")
elif city1 in bangladesh and city2 in bangladesh:
    print("Both cities are in bangladesh.")
else:
    print("They don't belong to same country.")



print('--------------------------------------------------------')

## Exercise: Python If Condition
# 2. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
#     1. Ask user to enter his fasting sugar level
#     2. If it is below 80 to 100 range then print that sugar is low
#     3. If it is above 100 then print that it is high otherwise print that it is normal
sugar = float(input("Please enter your fasting sugar level:"))
# sugar = float(sugar)
if sugar < 80:
    print("Your sugar is low, go eat some jalebi :)")
elif sugar > 100:
    print("Your sugar is high, stop eating all mithais..!")
else:
    print("Your sugar is normal, relax and enjoy your life!")


print('--------------------------------------------------------')
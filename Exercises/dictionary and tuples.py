population = {
    'china': 143,
    'india': 136,
    'usa': 32,
    'pakistan': 21
}

def add():
    country=input("Enter country name to add:").lower() #方法转换字符串中所有大写字符为小写
    if country in population:
        print("Country already exist in our dataset. Terminating")
        return
    p=input(f"Enter population for {country}:")
    p=float(p)
    population[country]=p # Adds new key value pair to dictionary
    print_all()

def remove():
    country = input("Enter country name to remove:").lower()
    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        return
    del population[country]
    print_all()

def query():
    country = input("Enter country name to query:").lower()
    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        return
    print(f"Population of {country} is: {population[country]} crore")

def print_all():
    for country, p in population.items():
        print(f"{country}==>{p}")

def main():
    op=input("Enter operation (add, remove, query or print):")
    if op.lower() == 'add':
        add()
    elif op.lower() == 'remove':
        remove()
    elif op.lower() == 'query':
        query()
    elif op.lower() == 'print':
        print_all()

if __name__ == '__main__':
    main()
'''
Enter operation (add, remove, query or print):ADD
Enter country name to add:UK
Enter population for uk:23
china==>143
india==>136
usa==>32
pakistan==>21
uk==>23.0
'''
print('----------------------------------------------------')

import math 
def circle_calculation(r):
    area = math.pi*(r**2)
    circumference = 2*math.pi*r
    diameter = 2*r
    return area, circumference, diameter 

if __name__ == '__main__':
    r = float(input('please enter the radius of the circle:'))
    area, circumference, diameter = circle_calculation(r)
    print(f"area {area}, circumference {circumference}, diameter {diameter}")
'''
please enter the radius of the circle:5
area 78.53981633974483, circumference 31.41592653589793, diameter 10.0
'''
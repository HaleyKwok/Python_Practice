# function body
def calculate_total(exp): #function name; input  -> function arguments
    total = 0
    for i in exp: #loop body
        total = total + i 
    return total #return value


tom_exp_list = [2100,3400,3500]
joe_exp_list = [200,500,700]

tom_total = calculate_total(tom_exp_list)
joe_total = calculate_total(joe_exp_list)

print("Tom's total expenses:", tom_total)
print("Joe's total expenses:", joe_total)


print('------------------------------------')

total = 0  #global variable 
def sum (a,b=0):
    print('a:',a) 
    print('b:',b)
    
    total=a+b  
    return total 
print(total)  
n=sum(5) # default here, since you only enter a
print('total:', n)

print('------------------------------------')

def pattern(n):
    for i in range(n):
        for j in range(i+1):
            print('*', end='')
        print()
print_pattern = int(input("Please input the number that you would like to print:"))
pattern(print_pattern)

print('------------------------------------')
# 1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
# ```
# area = (1/2)*base*height
# ```
#
# 2. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# ```
# rectangle area=length*width
# ```
# If no shape is supplied then it should take triangle as a default shape

def area(d1,d2,shape):
    if shape=='triangle':
        area=0.5*d1*d2
        return area
    elif shape=='rectangle':
        area=d1*d2
        return area
    else:
        print("Please enter valid shape")
        return None

triangle_base=int(input("Please enter the base of triangle:"))
triangle_height=int(input("Please enter the height of triangle:"))
triangle_area = area(triangle_base,triangle_height, 'triangle')
print("Area of triangle is:",triangle_area)

rectangle_length = int(input("Please enter the length of rectangle:"))
rectangle_width = int(input("Please enter the width of rectangle:"))
rectangle_area = area(rectangle_length,rectangle_width, 'rectangle')
print("Area of rectangle is:",rectangle_area)

print('------------------------------------')
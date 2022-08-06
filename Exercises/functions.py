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
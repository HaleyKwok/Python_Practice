class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old."
    def say_hi(self):
        print(f"Hi, my name is {self.name}.")
    def say_bye(self):
        print(f"Bye, my name is {self.name}.")
    def say_age(self):
        print(f"I am {self.age} years old.")
tom = Human('Tom', 20)
tom.say_hi()
tom.say_bye()
tom.say_age()
print(tom)

# Hi, my name is Tom.
# Bye, my name is Tom.
# I am 20 years old.
# Tom is 20 years old.
print('----------------------------------------------------')


class Human:
    def __init__(self, name, occupation): #whenever, self is data itself, need to put it at the beginning 
    # property
        self.name = name
        self.occupation = occupation
    
    # method 
    def do_work(self):
        if self.occupation == 'tennis player':
            print(self.name, 'plays tennis')
        elif self.occupation == 'actor':
            print(self.name, 'shoots a film')
            
    def speaks(self):
        print(self.name, 'says how are you?')
    
    def __str__(self):
        return f"{self.name} is a {self.occupation}."

joe = Human('Joe', 'tennis player')
joe.do_work()
joe.speaks()
print(joe)

# Joe plays tennis
# Joe says how are you?
# Joe is a tennis player.
print('----------------------------------------------------')


tom = Human('Tom', 'actor')
tom.do_work()
tom.speaks()
print(tom)

# Tom shoots a film
# Tom says how are you?
# Tom is a actor.
print('----------------------------------------------------')

        
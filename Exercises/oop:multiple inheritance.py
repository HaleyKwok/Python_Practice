class Father():
    def gardening(self):
        print("I enjoy gardening")
        
class Mother():
    def cooking(self):
        print("I enjoy cooking")
                
class Child(Father,Mother):
    def sports(self):
        print("I enjoy sports")

    # def __init__(self): # constructor
    #     super().__init__()
    #     super().cooking()
    #     super().gardening()
    #     self.sports()

c = Child()
c.gardening()
c.cooking()
c.sports()

# I enjoy gardening
# I enjoy cooking
# I enjoy sports

print('----------------------------')

# same function name in the child class will override the function in the parent class.
class Father():
    def skills(self):
        print("I enjoy gardening, programming")
        
class Mother():
    def skills(self):
        print("I enjoy cooking, arts")
                
class Child(Father,Mother):
    def skills(self):
        print("I enjoy sports")
        
c = Child()
c.skills()

# I enjoy sports

print('----------------------------')

class Father:
    def skills(self):
        print("I enjoy gardening, programming")

class Mother:
    def skills(self):
        print("I enjoy cooking, arts")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("I enjoy sports")

c = Child()
c.skills()

# I enjoy gardening, programming
# I enjoy cooking, arts
# I enjoy sports
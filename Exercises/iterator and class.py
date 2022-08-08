class RemoteControl:
    def __init__(self):
        self.channels = ['HBO', 'Disney', 'Star World']
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == len(self.channels): 
            raise StopIteration
        else:
            self.index += 1
            return self.channels[self.index - 1] 


r = RemoteControl()
itr = iter(r)
print(next(itr))
print(next(itr))


print('----------------------------')

class RemoteControl():
    def __init__(self):
        self.channels = ['HBO', 'cnn', 'abc', 'espn']
        self.index = -1
        
        #need to add this to return the data itself
    def __iter__(self): 
        return self
    
    def __next__(self):
        self.index +=1
        if self.index == len(self.channels):
            raise StopIteration
        
        return self.channels[self.index] 
    
r = RemoteControl()
itr = iter(r)
print (next(itr))
print (next(itr))


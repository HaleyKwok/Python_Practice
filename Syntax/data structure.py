a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))

a.insert(2, -1)
print(a)

a.append(333)
print(a)

a.index(333)
print(a)

a.remove(333)
print(a)

a.reverse()
print(a)

a.sort()
print(a)

print('----------------------------------------------------')


stack = [3,4,5]
stack.append(6)
stack.append(7)

print(stack)
stack.pop()
print(stack)

print('----------------------------------------------------')

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves

queue.popleft()                 # The second to arrive now leaves
print(queue)                    # Remaining queue in order of arrival

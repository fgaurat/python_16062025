from collections import deque

l = [10,20,30,40,50]

l.append(60)
print(l)
last_value = l.pop()
print(l)
print("last_value",last_value)
l.insert(0,-10)
print(l)
first_value = l.pop(0)
print(l)
print("first_value",first_value)

d = deque(l)
print(d)
d.appendleft(-10)
print(d)
first_value = d.popleft()
print("first_value",first_value)


# l = [10,20,30,40,50]
l = []

for i in range(10,60,10):
    l.append(i)
print(l)
# l = [i for i in range(10,60,10)]

l = list(map(lambda i:i,range(10,60,10)))
print(l)


l = [i for i in range(10,60,10)]

lines = [' ligne 01', ' ligne 02   ','ligne 03   ']
clean_lines = [line.strip() for line in lines]
print(clean_lines)

clean_lines_2 = [line.strip() for line in lines if "3" not in line]
print(clean_lines_2)

del clean_lines_2[-1]
print(clean_lines_2)
# a = 2
# del a
# print(a)
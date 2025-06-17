
a=3

def f():
    global a
    a=5    
    print(a)
    
print("init",a)
f()
print("end",a)




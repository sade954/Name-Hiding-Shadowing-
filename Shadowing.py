#Scoping using the global keyword:
y = 5


Sometimes called shadowing
def set_x(z): 
    x = z
    global a
    x = y
    print("X is:", x)
    a = 7
    
    
print("y before set_x:", y)

set_x(10)
print("y after set_x:", y)
print("a after set_x:", a)

#To run this in the terminal, type python3.7 <filename>.py, and this should be the output:
y before set_x: 5
X is: 5
y after set_x: 5
a after set_x: 7
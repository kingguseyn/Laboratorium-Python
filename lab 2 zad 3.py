x = float(input("first number:"))
y = float(input("second number:"))
z = input("what operator:")
if z=='*':
    print (x*y)
elif z == '-':
    print (x-y)
elif z== '+':
    print (x+y)
elif z == '**':
    print (x**y)
elif z == '/':
    if y == 0:
        print("can`t")
else:
    print (x/y)









print("Hello Welcome To my program")
print("what would you like to perform \n "
      "For BITWISE COMPLEMENT type 'c' \n "
      "For BITWISE AND type 'a' \n "
      "For BITWISE OR type 'o' \n "
      "For BITWISE XOR type 'x' ")
l = ['c', 'a', 'o', 'x']
y = input("Function")

if y == 'c':
    print('Enter the value of which you want COMPLEMENT')
    c = int(input("complement "))
    p = ~c
    print("COMPLEMENT Operation Value Is", p)
else:

    print('Enter first value for BITWISE operation number ')
    xa =  int(input('first value '))
    print('Enter second value for BITWISE operation number ')
    xb =  int(input('second value '))

    if  y == 'a':
        a = xa & xb
        print("And Operation Value Is", a)
    elif  y == 'o':
        o = xa | xb
        print("And Operation Value Is", o)
    elif  y == 'x':
        x = xa ^ xb
        print("And Operation Value Is", x)
    else:
        print("No operation assigned")
print('Thank you')

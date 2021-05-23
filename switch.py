print("Welcome to burger world\nKindly place your order\n")
print("Menu\n 1.Burger - 70\n 2.Pizza - 150\n 3.Chowmien - 60\n 4.Manchurian - 90\n 5.Paneer tikka - 110\n "
      "6.Chilli Paneer - 100\n 0.NOTHING ELSE")
x = 7
fc = 0
for i in range(x):
    y = int(input("enter food number"))
    if y == 1:
        item= "Burger"
        print(item)
        z = int(input("enter the quantity"))
        cost = 70 * z
        print("cost = ", cost)
    elif y == 2:
        item = "Pizza"
        print(item)
        z = int(input("enter the quantity"))
        cost = 150 * z
        print("cost = ", cost)
    elif y == 3:
        item = "Choemien"
        print(item)
        z = int(input("enter the quantity"))
        cost = 60 * z
        print("cost = ", cost)
    elif y == 4:
        item = "Manchurian"
        print(item)
        z = int(input("enter the quantity"))
        cost = 90 * z
        print("cost = ", cost)
    elif y == 5:
        item = "Paneer Tikka"
        print(item)
        z = int(input("enter the quantity"))
        cost = 110 * z
        print("cost = ", cost)
    elif y == 6:
        item = "Cilli Paneer"
        print(item)
        z = int(input("enter the quantity"))
        cost = 100 * z
        print("cost = ", cost)
    elif y == 0:
        break
    else:
        print("invalid input")


    fc = fc + cost
print("Total",fc)






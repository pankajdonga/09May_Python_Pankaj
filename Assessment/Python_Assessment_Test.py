fruit_shop={}

def manager():
    print('\nFruit Market Manager\n')
    print('1) Add Fruit Stock')
    print('2) View Fruit Stock')
    print('3) Update Fruit Stock\n')
    add_fruit=int(input("Enter Your Choice: "))
    return add_fruit

def add_stock():
    fruit_name=input("Enter Fruit Name: ")
    fruit_qty=int(input("Enter Fruit Quantity(in kg): "))
    fruit_price=input("Enter Fruit Price: ")
    more_oper=input('Do you want to perform more operations: press y for yes and n for no : ')
    return fruit_name,fruit_qty,fruit_price,more_oper


print('\nWELCOME TO FRUIT MARKET\n')
print('1) Manager')
print('2) Customer\n')

role_ch=int(input("Select Your Role: "))

if role_ch == 1:
    a=manager()
else:
    print('Enter Valid Role Choice.....')

if a == 1:
    print('\nADD FRUIT STOCK')
    x=add_stock()
    fruit_shop[x[0]]={}
    fruit_shop[x[0]]['qty'] = x[1]
    fruit_shop[x[0]]['price'] = x[2]
    if x[3] == 'y' or x[3] == 'Y':
        b=manager()
        if b == 1:
            y=add_stock()
            fruit_shop[y[0]]={}
            fruit_shop[y[0]]['qty'] = y[1]
            fruit_shop[y[0]]['price'] = y[2]
        if b == 2:
            print(fruit_shop)
        if b == 3:
            z=add_stock()
            fruit_shop[z[0]]={}
            fruit_shop[z[0]]['qty'] = z[1]
            fruit_shop[z[0]]['price'] = z[2]
else:
    print("Enter Valid Choice")





    
    




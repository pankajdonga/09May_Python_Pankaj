fruit_shop={}

def manager():
    print(f'\n{" "*40}Fruit Market Manager\n')
    print(f'{" "*40}1) Add Fruit Stock')
    print(f'{" "*40}2) View Fruit Stock')
    print(f'{" "*40}3) Update Fruit Stock\n')

def add_stock():
    print('\nADD FRUIT STOCK')
    fruit_name=input("Enter Fruit Name: ")
    fruit_qty=int(input("Enter Fruit Quantity(in kg): "))
    fruit_price=input("Enter Fruit Price: ")
    fruit_shop[fruit_name] = {'Qty':fruit_qty, 'Price':fruit_price}

def update_stock():
    print('\nUPDATE FRUIT STOCK')
    fruit_name=input("Enter Fruit Name: ")
    fruit_qty=int(input("Enter Fruit Quantity(in kg): "))
    fruit_price=input("Enter Fruit Price: ")
    if fruit_name in fruit_shop.keys():
        fruit_shop[fruit_name] = {'Qty':fruit_qty, 'Price':fruit_price}
    else:
        fruit_shop[fruit_name] = {'Qty':fruit_qty, 'Price':fruit_price}



print(f'\n{" "*40}WELCOME TO FRUIT MARKET\n')
print(f'{" "*40}1) Manager')
print(f'{" "*40}2) Customer\n')

role_ch=int(input("Select Your Role: "))

#================ Manager Section ================#

if role_ch == 1:
    manager()
    add_fruit=int(input("Enter Your Choice: "))

    if add_fruit == 1:
        add_stock()

    if add_fruit == 2:
        print(f'\n{fruit_shop}')

    if add_fruit == 3:
        update_stock()

    while True:
        more_oper=input('\nDo you want to perform more operations: press y for yes and n for no : ')
        if more_oper == 'y':
            manager()
            add_fruit=int(input("Enter Your Choice: "))

            if add_fruit == 1:
                add_stock()

            if add_fruit == 2:
                print(f'\n{fruit_shop}')

            if add_fruit == 3:
                update_stock()
        else:
            break

#================ Customer Section ================#

new_shop={'Apple': {'Qty': 10, 'Price': 100},
          'Banana': {'Qty': 20, 'Price': 40},
          'Pineapple': {'Qty': 4, 'Price': 80},
          'Kiwi': {'Qty': 9, 'Price': 200},
          'Mango': {'Qty': 15, 'Price': 120}}

def purchase():
    fruit_name=input("\nEnter Fruit Name: ")
    fruiy_qty=int(input("Enter Fruit Quantity(in kg): "))
    for i,j in new_shop.items():
        if fruit_name == i:
            price=list(j.values())[1]
            qty=list(j.values())[0] - fruiy_qty
            new_shop[fruit_name] = {'Qty':qty, 'Price':price}
    print('\n----------------------------')
    print('        CASH RECEIPT'          )
    print('----------------------------')     
    print(f'1). {fruit_name}               {fruiy_qty*price}')


if role_ch == 2:
    for i,j in new_shop.items():
        print(f'{i}: {j}')

    purchase()

    while True:
        purchase_more=input('\nDo you want to Purchase more?: press y for yes and n for no : ')
        if purchase_more == 'y':
            for i,j in new_shop.items():
                print(f'{i}: {j}')

            purchase()
        else:
            break

    




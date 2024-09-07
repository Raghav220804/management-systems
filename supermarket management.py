# -----------------SUPERMARKET MANAGEMENT SYSTEM--------------------
items = []

while True:
    input('Press enter to continue.')
    print('------------------Welcome to the supermarket------------------')
    print('1. View items\n2. Add items for sale\n3. Purchase items\n4. Search items\n5. Edit items\n6. Exit')
    choice = input('Enter the number of your choice: ')

    if choice == '1':
        print('------------------View Items------------------')
        if not items:
            print('No items in the inventory.')
        else:
            print(f'The number of items in the inventory are: {len(items)}')
            print('Here are all the items available in the supermarket:')
            for item in items:
                print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: ${item['price']}")

    elif choice == '2':
        print('------------------Add Items------------------')
        print('To add an item, fill in the form')
        item = {}
        item['name'] = input('Item name: ')
        while True:
            try:
                item['quantity'] = int(input('Item quantity: '))
                break
            except ValueError:
                print('Quantity should only be in digits')
        while True:
            try:
                item['price'] = int(input('Price $: '))
                break
            except ValueError:
                print('Price should only be in digits')
        items.append(item)
        print('Item has been successfully added.')

    elif choice == '3':
        print('------------------Purchase Items------------------')
        if not items:
            print('No items available for purchase.')
        else:
            purchase_item = input('Which item do you want to purchase? Enter name: ')
            for item in items:
                if purchase_item.lower() == item['name'].lower():
                    if item['quantity'] > 0:
                        print(f'Pay ${item["price"]} at the checkout counter.')
                        item['quantity'] -= 1
                    else:
                        print('Item out of stock.')
                    break
            else:
                print('Item not found.')

    elif choice == '4':
        print('------------------Search Items------------------')
        find_item = input("Enter the item's name to search in inventory: ")
        for item in items:
            if item['name'].lower() == find_item.lower():
                print(f"The item named {find_item} is displayed below with its details:")
                print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: ${item['price']}")
                break
        else:
            print('Item not found.')

    elif choice == '5':
        print('------------------Edit Items------------------')
        item_name = input('Enter the name of the item that you want to edit: ')
        for item in items:
            if item_name.lower() == item['name'].lower():
                print(f"Here are the current details of {item_name}:")
                print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: ${item['price']}")
                item['name'] = input('New item name: ')
                while True:
                    try:
                        item['quantity'] = int(input('New item quantity: '))
                        break
                    except ValueError:
                        print('Quantity should only be in digits')
                while True:
                    try:
                        item['price'] = int(input('New price $: '))
                        break
                    except ValueError:
                        print('Price should only be in digits')
                print('Item has been successfully updated.')
                break
        else:
            print('Item not found.')

    elif choice == '6':
        print('------------------Exited------------------')
        break

    else:
        print('You entered an invalid option.')

# initialize array
# ask user if they want to make a new customer
# if no, break the loop and print the list
# if yes, ask the user to name the customer
# put the first name in a key and the last name in a key
# ask the user for the customers lunch order
# put the order in that customers dictionary

customers = [{"fName": "Joe", "lName": "Schmoe", "Order": "Chicken"}]

while True:

    add_customer = input('Add another customer to the list? ')
    if add_customer == 'n':
        for i in customers:
            print("{} {} : {}".format(i['fName'], i['lName'], i['Order']))
        break

    if add_customer == 'y':
        fName, lName = input("Enter the customer's name: ").split()
        order = input("Enter the customer's order: ")

        customers.append({'fName': fName, 'lName': lName, 'Order': order})






#define the menu of restaurant

menu = {'pizza':40,
        'pasta':50,
        'burger':60,
         'salad':70,
         'coffe':80,
}

#greet
print("welcome to python restaurant")
print("pizza :Rs40\n pasta;:Rs50\n burger:Rs60 \n salad:Rs 70\n coffee:Rs80\n")

order_total = 0

item_1 =input("inter the name of item you want to order")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order ")

else :
    print(f"ordered item {item_1} is not avaible yet!")

another_item = input("do you want to add another item?(yes/no)")
if another_item == "yes" :
    item_2 = input("enter the name of second item =")
    if item_2 in menu:

        order_total +=menu[item_2]
        print(f"item {item_2}hass been added to order")

    else:
        print(f"ordered item {item_2} is not avaible!")

print(f"the total amount of item  to pay is {order_total} ")








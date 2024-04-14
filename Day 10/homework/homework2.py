item_price = float(input("please enter price or the item: "))
budget = float(input("enter your budget: "))

if budget >= item_price:
    print("you can aford the item")
else:
    needed_amount = item_price - budget
    print("you need ", needed_amount,"to buy the item")
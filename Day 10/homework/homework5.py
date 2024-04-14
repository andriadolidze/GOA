ticket_price = 10

num_tickets = int(input("how many tickets?: "))

if num_tickets < 5:
    print(ticket_price * num_tickets)
else:
    discounted_price = ticket_price * 0.7
total_price = discounted_price * num_tickets
print(total_price)
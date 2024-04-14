user_input = int(input("რამდენი გაქვს ხელფასი?: "))

if user_input > 10000:
    print("გოაში სწავლობდი?")
elif user_input < 10000 and user_input > 1000: 
    print("you mid")
elif user_input < 1000:
    print("შემოსულიყავი გოაში, მატრიცელო")
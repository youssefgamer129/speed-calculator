# Coffee shop management system

print("Welcome to the coffee shop management system")

answer = input("Do you want to drink something? (yes/no) ").lower()

if answer == "yes":
    drink = input("What do you want to drink? (tea/coffee) ").lower()

    if drink == "tea":
        tea_type = input("What kind of tea do you want? (black/green) ").lower()
        sugar = input("Do you want sugar in your tea? (yes/no) ").lower()

        if tea_type == "black":
            if sugar == "yes":
                print("Here is your black tea with sugar.")
            elif sugar == "no":
                print("Here is your black tea without sugar.")
        elif tea_type == "green":
            if sugar == "yes":
                print("Here is your green tea with sugar.")
            elif sugar == "no":
                print("Here is your green tea without sugar.")

    elif drink == "coffee":
        coffee_type = input("What kind of coffee do you want? (black/with milk) ").lower()
        sugar = input("Do you want sugar in your coffee? (yes/no) ").lower()

        if coffee_type == "black":
            if sugar == "yes":
                print("Here is your black coffee with sugar.")
            elif sugar == "no":
                print("Here is your black coffee without sugar.")
        elif coffee_type == "with milk":
            if sugar == "yes":
                print("Here is your coffee with milk and sugar.")
            elif sugar == "no":
                print("Here is your coffee with milk without sugar.")

    else:
        print("Sorry, we don't have that drink.")

elif answer == "no":
    print("No problem, have a nice day!")

else:
    print("Sorry, we can't help you.")
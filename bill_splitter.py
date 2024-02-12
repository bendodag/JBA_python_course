# write your code here
import random


def lucky_feature(list_of_guests, guests_dict, n_of_guests, bill):
        rand_name = list_of_guests[random.randint(0, n_of_guests - 1)]
        print(f"{rand_name} is the lucky one!")
        guests_dict[rand_name] = 0
        list_of_guests.remove(rand_name)

        for i in range(0, n_of_guests - 1):
            guests_dict[list_of_guests[i]] = round(bill/(n_of_guests - 1), 2)
        
        return guests_dict


guests = dict()
initial_bill = 0
guest_names = []

num_of_guests = int(input("Enter the number of friends joining (including you):"))

if num_of_guests <= 0:
    print("No one is joining for the party")
else:
    for i in range(0, num_of_guests):
        guest_name = input("Enter the name of every friend (including you), each on a new line:")
        guest_names.append(guest_name)

    total_bill = float(input("Enter the total bill value:"))

    for i in range(0, num_of_guests):
        guests[guest_names[i]] = round(total_bill/num_of_guests, 2)

    lucky_feat = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    
    if lucky_feat == "Yes":
        guests = lucky_feature(guest_names, guests, num_of_guests, total_bill)
        
    else:
        print("No one is going to be lucky") 

    print(guests)

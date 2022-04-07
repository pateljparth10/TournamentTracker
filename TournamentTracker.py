
participants_list = []
start_up_valid = True



def valid_name():
    valid_name_loop = True
    while valid_name_loop == True:
        name_p = input("Participant Name: ")
        space = name_p.find(" ")
        first_name = name_p[0:space]
        first_name.strip()
        last_name = name_p[space+1 : len(name_p)]
        last_name.strip()
        if first_name.isalpha():
            if last_name.isalpha():
                valid_name_loop = False
                return name_p
        else:
            print("That is not a valid name. Please try again.")

def valid_number():
    valid_number_loop = True
    while valid_number_loop == True:
        number_p = input("Slot Number: ")
        if str(number_p).isdigit():
            if int(number_p) <= len(participants_list) and int(number_p) > 0:
                valid_number_loop = False
                return number_p
            else:
                print("Slot number does not exist. Please try again.")
        else:
            print("That is not a valid number. Please try again.")


while start_up_valid == True:
    print("Welcome to Tournament R Us")
    print("==========================")
    number_of_participants = input("Enter the number of participants: ")
    if str(number_of_participants).isdigit():
        start_up_valid = False
    else:
        print("That is not a valid number. Please try again.")
    
for i in range(int(number_of_participants)):
    participants_list.append(None)

print(f"There are {number_of_participants} participants slots ready for sign-up")


def sign_up():
    sign_up_loop = True
    while sign_up_loop:
        print("Participants Sign Up")
        print("==============================")
        participant_name = valid_name()
        slot_number = valid_number()
        if participants_list[int(slot_number) -1] == None:
            participants_list[int(slot_number) -1] = participant_name
            print("Success:")
            print(f"{participant_name} is signed up in starting slot #{slot_number}.")
            sign_up_loop = False
        else: 
            print("Error:\n Slot #" + str(slot_number) + " is filled. Please try again." )


sign_up()

def cancel_sign_up():
    cancel_sign_up_loop = True
    while cancel_sign_up_loop:
        print("Participants Cancellation")
        print("==============================")
        slot_number = valid_number()
        participant_name = valid_name()
        if participants_list[int(slot_number) -1] == participant_name:
            participants_list[int(slot_number) -1] = None
            print("Success: ")
            print(f"{participant_name} has been cancelled from starting slot #{slot_number}.")
            cancel_sign_up_loop = False
        else: 
            print("Error:\n" + str(participant_name) + " is not in that starting slot. Please try again." )

cancel_sign_up()
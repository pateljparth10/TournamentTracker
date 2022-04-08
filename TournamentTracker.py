
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
        if participants_list[int(slot_number)-1] == None:
            participants_list[int(slot_number)-1] = participant_name
            print("Success:")
            print(f"{participant_name} is signed up in starting slot #{slot_number}.")
            sign_up_loop = False
        else: 
            print("Error:\n Slot #" + str(slot_number) + " is filled. Please try again." )



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



def view_participants():
    view_participants_loop = True
    while view_participants_loop:
        print("View Participants")
        print("===========================")
        slot_number = valid_number()
        slot_min = int(slot_number) -6
        slot_max = int(slot_number) + 5
        for i in range(slot_min,slot_max):
            if i > -1:
                if i < len(participants_list):
                    print(f"{i+ 1} : {participants_list[i]}")
        view_participants_loop = False

def save_changes():
    save_changes_loop = True
    while save_changes_loop:
        print("Save Changes")
        print("=================")
        answer = input("Save your changes to CSV? [y/n]")
        if answer == "y":
            registration_file = open("C:\Repository\TournamentTracker\Registration.csv","w")
            for position in range(len(participants_list)):
                registration_file.write("%i, %s\n" %(position+ 1, participants_list[position]))
            registration_file.close()
            print("You have saved all changes.")
            save_changes_loop = False
        elif answer == "n":
            print("Your changes have not been saved.")
            save_changes_loop = False
        else:
            print("That is not a valid input.")

sign_up()
sign_up()
view_participants()
save_changes()        


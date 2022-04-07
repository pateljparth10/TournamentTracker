

participants_list = []

start_up_valid = True

while start_up_valid == True:
    print("Welcome to Tournament R Us")
    print("==========================")
    number_of_participants = input("Enter the number of participants: ")
    if str(number_of_participants).isdigit():
        start_up_valid = False
    

print(f"There are {number_of_participants} participants slots ready for sign-up")

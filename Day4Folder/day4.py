# Write all your codes for Day 4 here.
# REMEMBER to change main.py to import this file.
# You can COMMENT out the previous task before going on to the next task
# print("hello from day4")

# password = input("Please enter your password: ")
# counter = 1

# while counter < 5:
#     if password != "Natalie":
#         print("You have tried " + str(counter) + " amount of tries.")
#         password = input("Try again: ")
#         counter = counter + 1
#     else:
#         break

# if counter >= 5:
#         print("You have been locked out.")
# else:
#         print("You have sucessfully logged in")

riddle = input("What do you call a deer with no eyes? ")
counter = 1 

while counter <5:
    if riddle != "No eye dear":
        print("You have tried " + str(counter) + " amount of tries.")
        riddle = input("Please try again: ")
        counter = counter + 1
    else:
        break

if riddle == "No eye dear":
    print("You have answered correctly")    


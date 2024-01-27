import sys

# Some important variables used in the next block.
entry_list = []
tested_dict = {}
num_entries = 0
entry = ""

# Keep adding entries until the user types 'stop entries'.
while entry != 'stop entries':

    # This asks the user to type their entry.
    if num_entries == 0:
        entry = input("What is your first entry? Type it here: ")
    elif num_entries == 1:
        entry = input("What is your second entry? Type it here: ")
    elif num_entries == 2:
        entry = input("What is your third entry? Type it here: ")
    else:
        entry = input("What is your next entry? Type it here, or type 'Stop Entries' to stop: ")

    # When the user types 'stop entries', if there are too few entries, the program ends. Otherwise, it continues to the sorting block.
    if entry.lower() == 'stop entries' or entry.lower() == 'end entries':
        if num_entries <= 2:
            print("Not enough entries! Exiting program.")
            sys.exit()
        else:
            break
    elif entry in entry_list:
        print("You have already listed this entry! Try something else")
    else:
        num_entries += 1
        tested_dict[entry] = []
        entry_list.append(entry)

# These are more important variables used in the sorting block.
chained_reverses = 0
current_pos = num_entries - 1
unsorted_front_pos = -1
unsorted_end_pos = num_entries
end_to_front = True
all_sorted = False

#This determines if the two entries swap positions or not.
def checkSwap(list, current, check):
    while True:
        swap = input(f"Is {entry_list[current]} higher up than {entry_list[check]}? Enter 'yes' or 'no': ")
        if swap.lower() == 'yes' or swap.lower() == 'y':
            list[current], list[check] = list[check], list[current]
            break
        elif swap.lower() == 'no' or swap.lower() == 'n':
            break
        else:
            print(f"Please respond with 'yes' or 'no'. Is {entry_list[current]} higher up than {entry_list[check]}? ")

# This iterates backwards and then forwards though the list, repeatedly, until everything has been sorted into its place.
while all_sorted == False:

    # This exits the loop when everything has been sorted.
    if chained_reverses > 1:
        all_sorted = True

    # This is the logic for going from the end of the list to the front.
    elif end_to_front == True and (current_pos - 1) > unsorted_front_pos:
        if entry_list[current_pos - 1] in tested_dict[entry_list[current_pos]]:
            current_pos -= 1
        else:
            tested_dict[entry_list[current_pos]].append(entry_list[current_pos - 1])
            tested_dict[entry_list[current_pos - 1]].append(entry_list[current_pos])
            current_pos -= 1
            checkSwap(entry_list, current_pos + 1, current_pos)
        chained_reverses = 0
    elif end_to_front == True:
        unsorted_front_pos += 1
        end_to_front = False
        current_pos += 1
        chained_reverses += 1

    # This is the logic for going from the front of the list to the end.
    elif end_to_front == False and (current_pos + 1) < unsorted_end_pos:
        if entry_list[current_pos + 1] in tested_dict[entry_list[current_pos]]:
            current_pos += 1
        else:
            tested_dict[entry_list[current_pos]].append(entry_list[current_pos + 1])
            tested_dict[entry_list[current_pos + 1]].append(entry_list[current_pos])
            current_pos += 1
            checkSwap(entry_list, current_pos, current_pos - 1)
        chained_reverses = 0
    elif end_to_front == False:
        unsorted_end_pos -= 1
        end_to_front = True
        current_pos -= 1
        chained_reverses += 1

# This prints out the finalized list when the sorting is complete.
print("Your list has been sorted! Here is the final list:")
x = 1
for entry in entry_list:
    print(f"{x}. {entry}")
    x += 1
# #TODO: Create a letter using starting_letter.txt
# #for each name in invited_names.txt
# #Replace the [name] placeholder with the actual name.
# #Save the letters in the folder "ReadyToSend".
#
# names = open(file="./Input/Names/invited_names.txt")
# name_list = []
#
# for each_line in names.readlines():
#     each_line = each_line.strip()
#     name_list.append(each_line)
#
# # print(name_list)
#
# letter = open(file="./Input/Letters/starting_letter.txt")
# new_x = letter.read()
# for each_name in name_list:
#     new_letter = new_x.replace("[name]", each_name.strip())
#     print(new_letter)
#     with open(file=f"./Output/ReadyToSend/letter_for_{each_name}.txt", mode="w") as f:
#         f.write(new_letter)

PLACEHOLDER = "[name]"
with open(file="./Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_files:
    letter_content = letter_files.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(file=f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
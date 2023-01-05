PLACEHOLDER="[name]"
with open("./Input/Names/invited_names.txt") as name_file:
    
    names=name_file.readlines()



with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents=letter_file.read()
    for name in names:
        stripped_name=name.strip()
        new_letter=letter_contents.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}","w") as final_letter:
            final_letter.write(new_letter)
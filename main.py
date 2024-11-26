PLACEHOLDER = "[name]"

with open('Input/Names/invited_names.txt', 'r') as names_file:
    names = names_file.readlines()

names = [name.strip() for name in names]

for name in names:
    with open('Input/Letters/starting_letter.txt') as letter_file:
        bp_letter = letter_file.read()
        personalized_letter = bp_letter.replace(PLACEHOLDER, name)

    path = f"Output/ReadyToSend/{name}-letter.txt"

    with open(path, mode="w") as file:
        new_letter = file.write(personalized_letter)



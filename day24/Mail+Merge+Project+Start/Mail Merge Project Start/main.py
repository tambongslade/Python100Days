#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
Names = []

with open("./Input/Names/invited_names.txt") as Name:
    content = Name.read()
    Names.append(content.split("\n"))
    print(len(Names))

for i in range(len(Names[0])):
    with open("./Input/Letters/starting_letter.txt", mode="r") as Letter:
        content = Letter.read()
        letter = content
        name = Names[0][i].strip("{'")
        letter = letter.replace("[name]", f"{name}")
    with open(f"./Output/ReadyToSend/{Names[0][i]}.txt", mode="w") as output:
        output.write(letter)



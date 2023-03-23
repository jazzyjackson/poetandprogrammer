madlib = "Once upon a ____________(noun), there was a ____________(adjective) ____________(noun) who loved to ____________(verb). One day, while ____________(verb + ing), the ____________(noun) stumbled upon a ____________(adjective) ____________(noun) in the middle of the ____________(noun). Without hesitation, the ____________(noun) ____________(verb) towards the ____________(noun) and ____________(verb + ed) it with all their might. Suddenly, a bright light ____________(verb) and a ____________(adjective) ____________(noun) appeared before them, offering a reward for their heroic act. From that day on, the ____________(noun) continued to ____________(verb) with a newfound sense of purpose, always on the lookout for more ____________(adjective) ____________(nouns) to save."

# write the function that takes the string in madlib and replace all the blanks with user input, prompting the user to fill out the blanks with content that matches the parameters in the parentasis to the right of the blank

def madlib_function(madlib):
    # split the madlib string into a list of words
    madlib_list = madlib.split()
    # create a new list to hold the madlib with user input
    madlib_list_with_user_input = []
    # loop through the madlib list
    for word in madlib_list:
        # if the word contains a blank, prompt the user to fill in the blank
        if word.find("___________") != -1:
            # remove the blank from the word
            word = word.replace("___________", "")
            # prompt the user to fill in the blank
            user_input = input(f"Please enter a {word}: ")
            # add the user input to the madlib list
            madlib_list_with_user_input.append(user_input)
        else:
            # add the word to the madlib list
            madlib_list_with_user_input.append(word)
    # join the madlib list into a string
    madlib_string = " ".join(madlib_list_with_user_input)
    # return the madlib string
    return madlib_string

#print the madlib function with the madlib string as the parameter

print(madlib_function(madlib))






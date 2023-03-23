# Create a simple Mad Libs game that asks the user for different types of words (e.g., noun, adjective, verb) and inserts them into a pre-defined story template.

# Define a dictionary of replacements
def create_replacements():
    replacements = {}

    # Prompt the user for input and store it in the dictionary
    replacements['{adjective}'] = input("Enter an adjective: ")
    replacements['{noun}'] = input("Enter a noun: ")
    replacements['{adjective2}'] = input("Enter an adjective: ")
    replacements['{noun2}'] = input("Enter a noun: ")
    replacements['{adjective3}'] = input("Enter an adjective: ")
    replacements['{noun3}'] = input("Enter a noun: ")
    replacements['{noun4}'] = input("Enter a noun: ")
    replacements['{verb5}'] = input("Enter a verb ending in -ing: ")
    replacements['{noun5}'] = input("Enter a noun: ")
    replacements['{verb6}'] = input("Enter a verb in past tense: ")
    replacements['{noun6}'] = input("Enter a noun: ")
    replacements['{verb7}'] = input("Enter a verb: ")
    replacements['{noun7}'] = input("Enter a noun: ")
    replacements['{noun9}'] = input("Enter a plural noun: ")
    replacements['{verb}'] = input("Enter a verb: ")
    return replacements

 # Define the MadLib sentence
mymadlib = "Once upon a time, there was a {adjective} {noun} who lived in a {adjective2} {noun2} in the {adjective3} {noun3}. The {noun4} loved to {verb5} all day long, but one day, the {noun5} {verb6} into a {adjective} {noun6} and couldn't {verb7} anymore. The {noun7} was very sad and didn't know what to do. But then, a {adjective2} {noun} appeared and offered to {verb} the {noun} back to its original form. The {noun} was overjoyed and thanked the {noun} for its {adjective} help. From that day on, the {noun} and the {noun} became the best of {noun9}, and the {noun} learned to {verb5} more carefully"

def madlib_formatter(madlib):
    # Create a dictionary of replacements
    replacements = create_replacements()
    for placeholder, replacement in replacements.items():
        madlib = madlib.replace(placeholder, replacement)
    return madlib

print(madlib_formatter(mymadlib))
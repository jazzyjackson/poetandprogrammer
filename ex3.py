# we're going to write a madlib game
# I'll define a template, and then we'll need a function to grab all the named blanks
# and ask the user for the words to fill them in
# Then I'll need to upgrade the template to an f-string and print it out

# define the template
template = """
Title: Biking and Bagels

One sunny day, {name} decided to {verb} their {adjective} bike through the {adjective} campus. They whizzed past {plural noun} and {plural noun}, feeling the {adjective} breeze in their hair.

Suddenly, a craving for a {adjective} bagel struck them like a {noun}. {Name} made a beeline for the nearest campus {type of building}, where they knew the best bagels were served.

As they approached the counter, the {occupation} asked, "{Question}?" {Name} replied, "{Adjective} {flavor} bagel, please!" The {occupation} handed them a bagel, but to {name}'s surprise, it was shaped like a {noun}!

{Name} couldn't help but {verb} out loud, making everyone in the room join in the {noun}-shaped bagel laughter. From that day on, {name} never looked at bagels the same way again.
"""

# define a function to get the words from the user


def get_words():
    words = {}
    words['name'] = input("Enter a name: ")
    words['verb'] = input("Enter a verb: ")
    words['adjective'] = input("Enter an adjective: ")
    words['plural noun'] = input("Enter a plural noun: ")
    words['noun'] = input("Enter a noun: ")
    words['type of building'] = input("Enter a type of building: ")
    words['occupation'] = input("Enter an occupation: ")
    words['question'] = input("Enter a question: ")
    words['flavor'] = input("Enter a flavor: ")
    return words
# write a slightly different get_words function that performs a regex on the template to extract the key names and then ask the user for input


def get_words():
    words = {}
    # use a regex to extract the key names from the template, simple, dumb regex
    # this will work for this template, but it's not a general solution
    # it will also fail if the template has any other curly braces in it
    # first, split the template into lines
    lines = template.splitlines()
    # then, loop through the lines
    for line in lines:
        # for each line, find all the curly braces
        matches = re.findall(r'{(.*?)}', line)
        # then, loop through the matches
    for match in matches:
            # for each match, ask the user for input
            words[match] = input(f"Enter a {match}: ")
    return words

# define a function to upgrade the template to an f-string
def upgrade_template(template, words):
    # the template includes mixed case words, but the dictionary keys are all lowercase
    # so modify the template first to make sure that I don't get keyerrors because of mixed case
    template = template.lower()
    return template.format(**words) # this is the magic line

# define a main function that calls the other functions
def main():
    words = get_words()
    upgraded_template = upgrade_template(template, words)
    print(upgraded_template)

# call the main function if this file is run as a script
if __name__ == '__main__':
    main()
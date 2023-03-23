#write a function that takes three strings as input, and fills them in to a madlib template

def madlib(name, subject, verb):
    return name + " is a " + subject + " who " + verb + "." 


#prompt the user for three strings, and call the function with the user input
name = input("Enter a name: ")
subject = input("Enter a subject: ")
verb = input("Enter a verb: ")

print(madlib(name, subject, verb))



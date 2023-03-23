# Create a function that takes a string as input and returns the average length of words in the string. 

def average_length_of_words(string):
    words = string.split()
    return sum(len(word) for word in words) / len(words)

#test average_length_of_words with various paramaters and print these to the terminal
print(average_length_of_words("This is a test"))
print(average_length_of_words("This is a test of the average length of words function"))
print(average_length_of_words("This is a test of the average length of words function with a very long string"))




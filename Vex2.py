#write a write a skeleton function for the word length calculator, including function definition, input parameters, and a return statement  
Sample_string = "life is like a box of chocolates, you never know what you're gonna get"

def wordLengthCalculator(word):
    return len(word)

#a loop that iterates through the words in the string, and finds the average length of the words in the string
def averageWordLengthCalculator(Sample_string):
    words = Sample_string.split()
    total = 0
    for word in words:
        total = total + wordLengthCalculator(word)
    return total/len(words)

#call the function and print the result
print(averageWordLengthCalculator(Sample_string))

#test the function with a large variety of strings, including strings with punctuation, numbers, and special characters, and strings with non-English characters

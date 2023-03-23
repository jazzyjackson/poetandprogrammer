#Objective: Create a function that takes a string as input and returns the average length of words in the string.
def word_length_calculator(sentence):
    # Split the sentence into individual words
    words = sentence.split()
    
    # Calculate the total number of characters in all words
    total_chars = sum(len(word) for word in words)
    
    # Calculate the average word length
    if len(words) > 0:
        avg_length = total_chars / len(words)
    else:
        avg_length = 0
    
    return avg_length

Sentence = "feed me as much fruit as you can"
# Print out sentence
print(Sentence.split())
avg_length = word_length_calculator(Sentence)
print(avg_length)
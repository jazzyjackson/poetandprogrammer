def count_char(string, char):
 count = 0
 for c in string:
  if c == char:
   count += 1
   return count
  
string = "contemplate"
char = "e"
count = count_char(string, char)
print (f"There are {count} instances of {char} in {string}")

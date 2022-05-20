#Python program to capitalize the first and last character of each word in a string (input string should be a statement)

s = "Python is a high level programming language"
s = s.title()
s = s.split()
string =" "
for i in s:
    string+= i[:-1]+i[-1].upper()+" "
print(string)

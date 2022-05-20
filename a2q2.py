#Python program to count the number of vowels in a given string

sentence = "Python is a high level programming language"
string = sentence.lower()
count=0
list = ["a","e","i","o","u"]
for i in string:
    if i in list:
        count = count +1
print("number of vowels in sentence:", count)
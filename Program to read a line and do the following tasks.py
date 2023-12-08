#Write a program to read a line and count:
#1.Number of digits
#2.Number of alphabets
#3.Number of lowercase letters
#4.Number of uppercase letters
#5.Number of symbols


a=input("Type a line: ")
lowercasecount=uppercasecount=0
digitscount=alphabetcount=symbolcount=0
for i in a:
    if i.islower():
        lowercasecount+=1
    elif i.isupper():
        uppercasecount+=1
    elif i.isdigit():
        digitscount+=1
    elif i.isalnum() !=True and a !=' ':
        symbolcount+=1
    elif i.isalpha():
        alphabetcount+=1
print(" ")
print("Number of digits in the given line:",digitscount)
print("Number of alphabets in the given line:",alphabetcount)
print("Number of lowercase letters in the given line:",lowercasecount)
print("Number of uppercase letters in the given line:",uppercasecount)
print("Number of symbols in the given line:",symbolcount)

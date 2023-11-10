
dt1={}
a="He kept repeating the same thing over and over He often has to ask people to repeat themselves because he's a little deaf"
words=a.split()

for i in words:
    key=i
    if key not in dt1:
        count=words.count(key)
        dt1[key]=count

print("Frequencies \n",words)

print(dt1,end=" ")


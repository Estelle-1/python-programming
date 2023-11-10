f=open(r"C:\Users\admin\AppData\Local\Programs\Python\Python37\FILE PEPPA.txt","r")
s=f.readlines()

for i in s:
    if i[0]=="P" or i[0]=="p":
        print(i)
f.close()

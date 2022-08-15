from tkinter import E


startstr1="LUST %2F%2F"
startstr2="ПОХОТЬ %2F%2F"
endstr1="/ FIRST"
endstr2="/ ПЕРВЫЙ"
filename="2-1.txt"
result=startstr1+"="+startstr2+"\n"
diff = len(endstr2) - len(endstr1)
if diff >=0:
    a = endstr1
else:
    a = endstr2
for i in range(len(a)):
    if startstr1=="":
        result+=endstr1[:i]+"="+endstr2[:i]+"\n"
    else:
            result+=startstr1+endstr1[:i]+"="+startstr2+endstr2[:i]+"\n"
result+=startstr1+endstr1+"="+startstr2+endstr2+"\n"
with open(filename, "a",encoding="utf-8") as file:
    file.write(result)

        




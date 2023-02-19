replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]

s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."

strToList = s.split(" ")

for str_word in range(0,len(strToList)-1):
    for replace_word in range(0,len(replace_with)):
        if replace_with[replace_word] == strToList[str_word]:
            strToList[str_word] = replace_with[replace_word+1]

print(strToList)

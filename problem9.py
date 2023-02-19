replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]

s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."

strToList = s.split()

for i in range(len(strToList)):
    if strToList[i] in replace_with:
        idx = replace_with.index(strToList[i])
        if idx < len(replace_with) - 1:
            strToList[i] = replace_with[idx+1]

output = ' '.join(strToList)

print(output)

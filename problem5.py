x={ 'a' : 1, 'b' :  2, 'c': 3, 'd': 4}

output=[]
for key in x:
    val=x[key]
    output.append(key)
    output.append(val)

print(output)
import re


def create_new_string():
    a = ['oh', 'Emelia', 'to']
    for i in range(0,len(a)):
        a[i]=a[i].lower()
    s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."
    strToList = re.split(r'[\s,.]+', s)
    outputList=[]
    for i in range(0,len(strToList)):
        if strToList[i].lower() in a:
            outputList.append(strToList[i+1])

    outputString = ' '.join(outputList)
    with open('out.txt', 'w') as file:
        file.write(outputString)

create_new_string()

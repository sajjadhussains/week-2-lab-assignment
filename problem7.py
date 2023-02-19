def replace_comma_with_space(text):
    output=""
    for character in text:
        if(character==","):
            output+=" "
        else: 
            output+=character
    return output
s = "I,have,been,practising,python,since,the,course,started"

output = replace_comma_with_space(s)
print(output)

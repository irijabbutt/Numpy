# occurences of a specific character in a string
n=0
char="a"
text="akjdadjda"
for i in text:
    if char==i:
        n=i      
        print("Occurence: ",n) 
    else:
        print("char not present")


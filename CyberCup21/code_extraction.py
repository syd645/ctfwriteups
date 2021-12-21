#bloos world color code
#Getting the hex color codes from the text file holding the HTML

lines = []

#opens the html_base.txt and sets each line as an object in lines array
with open('html_base.txt') as f:
    lines = f.readlines()

#Read in each entry of lines and get only the 6 characters after the '#'
for line in lines:
    result = line.index('#')
    slice_size = slice(result+1, result+7,1)
    #sets code equal to the needed 6 hex characters
    code = line[slice_size]
    #converts from hex and prints the output
    code_edit1 = bytes.fromhex(code)
    code_edit2 = code_edit1.decode()
    print(code_edit2)

f.close()


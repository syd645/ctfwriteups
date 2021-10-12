#bloos world color code
#Getting the hex color codes from the text file holding the HTML

lines = []
codes = []

with open('html_base.txt') as f:
    lines = f.readlines()


for line in lines:
    result = line.index('#')
    #print(result)
    slice_size = slice(result+1, result+7,1)
    code = line[slice_size]
    #code = str(code)
    #print(code)
    code_edit1 = bytes.fromhex(code)
    code_edit2 = code_edit1.decode()
    print(code_edit2)

f.close()


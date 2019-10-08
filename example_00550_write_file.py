
# read and write file

text = 'hallo wie geht es?'

myfilename = "mytext.txt"

with open(myfilename, "w") as file:
    file.write(text)
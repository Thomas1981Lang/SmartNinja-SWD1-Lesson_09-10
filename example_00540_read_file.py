
# einlesen von test.txt

filename = "test.txt"

myfile = open(filename)

mylines = myfile.readlines()

myfile.close()

print(mylines)

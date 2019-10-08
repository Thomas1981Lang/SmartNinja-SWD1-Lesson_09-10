# coding=utf-8
# schreibe eine while schleife
# sie addiert jedesmal 2 zu einem counter
# wenn der counter größer ist als 20, breche ab
# ansonsten print den counter

counter = 0

while counter <= 20:
    print(counter, ' Counter 1')
    counter += 2


counter = 0

while True:
    print(counter)
    counter += 2
    if counter > 20:
        break


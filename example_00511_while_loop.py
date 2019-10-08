# write a while loop to check if input with following symbols *,+,-,/ is  correct
# if yes exit loop

# while True:
#     var = input('Bitte gib ein Symbol an')
#     if '*' in var or '+' in var or '-' in var or '/' in var:
#         break



# solution b
# while True:
#     var = input('Bitte gib ein Symbol an')
#     if var in "+-*/":
#         print('ok')
#         break

# solution c
while True:
    var = input('Bitte gib ein Symbol an: ')
    if var in ["+", "-", "*", "/"]:
        print('ok')
        break
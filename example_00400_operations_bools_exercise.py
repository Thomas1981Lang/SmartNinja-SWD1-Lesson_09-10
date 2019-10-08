# coding=utf-8
# erstelle 2 zahlen (Bsp.: 5 und 1000), speichere sie als variablen
# prüfe ob die erste größer als die zweite ist
num_one = 5
num_two = 1000

if num_one > num_two:
    print('{} ist größer als {}'. format(num_one, num_two))
else:
    print('{} ist nicht größer als {}'. format(num_one, num_two))

# prüfe ob beide zahlen gleich sein
if num_one == num_two:
    print('{0} ist gleich groß wie {1}'. format(num_one, num_two))
else:
    print('{0} ist nicht gleich groß wie {1}'. format(num_one, num_two))

# erstelle 2 strings (wörter)    (z.B. Hallo und Tschüss)
# prüfe ob beide wörter gleich sind
txt_one = 'Hallo'
txt_two = 'Tschüss'

if txt_one == txt_two:
    print('{} ist gleich wie {}'. format(txt_one, txt_two))
else:
    print('{} ist nicht gleich wie {}'. format(txt_one, txt_two))



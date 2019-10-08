# erstelle eine liste mit folgenden daten ingredients salad, orange, mango
# waehle durch einen Zufallsgenerator ein element aus und speichere es in random_fruit.txt

fruits = "apfel, orange, kiwi"

filename = "fruitsalat.txt"


with open(filename, "w") as file:
    file.write(fruits)
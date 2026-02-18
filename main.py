name = "Petras"
surname = "Petraitis"

if len(name) > len(surname):
    print(name)
if len(name) == len(surname):
    print(name, surname)
else:
    print(surname)

name = "Bruce"
surname = "Willis"

print(name.upper())
print(surname.lower())

name = "Bruce"
surname = "Willis"
initials = name[0] + surname[0]

print(initials)

name = "Bruce"
surname = "Willis"

last_initials = name[-3:] + surname[-3:]
print(last_initials)

text = "An American in Paris"
changed_text = text.replace("a", "*").replace("A", "*")
print(changed_text)

text1 = "An American in Paris"
text2 = "Breakfast at Tiffany's"
text3 = "2001: A Space Odyssey"
text4 = "It's a Wonderful Life"

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""

    for letter in text:
        if letter not in vowels:
            result += letter

    return result

print(remove_vowels(text1))
print(remove_vowels(text2))
print(remove_vowels(text3))
print(remove_vowels(text4))

word = "level"

if word[0] == word[-1]:
    print("Sutampa")
else:
    print("Nesutampa")

word = "cappucino"

if word[0] == word[-1]:
    print("Sutampa")
else:
    print("Nesutampa")

word = "Telephone"

new_word = word[0] + "_" * (len(word) - 2) + word[-1]
print(new_word)

text = "Man 24 metai"

if ("0" in text or "1" in text or "2" in text or "3" in text or
    "4" in text or "5" in text or "6" in text or
    "7" in text or "8" in text or "9" in text):
    print("Yra skaičių")
else:
    print("Tik raidės")

text = "Man gerai sekasi"

if ("0" in text or "1" in text or "2" in text or "3" in text or
    "4" in text or "5" in text or "6" in text or
    "7" in text or "8" in text or "9" in text):
    print("Yra skaičių")
else:
    print("Tik raidės")


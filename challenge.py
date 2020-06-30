text = "the dog went his merry way"

# vowels = {"a", "o", "u", "e", "i"}
vowels = frozenset("aeiou")
finalSet = set(text).difference(vowels)

# for letter in text:
#     print(letter)
#     if letter in vowels:
#         print("found vowel " + letter)
#         text = text.replace(letter, "")

print(finalSet)

finalList = sorted(finalSet)
print(finalList)


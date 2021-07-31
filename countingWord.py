introduction = input("Enter Your Greeting: ")
characterCount = 0
wordCount = 1
for i in introduction:
    characterCount = characterCount + 1
    if(i == ' '):
        wordCount = wordCount + 1
print("Number of words in the string: ")
print(wordCount)
print("Number of characters in the string: ")
print(characterCount)
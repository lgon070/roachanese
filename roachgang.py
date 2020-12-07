text = input("Text to translate to Roachanese: ")
words = text.split(" ")
special_chars = ['.', ',', ';', ':', '-', '_', '\'', '\"', '?', '!', '$', '%', '&', '*', '(', ')', '/', '\\']
translated = []

for word in words:
    if "brother" in word:
        translated.append(word)
    else:
        newWord = word
        noSC = True
        for char in special_chars:
            if char in word:
                noSC = False
                index = word.find(char)
                newWord = word[:index] + "roach" + word[index:]
        if noSC:
            translated.append(newWord + "roach")
        else:
            translated.append(newWord)

translatedText = " "
print(translatedText.join(translated))



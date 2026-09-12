text = input("Sentence: ")

sentencestext = text.replace("!",".").replace("?",".")
sentences = sentencestext.split(".")

wordstext = sentencestext.replace(".","").replace(",","").replace(";","").replace(":","")
words = wordstext.split(" ")

letters = 0

for word in words:
    letters += len(word)

L = letters/len(words)*100
S = (len(sentences)-1)/len(words)*100

coleman = 0.0588 * L - 0.296 * S - 15.8

coleman = round(coleman)
# coleman = str(coleman)
# coleman = int(coleman[0])
if coleman > 16:
    print("Grade 16+")
elif coleman < 1:
    print("Before Grade 1")
else:
    print("Grade " + str(coleman))

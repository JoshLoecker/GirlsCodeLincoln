def textAnalyzer(text):
    print("Character count: " + str(len(text)))
    print("Word count: " + str(len(text.split())))
    print("Average words per character: " + str(len(text.split()) / len(text)))


textAnalyzer("This is a test string")
textAnalyzer("This is a test string with more words")

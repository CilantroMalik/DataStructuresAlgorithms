from sortedMap import SortedMap
"""
--- SearchEngine ---
Module that reads in a corpus of articles and creates a concordance out of them, an alphabetized list of all words in the
articles with data surrounding number and location of usages. The program uses this to inform a search algorithm that can
match a short user query to one of the articles based on word frequencies.
"""

# -- read in and process text file --
articleDB = SortedMap()
with open("./News.txt", mode='r') as newsFile:
    fullText = " ".join(newsFile.readlines())
    index = fullText.find("<ID>")
    while index != -1:
        articleId = int(fullText[index+4:fullText.find("</ID>", index)])
        bodyStart = fullText.find("<BODY>", index)
        articleText = fullText[bodyStart+6:fullText.find("</BODY>", bodyStart)]
        articleDB[articleId] = articleText
        index = fullText.find("<ID>", index+1)

print(articleDB)

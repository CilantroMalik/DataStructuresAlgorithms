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


# -- helper classes and functions --
class WordEntry:
    def __init__(self, line, pos):
        self.count = 1
        self.locations = [(line, pos)]

    def inc(self):
        self.count += 1

    def addLoc(self, line, pos):
        self.locations.append((line, pos))


def inc(aMap, key):
    try:
        aMap[key] += 1
    except KeyError:
        aMap[key] = 1


def updateEntry(aMap, key, line, pos):
    try:
        aMap[key].addLoc(line, pos)
        aMap[key].inc()
    except KeyError:
        aMap[key] = WordEntry(line, pos)


# -- create a concordance for each article --
# note: the full corpus concordance will just have word counts, but the individual article ones will store line
#       number and position information (as this is not really applicable for the large scale concordance)
fullCorpus = SortedMap()
masterTable = []
for article in articleDB:
    localConcordance = SortedMap()
    for i, line in enumerate(article.split("\n")):
        for j, word in enumerate(line.split()):
            if not word.lower().islower():
                continue
            inc(fullCorpus, word.lower())
            updateEntry(localConcordance, word.lower(), i, j)

import os

from sortedMap import SortedMap
"""
--- SearchEngine ---
Module that reads in a corpus of articles and creates a concordance out of them, an alphabetized list of all words in the
articles with data surrounding number and location of usages. The program uses this to inform a search algorithm that can
match a short user query to one of the articles based on word frequencies.
"""

# -- read in and process text file --
articleDB = SortedMap()
with open("./testNews.txt", mode='r') as newsFile:
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

    def getCount(self):
        return self.count

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


def cleanup(aWord):
    if not aWord[-1].isalpha():
        return aWord[:-1].lower()
    return aWord.lower()


def validate(aWord):
    if not word.lower().islower():
        return False
    for char in word:
        if char.isalpha():
            return True
    return False


# -- create a concordance for each article --
# note: the full corpus concordance will just have word counts, but the individual article ones will store line
#       number and position information (as this is not really applicable for the large scale concordance)
fullCorpus = SortedMap()  # a map of integers (keys are words, values are their counts)
masterTable = SortedMap()  # a map of maps (keys are article IDs, values are their concordances)
progress = 0
for article in articleDB:
    localConcordance = SortedMap()
    for i, line in enumerate(article.getVal().split("\n")):
        for j, word in enumerate(line.split()):
            if not validate(word):
                continue
            processed = cleanup(word)
            inc(fullCorpus, processed)
            updateEntry(localConcordance, processed, i, j)
    masterTable[article.getKey()] = localConcordance
    progress += 1
    os.system("clear")
    print("Articles scanned:", progress, "out of", len(articleDB))
    print("=" * int(progress / 5))

# -- implement search engine algorithm --
print("— Search the Corpus —")
query = input("Enter a query: ")
topResult1, topResult2 = None, None
if len(query.split(" ")) > 1:  # multi-word query
    maxCount = 0  # stores the article ID with the most occurrences of a particular multi-word phrase in its entirety
    for article in articleDB:
        numOccurrences = article.getVal().count(query)
        maxCount = article.getKey() if numOccurrences > maxCount else maxCount
    if maxCount > 0:
        topResult1 = articleDB[maxCount]
# single-word queries
results = []
for word in query.split(" "):
    maxOccurrences, secondMaxOccurrences = 0, 0
    maxArticle, secondMaxArticle = None, None
    for article in articleDB:
        concordance = masterTable[article.getKey()]
        try:
            if concordance[word].getCount() > maxOccurrences:
                secondMaxOccurrences, secondMaxArticle = maxOccurrences, maxArticle
                maxOccurrences, maxArticle = concordance[word].getCount(), article
            elif concordance[word].getCount() > secondMaxOccurrences:
                secondMaxOccurrences, secondMaxArticle = concordance[word].getCount(), article
        except KeyError:
            pass
    if maxArticle is not None:
        results.append((maxArticle, maxOccurrences))
    if secondMaxArticle is not None:
        results.append((secondMaxArticle, secondMaxOccurrences))
articleWeights = SortedMap()
for result in results:
    try:
        articleWeights[result[0].getKey()] += result[1]
    except KeyError:
        articleWeights[result[0].getKey()] = result[1]
maxWeight, secondMaxWeight = 0, 0
heaviest, secondHeaviest = None, None
for item in articleWeights:
    if item.getVal() > maxWeight:
        secondMaxWeight = maxWeight
        secondHeaviest = heaviest
        maxWeight = item.getVal()
        heaviest = item.getKey()
    elif item.getVal() > secondMaxWeight:
        secondMaxWeight = item.getVal()
        secondHeaviest = item.getKey()
if heaviest is None:
    print("No results.")
elif secondHeaviest is None:
    print("Only one result...")
    topResult1 = articleDB[heaviest]
    print("----------------- First Result -----------------\n", topResult1)
else:
    if topResult1 is None:
        topResult1 = articleDB[heaviest]
        topResult2 = articleDB[secondHeaviest]
    else:
        topResult2 = articleDB[heaviest] if articleDB[heaviest] != topResult1 else articleDB[secondHeaviest]
    print("----------------- First Result -----------------\n", topResult1)
    print("----------------- Second Result -----------------\n", topResult2)

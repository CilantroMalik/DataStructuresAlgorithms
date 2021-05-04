import os
from sortedMap import SortedMap

"""
--- SearchEngine ---
Module that reads in a corpus of articles and creates a concordance out of them, an alphabetized list of all words in the
articles with data surrounding number and location of usages. The program uses this to inform a search algorithm that can
match a short user query to one of the articles based on word frequencies.
"""

# -- read in and process text file --
articleDB = SortedMap()  # store articles in a sorted map, with IDs as keys
with open("./News.txt", mode='r') as newsFile:
    fullText = "\n".join(newsFile.readlines())  # create a string containing each line separated by a single newline character
    index = fullText.find("<ID>")  # locate the first ID tag from which we will read the ID of the first article, as a starting point
    while index != -1:  # for every single article until we can no longer find another ID tag (i.e. reached the last article)
        articleId = int(fullText[index+4:fullText.find("</ID>", index)])  # extract the article ID from between the tags as an integer
        bodyStart = fullText.find("<BODY>", index)  # find the start of the body tag for this article
        articleText = fullText[bodyStart+6:fullText.find("</BODY>", bodyStart)]  # get all the text after the opening and before the closing body tag
        articleDB[articleId] = articleText  # add the entry to the map
        index = fullText.find("<ID>", index+1)  # and prepare for the next iteration by looking for the next opening ID tag


# -- helper classes and functions --
class WordEntry:  # class that stores one entry in a concordance with necessary information
    def __init__(self, line, pos):
        self.count = 1  # number of occurrences of this word in the relevant scope
        self.locations = [(line, pos)]  # locations ("coordinates") in which this word appears in the releavnt scope

    def getCount(self):
        return self.count  # simple getter method for the property

    def inc(self):  # mostly for convenience; the only time we will ever need to change count is to increment it by one
        self.count += 1

    def addLoc(self, line, pos):  # adds a location to the internal list specified by a tuple of the line number and position on that line
        self.locations.append((line, pos))


def inc(aMap, key):  # method that increments the entry in the given map corresponding to the specified key (as a convenience)
    try:  # if the entry exists, increment it normally
        aMap[key] += 1
    except KeyError:  # if not, create the entry starting with a value of 1
        aMap[key] = 1


# method that adds a location and increments the WordEntry in a concordance; meant to be called for each word while
# processing an article and handles all the work of keeping concordance information up to date, while improving readability
def updateEntry(aMap, key, line, pos):
    try:  # if the word exists already, just add the location and increment its counter
        aMap[key].addLoc(line, pos)
        aMap[key].inc()
    except KeyError:  # if not, make a new WordEntry and assign it; the default count value is 1 and it adds the given location on initialization
        aMap[key] = WordEntry(line, pos)


def cleanup(aWord):  # another readability-improving method that handles word endings and case sensitivity
    if not aWord[-1].isalpha():  # if the last character is non-alphanumeric (usually a punctuation mark) remove it
        return aWord[:-1].lower()  # and always lowercase the word before returning to achieve case-insensitive behavior
    return aWord.lower()


def validate(aWord):  # method that, along with cleanup, handles empty words and "words" composed of non-alphanumerics
    if not aWord.lower().islower():  # islower() returns false if there are no cased characters (i.e. letters) so this is a check for empty strings
        return False
    for char in aWord:  # checks if there are no letter characters in the word (e.g. for things like '1', '&', etc) that should be skipped
        if char.isalpha():  # if there is at least one letter, the word is valid
            return True
    return False  # if we have not returned yet, the word is not empty but has no letters so it is invalid


# -- create a concordance for each article --
# note: the full corpus concordance will just have word counts, but the individual article ones will store line
#       number and position information (as this is not really applicable for the large scale concordance)
fullCorpus = SortedMap()  # a map of integers (keys are words, values are their counts)
masterTable = SortedMap()  # a map of maps (keys are article IDs, values are their concordances)
progress = 0  # for user feedback, as the process can take a while
for article in articleDB:
    localConcordance = SortedMap()  # will need to create a "local" concordance for every individual article
    for i, line in enumerate(article.getVal().split("\n")):  # loop through lines and words along with their indices
        for j, word in enumerate(line.split()):
            if not validate(word):  # validate the word to see if it should be counted
                continue
            processed = cleanup(word)  # preprocess the word with another helper function
            inc(fullCorpus, processed)  # increment the relevant word's count in the large corpus
            updateEntry(localConcordance, processed, i, j)  # and add the count and location to the local concordance
    masterTable[article.getKey()] = localConcordance  # when finished, add the local concordance to the map of maps
    progress += 1
    os.system("clear")  # display the progress to the user for transparency
    print("Articles scanned:", progress, "out of", len(articleDB))
    print("=" * int(progress / 5))

# -- implement search engine algorithm --
print("— Search the Corpus —")
query = input("Enter a query: ")  # fetch the user query
topResult1, topResult2 = None, None  # store the results when they are determined
if len(query.split(" ")) > 1:  # multi-word query handling
    maxCount = 0  # stores the article ID with the most occurrences of a particular multi-word phrase in its entirety
    maxCountArticle = -1
    for article in articleDB:  # go through every article and count the occurrences of the entire multi-word phrase
        numOccurrences = article.getVal().count(query)  # use builtin count method of a string
        maxCount = article.getKey() if numOccurrences > maxCount else maxCount  # if this is the highest count, store the article key
    # if no article had any occurrences of the phrase, this isn't a meaningful result; otherwise, this is the top result by default because it's an exact match
    if maxCountArticle == -1:
        topResult1 = articleDB[maxCount]  # store the article corresponding to the stored key we arrived at
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

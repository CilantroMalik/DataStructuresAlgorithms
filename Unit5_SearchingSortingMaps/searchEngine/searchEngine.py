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
# single-word analysis: using the concordances we created earlier
results = []  # store all possibly relevant results before filtering them to the most relevant one or two
for word in query.split(" "):  # search for each word separately
    maxOccurrences, secondMaxOccurrences = 0, 0  # create variables for the highest and second highest count of the word
    maxArticle, secondMaxArticle = None, None  # and corresponding ones for the articles that had those highest counts
    for article in articleDB:  # go through every article and try to find the relevant entry in that article's local concordance
        concordance = masterTable[article.getKey()]  # accessible from our map of maps with the article ID, due to the earlier setup
        try:  # wrap in a try-except because the word may not be in the article at all
            # we want to store the two largest counts of the word, which means we only pick out the articles whose counts are higher than the current stored values
            if concordance[word].getCount() > maxOccurrences:  # use the stored count property of every entry in the concordance
                secondMaxOccurrences, secondMaxArticle = maxOccurrences, maxArticle  # if larger than the max value, push the current max to second highest
                maxOccurrences, maxArticle = concordance[word].getCount(), article  # and then replace the max with this one
            elif concordance[word].getCount() > secondMaxOccurrences:  # if only larger than the second highest but not larger than the highest value
                secondMaxOccurrences, secondMaxArticle = concordance[word].getCount(), article  # just replace the second highest with this article's count
        except KeyError:  # if the word doesn't exist, we don't care, so the program just moves on without throwing an error and halting execution
            pass
    if maxArticle is not None:  # if we found an article that has the word in it at least once, we add that article to the results
        results.append((maxArticle, maxOccurrences))  # add the article key along with its number of occurrences, to be used as a weight later
    if secondMaxArticle is not None:  # if we found a second highest article, add that as well and its number of occurrences
        results.append((secondMaxArticle, secondMaxOccurrences))
# result selection: use a system of weights to find the article with the highest "score" across all words in the query
# this is to favor articles that placed highest or second highest for multiple words in the search query, if it was
# more than one word; if it was a single word, it effectively behaves like one would expect and finds the simple maximum
articleWeights = SortedMap()  # store weights in a map
for result in results:  # go through every result and add the number of occurrences to that article's "score"
    try:
        articleWeights[result[0].getKey()] += result[1]
    except KeyError:  # if the key does not exist yet, we assign to it instead of incrementing it
        articleWeights[result[0].getKey()] = result[1]
maxWeight, secondMaxWeight = 0, 0  # store the highest and second highest weights and their corresponding articles
heaviest, secondHeaviest = None, None
for item in articleWeights:  # for every weight, see if it is the highest or second highest
    if item.getVal() > maxWeight:  # same logic as earlier: if larger than max, push max to second max and replace the max
        secondMaxWeight, secondHeaviest = maxWeight, heaviest
        maxWeight, heaviest = item.getVal(), item.getKey()  # the items here are article keys and their weights
    elif item.getVal() > secondMaxWeight:  # and if larger than only the second max, just replace that
        secondMaxWeight, secondHeaviest = item.getVal(), item.getKey()
# final selection and displaying of results
if heaviest is None:  # if there is no weight larger than 0, this variable will never be set, which means no word in the query exists in any article
    print("No results.")  # so report as such
elif secondHeaviest is None:  # if only one nonzero result was found, secondHeaviest will still be None, so we handle this case
    if topResult1 is None:  # if there was no result from the multi-word phase, set the top result to our "heaviest" article
        topResult1 = articleDB[heaviest]
    else:  # if there was already a first result, set the second result to the heaviest, unless they are the same article in which case we have only one actual result
        topResult2 = articleDB[heaviest] if articleDB[heaviest] != topResult1 else None
    if topResult2 is None:  # if there was no second result, inform the user of this
        print("Only one result...")
    print("----------------- First Result -----------------\n", topResult1)  # we are guaranteed to have at least one result in this case
    if topResult2 is not None:  # if we have two results, display both of them
        print("----------------- Second Result -----------------\n", topResult2)
else:  # finally, if both of the heaviest slots are occupied, we have potentially more than two top results
    if topResult1 is None:  # if this was not already filled from the multi-word phase, populate both result slots with our highest weighted articles
        topResult1 = articleDB[heaviest]
        topResult2 = articleDB[secondHeaviest]
    else:  # if the first result slot is already full, put the heaviest article in the second (unless they are the same, in which case use the second heaviest)
        topResult2 = articleDB[heaviest] if articleDB[heaviest] != topResult1 else articleDB[secondHeaviest]
    print("----------------- First Result -----------------\n", topResult1)  # finally, print both results
    print("----------------- Second Result -----------------\n", topResult2)

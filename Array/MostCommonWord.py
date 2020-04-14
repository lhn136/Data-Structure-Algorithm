from collections import defaultdict
import re

def mostCommonWord(paragraph, banned):
    wordDict = defaultdict(int)
    lowerParagraph = re.sub("[?.!/;:,]",'',paragraph.lower())
    for word in lowerParagraph.split():
        wordDict[word] += 1

    maxCount = 0
    maxWord = ''
    for word,val in wordDict.items():
        if word not in banned:
            if val > maxCount:
                maxCount = val
                maxWord = word
    return maxWord



print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]))


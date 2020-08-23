#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findKangarooScore' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY words
#  2. STRING_ARRAY wordsToSynonyms
#  3. STRING_ARRAY wordsToAntonyms
#
'''
3
Devilish
Devilishly
phone
4
Devilish:evil
phone:cell,telephone
decoy:facade,fake
Devilishly:evil
1
decoy:truth,real
'''

'''
2
Municipality
Community
2
Municipality:city,unity
Community:county,city
1
community:my
'''

class Solution():
    def __init__(self, words, wordsToSynonyms, wordsToAntonyms):
        print(words, wordsToSynonyms, wordsToAntonyms)
        self.words = words
        self.wordSynonymsDict = self.getWordDict(wordsToSynonyms)
        self.wordAntonymsDict = self.getWordDict(wordsToAntonyms)
        # print(self.wordAntonymsDict)
        self.synJoeyToKangaroos = {}
        self.antJoeyToKangaroos = {}
        self.totalScore = 0

    def getWordDict(self, wordSets):
        wordDict = {}
        for wordSet in wordSets:
            parent, children = wordSet.split(':')
            parent = parent.lower()
            children_list = [child.lower() for child in children.split(',')]
            wordDict[parent] = children_list
        return wordDict


    def findKangarooScore(self):
        # Get Synonym score and Antonym Score for each word
        # print("Finding Score for: {}".format(words))
        for word in self.words:
            synScore = self.getWordScore(word.lower(), self.wordSynonymsDict, 1)
            antScore = self.getWordScore(word.lower(), self.wordAntonymsDict, 0)
            # print('{}: SynScore = {}, AntScore = {}'.format(word, synScore, antScore))
            self.totalScore += (synScore - antScore)

        # Get Synonym Cousin Score and Antonym Cousin Score
        synCousinScore = self.getCousinScore(self.synJoeyToKangaroos)
        antCousinScore = self.getCousinScore(self.antJoeyToKangaroos)

        # print('Normal score = {}, synCousin = {}, antCousin = {}'.format(self.totalScore, synCousinScore, antCousinScore))
        

        return self.totalScore + antCousinScore + synCousinScore
    
    def getCousinScore(self, joeyDict):
        # print(joeyDict)
        score = 0
        for joey in joeyDict:
            # no. of combinations to select 2 from 'l' elements: l*(l-1)//2
            l = len(joeyDict[joey])
            score += (l*(l-1)//2)
        return score
        

        

    def getWordScore(self, parent, wordDict, synFlag):
        score = 0
        for child in wordDict.get(parent, []):
            # print('{} Get score of {} and {}'.format(synFlag, parent, child))
            if self.isJoey(parent, child):
                score += 1
                # Add to joeyToKangaroos dictionary to calculate cousin points later
                if synFlag:
                    if child not in self.synJoeyToKangaroos:
                        self.synJoeyToKangaroos[child] = []
                    self.synJoeyToKangaroos[child].append(parent)
                else:
                    if child not in self.antJoeyToKangaroos:
                        self.antJoeyToKangaroos[child] = []
                    self.antJoeyToKangaroos[child].append(parent)

        return score

    def isJoey(self, parent, child):
        p, c = 0, 0
        prevMatchIndex = -2
        isContinousFlag = True # set to True by default
        matchFound = False
        while p < len(parent):
            if parent[p] != child[c]:
                p += 1
                continue
            # parent[p] == child[c]
            # print('Word = {}, Child = {}. c = {}, prev = {}, curr = {}'.format(parent, child, c, prevMatchIndex, p))
            if matchFound and isContinousFlag and p > prevMatchIndex+1:
               isContinousFlag = False 
            # if isContinousFlag and p == prevMatchIndex+1:
            #     prevMatchIndex = p
            # elif prevMatchIndex >= 0:
            #     isContinousFlag = False
            
            prevMatchIndex = p
            c += 1
            p += 1
            matchFound = True
            if c == len(child):
                break

        
        if c < len(child):
            # Not all child characters found
            return False


        # All cases from here on are for when child IS found
        
        if not isContinousFlag:
            # i.e. the child word doesnt occur continously
            return True

        lastChildChar = child[-1]
        while p < len(parent):
            # Check if the last char can be found in parent from where we stopped in prev while loop
            if parent[p] == lastChildChar:
                isContinousFlag = False
            p += 1

        if isContinousFlag == False:
            # Child word is not continous
            return True

        # Default and when child is Continuous
        # print("Child '{}' is continuous in '{}'.".format(child, parent))
        return False




def findKangarooScore(words, wordsToSynonyms, wordsToAntonyms):
    # Write your code here
    solve = Solution(words, wordsToSynonyms, wordsToAntonyms)
    return solve.findKangarooScore()
if __name__ == '__main__':
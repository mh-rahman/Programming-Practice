# '''
# There is a problem on level 4 called "distract the guards" where it's about graph matching and math theory called distracted the guards. Although my code got AC but I've also found a counter case soon after submission. I figured out that I need some math theory expert to help me complete the puzzle and stop it from haunting me.
# '''

# #Get counter - for easy lookup
# #sort banana array
# #Get max elem - maxBananas
# #Keep track of potential matches in a set
# for i,b in enumerate(bananas):
#     nxt = 2*b
#     while not nxt > maxBananas:
#         if nxt in bCounter:
#             potentialMatches[i].add(nxt)
#         nxt *= 2


n = 107
print((24**n - 9*(8**n) + 18*(3**n) + 9*(2**n) - 24)%(10**9 + 7))
    


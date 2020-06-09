import collections
class Solution:
    def fourSumCount(self, A, B, C, D) -> int:
        
        if not A and not B and not C and not D:
            return 0
        
        if len(A) == 1 and len(B) == 1 and len(C) == 1 and len(D) == 1:
            return 1 if 0 in A and 0 in A and 0 in C and 0 in D else 0
        
        ##Approach 1
#         A.sort()
#         B.sort()
#         C.sort()
#         D.sort()
        
#         dictA = {}
#         dictB = {}
#         # dictC = {}
#         dictC = {num:D.count(num) for num in set(D)}
        
#         count = 0
#         targetA = 0
#         for a in set(A):
#             targetB = targetA - a
#             # print("A: setting",a,"searching for",targetB,":target = ",targetA)
#             if dictA.get(targetB,-1) == -1:
#                 ##Never searched
#                 countB = 0
#                 for b in set(B):
#                     targetC = targetB - b
#                     # print("B: setting",b,"searching for",targetC,":target = ",targetB)
#                     if dictB.get(targetC,-1) == -1:
#                         countC = 0
#                         for c in set(C):
#                             targetD = targetC - c
#                             # print("C: setting",c,"searching for",targetD,":target = ",targetC)
#                             countC += (dictC.get(targetD,0)*C.count(c))
#                         dictB[targetC] = countC
#                     else:
#                         countC = dictB[targetC]
#                     countB += countC*B.count(b)
#                 dictA[targetB] = countB
#             else:
#                 countB = dictA[targetB]
                
#             count += countB*A.count(a)
            
#         return count


        ##Approach 2:
        AB = collections.Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)


class Solution2:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        def binarySearch(A:List[int],n:int) -> bool:
            #returns true if n in A (in log time)
            pass
        
        #Since we are checking indices only, need to consider all possibilities
        #Sort since only count is asked and not actual indices
        #Define boundary for C,D combinations: minCD = min(C)+min(D), maxCD = max(C)+max(D)
        #For any sum s using A,B (n**2 possibilities), find if -s is possible from C,D
        #If x<minCD or x>maxCD, set count 0 (impossible to get x from C,D)
        #Else, Store x:count (x = -s) in a hash table (cdDict)
        #Else, If x not in abDict then do:
        #To check x in C,D: for all (c) from C and search for x-c in D. Add to count.
        #Optionally store the result of x-c:res in another hash table (dDict)
        #Using 2 hash tables - one to store 
        
        return 0
class Solution:
    def mygenerateParenthesis(self, n: int) -> List[str]:
#         def helper(n, start, end):
#             if n == 1:
#                 s = start+'()'+end
#                 res.add(s)
#             else:
#                 helper(n-1,'()'+start,end)
#                 helper(n-1,start+'(',')'+end)
#                 helper(n-1,start+'()'+end,'')
#                 helper(n-1,'('+start,end+')')
#                 helper(n-1,start,end+'()')
        
#             return
        
#         res = set([])
#         helper(n,'','')
        return res

    def generateParenthesis(self, n):
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left-1, right)
            if right > left: generate(p + ')', left, right-1)
            if not right:    parens += p,
            return parens
        return generate('', n, n)
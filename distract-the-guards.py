# '''
# There is a problem on level 4 called "distract the guards" where it's about graph matching and math theory called distracted the guards. Although my code got AC but I've also found a counter case soon after submission. I figured out that I need some math theory expert to help me complete the puzzle and stop it from haunting me.
# '''

from collections import defaultdict
from math import gcd

def loops(x, y):
    res = int((x+y)/gcd(x,y))
    return bool(res & (res - 1))

def remove(guards, ref):
    for i in range(len(guards)):
        j = 0 
        while j < len(guards[i]):
            if(guards[i][j]==ref):
                guards[i].pop(j)
            j+=1 
    guards[ref]=[-1]

def answer(banana_list):
    guards= [[] for i in range(len(banana_list))]
    bad=0
    
    for i in range(len(guards)):
        for j in range(len(guards)):
            if(loops(banana_list[i], banana_list[j])):
                guards[i].append(j)

    to_process=len(banana_list)
    while(to_process>0):

        min_num=0
        for i in range(len(guards)):
            if(i!=0 and (len(guards[i])<len(guards[min_num]) or guards[min_num]
                == [-1]) and guards[i]!=[-1]):
                min_num=i

        if((len(guards[min_num])) == 0 or (len(guards[min_num])==1 and
                guards[min_num][0] == guards[min_num]) and guards[min_num] !=
                [-1]):
            remove(guards, min_num)
            to_process-=1
            bad+=1
        else:
            min_node=guards[min_num][0]
            for i in range(len(guards[min_num])):
                if(i!=0 and guards[min_num][i]!=min_num and len(guards[guards[min_num][i]])<len(guards[min_node])):
                    min_node=guards[min_num][i]
            if(guards[min_node]!=[-1]):
                remove(guards, min_num)
                remove(guards, min_node)
                to_process-=2

    return bad 



def isInfiniteLoop(b1, b2):
  # total bananas
  
  total = b1+b2

  # Trimming end zero bits
  while total & 1 == 0:
    total = total >> 1

  
  # Check if new total divides b1 - if yes, then it will not be an infinite loop
  # print('New total after trimming = {}'.format(total))
  # print(b1 % total == 0 )
  return not b1 % total == 0


def getGuardGraph(bananas):
  graph, l = defaultdict(list), len(bananas)
  
  for i in range(l):
    for j in range(i,l):
      if isInfiniteLoop(bananas[i], bananas[j]):
        # if i not in graph:
        #   graph[i] = []
        graph[i].append(j)
        graph[j].append(i)

  # print(graph)
  return graph.items()
        

def answer0(bananas):
  graph = getGuardGraph(bananas)
  print(graph)

  # using Blossom's Algorithm to efficiently find the maximum matching

# print(answer0([1,2]))


# print(answer([1,2]))
def makeGood(s: str) -> str:
    res = []
    i = 0
    while i <len(s)-1:
        c, c_ = s[i], s[i+1]
        if c != c_ and c.lower() == c_.lower():
            i += 2
        else:
            res.append(c)
            i += 1
    if i < len(s):
      res.append(s[i])
    print(res)
    return ''.join(res)

test = "leEeetcode"
print(makeGood(test))

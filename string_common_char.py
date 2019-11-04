string1='apple'
string2='pineapple'
l=[]
for s in string1:
  if s in string2 and s not in l:
    l.append(s)
print(l)

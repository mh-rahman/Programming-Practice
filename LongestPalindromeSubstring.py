#! python

s=input('Enter the string:')
length=len(s)
n=length

max_palindrome_count=1
max_palindrom_string=s[0]

# Finding odd length palindromes

for i in range (1,length-1):
    this_count=1
    j=1
    #for j in range(1,min(i,n-2-i)+1):
    while s[i-j]==s[i+j] and j<(min(i,n-1-i)+1):
        this_count+=2
        j+=1
        if j==(min(i,n-1-i)+1):
            break
    if this_count>max_palindrome_count:
        max_palindrome_count=this_count
        max_palindrom_string=s[i-j+1:i+j]

# Even palindromes

for i in range (0,length-1):
    if s[i]!=s[i+1]:
        continue
    else:
        this_count=0
        j=0
        #for j in range(1,min(i,n-2-i)+1):
        print (i,j)
        while s[i-j]==s[i+j+1] and j<(min(i,n-2-i)+1):
            this_count+=2
            j+=1
            if j==(min(i,n-2-i)+1):
                break
        if this_count>max_palindrome_count:
            max_palindrome_count=this_count
            max_palindrom_string=s[i-j+1:i+j+1]

print('Longest palindrom count is {} and the string is {}'.format(max_palindrome_count,max_palindrom_string))

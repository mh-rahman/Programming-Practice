class Solution:
    def decodeString(self, s: str) -> str:
        def decodeHelper(inp):
            if '[' not in inp:
                return inp
            else:

                start_pointer = 0
                temp = ''
                
                while inp[start_pointer]>='a' and inp[start_pointer]<='z':
                    start_pointer+=1
                
                temp+=inp[:start_pointer]
                end_pointer = start_pointer
                
                while inp[start_pointer]!='[':
                    start_pointer+=1

                mul = int(inp[end_pointer:start_pointer])

                count = 1
                pointer = start_pointer

                while count>0:
                    pointer+=1
                    if inp[pointer] == '[':
                        count+=1
                    elif inp[pointer] == ']':
                        count-=1


                end_pointer = pointer

                temp = temp + mul*decodeHelper(inp[start_pointer+1:end_pointer]) + decodeHelper(inp[end_pointer+1:])
                
                
                return temp
            

        return decodeHelper(s)

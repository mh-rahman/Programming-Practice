class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node('Begin')
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        # print(word)
        head = self.head
        for c in word:
            if c not in head.children:
                # print('Adding ',c,'to', head.val)
                head.children[c] = Node(c)
            head = head.children[c]
        head.children['End'] = word
                
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        head = self.head
        for i,c in enumerate(word):
            if c == '.':
                for temp in head.children:
                    if len(temp) > 1:
                        continue
                    if self.helper(head.children[temp],i+1,word):
                        return True
            if c not in head.children:
                return False
            head = head.children[c]
        
        return head.children.get('End','') == word
        

        
    def helper(self,head,ind,word):
        # print(head.val,ind,word)
        while ind < len(word):
            c = word[ind]
            # print(c, c in head.children)
            if c == '.':
                for temp in head.children:
                    if len(temp) > 1:
                        continue
                    if self.helper(head.children[temp],ind+1,word):
                        return True
            if c not in head.children:
                return False
            head = head.children[c]
            ind += 1
        return 'End' in head.children
        
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


class Node:
    
    def __init__(self,val):
        self.val = val
        self.children = {}
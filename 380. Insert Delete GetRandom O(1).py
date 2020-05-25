class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val_flag_list = []
        self.vals = set([])
        self.val_to_index = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        flag = False
        
        if val not in self.vals:
            flag = True
            self.vals.add(val)
            if self.val_to_index.get(val,-1) == -1:
                self.val_flag_list.append([val,1])
                self.val_to_index[val] = len(self.val_flag_list) - 1
            else:
                self.val_flag_list[self.val_to_index[val]][1] = 1
            
        return flag
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        flag = False
        if val in self.vals:
            flag = True
            self.vals.remove(val)
            self.val_flag_list[self.val_to_index[val]][1] = -1
            # self.val_to_index[val] = -1
            
        return flag
        
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        choice = (-1,-1)
        while choice[1] == -1:
            choice = random.choice(self.val_flag_list)
            
        return choice[0]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
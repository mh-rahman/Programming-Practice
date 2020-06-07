class BrowserHistory:

    def __init__(self, homepage: str):
        self.hp = homepage
        self.bwd = [homepage]
        self.fwd = []

    def visit(self, url: str) -> None:
        # print(url)
        self.bwd.append(url)
        self.fwd = []
        # print(self.bwd)
        return 

    def back(self, steps: int) -> str:
        # print('Before backward',self.bwd,self.fwd,steps)
        i = 0
        l = len(self.bwd)-1
        while i < min(steps,l):
            url = self.bwd.pop()
            self.fwd.append(url)
            i+=1
        # print('After backward',self.bwd,self.fwd,steps)
        return self.bwd[-1]

    def forward(self, steps: int) -> str:
        # print('Before forward',self.bwd,self.fwd,steps)
        i = 0
        l = len(self.fwd)
        if l < 1:
            return self.bwd[-1]
        while i < min(steps,l):
            url = self.fwd.pop()
            self.bwd.append(url)
            i+=1
        # print('After forward',self.bwd,self.fwd,steps)
        return self.bwd[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
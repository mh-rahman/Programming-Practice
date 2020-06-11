class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not numCourses:
            return []
        needs = {i:0 for i in range(numCourses)} #course:dependency_count
        neededby = {i:[] for i in range(numCourses)}
        
        for prereq in prerequisites:
            course,dependsOn = prereq
            needs[course]+=1
            neededby[dependsOn].append(course)
        
        res = []
        independent = [k for k in needs.keys() if needs[k] == 0]

        while independent:
            course = independent.pop()
            res.append(course)
            numCourses-=1
            for c in neededby[course]:
                needs[c]-=1
                if needs[c] == 0:
                    independent.append(c)

        return res if not numCourses else []
        
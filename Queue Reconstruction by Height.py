class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = []
        people = [[x[0], x[1], x[1]] for x in people]
        while people:
            people = sorted(people, key = lambda x: (x[1], x[0]), reverse = True)
            temp = people.pop()
            for i in range(len(people)):
                if people[i][0]>temp[0]:
                    continue
                else:
                    people[i][1]-=1
            result.append(temp)
        result = [[x[0], x[2]] for x in result]
        # print(result)
        return result
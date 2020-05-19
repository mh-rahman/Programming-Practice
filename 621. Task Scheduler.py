class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_count = list(collections.Counter(tasks).values())
        max_count = max(tasks_count)
        max_count_tasks = tasks_count.count(max_count)
        return max(len(tasks), (max_count-1)*(n+1)+max_count_tasks)
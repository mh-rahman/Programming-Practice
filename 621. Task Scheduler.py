class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0: return len(tasks)
        
        task_counter, last_ran = Counter(tasks), {} # task: time when task was last performed
        task_heap, total_wait, time_elapsed = [], 0, 0
        heapq.heapify(task_heap)
        
        for k in task_counter:
            heapq.heappush(task_heap, (-1*task_counter[k],-n-1,k))
            # (negative of no. of tasks of type k, last_ran, k)
            
        # print(task_heap)
        
        while task_heap:
            num, last_ran, task = heapq.heappop(task_heap)
            new_heap, most_prev = [], last_ran
            # print('time_elapsed = ', time_elapsed)
            # print(time_elapsed, last_ran, n, not (time_elapsed - last_ran > n))

            while task_heap and not time_elapsed - last_ran > n:
                # print('Cannot run {}, instances = {}, last ran = {}'.format(task, num, last_ran))
                new_heap.append((num, last_ran, task))
                num, last_ran, task = heapq.heappop(task_heap)
                
                # Keeping track of the most previous run
                most_prev = min(most_prev, last_ran)
            
            if not time_elapsed - last_ran > n:
                # Checking if even the last task cannot be done
                # print('Cannot run {}, instances = {}, last ran = {}'.format(task, num, last_ran))
                
                new_heap.append((num, last_ran, task))
                task_heap = new_heap
                heapq.heapify(task_heap)
                
                # Skipping to time where a task can be ran
                total_wait += (most_prev + n + 1 - time_elapsed)
                time_elapsed = most_prev + n + 1
                
                # print('Wait time.')
                continue
            
            # print('Completing task {}, remaining instances = {}'.format(task,-num-1) )
            
            #Adding tasks back to heap
            while new_heap:
                heapq.heappush(task_heap, new_heap.pop())

            
            if num + 1 < 0:
                heapq.heappush(task_heap, (num+1, time_elapsed, task))
            
            time_elapsed += 1
            
            
        return len(tasks) + total_wait
            
            
            
#approch 1
class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        Jobs.sort(key=lambda x: x.profit, reverse=True)
        
        # To keep track of free time slots
        result = [False] * n
        
        # To store result (sequence of jobs)
        job_sequence = [-1] * n
        
        # Total profit and job count
        total_profit = 0
        job_count = 0

        # Iterate through all given jobs
        for job in Jobs:
            # Find a free slot for this job (we start from the last possible slot)
            for j in range(min(n, job.deadline) - 1, -1, -1):
                # Free slot found
                if not result[j]:
                    result[j] = True
                    job_sequence[j] = job.id
                    total_profit += job.profit
                    job_count += 1
                    break
        
        return job_count, total_profit
      #approach 2
      import heapq
 
 
def printJobScheduling(arr):
    n = len(arr)
 
    # arr[i][0] = job_id, arr[i][1] = deadline, arr[i][2] = profit
 
    # sorting the array on the
    # basis of their deadlines
    arr.sort(key=lambda x: x[1])
 
    # initialise the result array and maxHeap
    result = []
    maxHeap = []
 
    # starting the iteration from the end
    for i in range(n - 1, -1, -1):
 
        # calculate slots between two deadlines
        if i == 0:
            slots_available = arr[i][1]
        else:
            slots_available = arr[i][1] - arr[i - 1][1]
 
        # include the profit of job(as priority), deadline
        # and job_id in maxHeap
        # note we push negative value in maxHeap to convert
        # min heap to max heap in python
        heapq.heappush(maxHeap, (-arr[i][2], arr[i][1], arr[i][0]))
 
        while slots_available and maxHeap:
 
            # get the job with max_profit
            profit, deadline, job_id = heapq.heappop(maxHeap)
 
            # reduce the slots
            slots_available -= 1
 
            # include the job in the result array
            result.append([job_id, deadline])
 
    # jobs included might be shuffled
    # sort the result array by their deadlines
    result.sort(key=lambda x: x[1])
 
    for job in result:
        print(job[0], end=" ")
    print()
 

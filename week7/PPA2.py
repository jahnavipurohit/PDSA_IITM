'''A manufacturing plant has n independent working lines. Each job requires different 
amount of time to be completed and due time. Optimize the scheduling of jobs for every line 
so that every job is will be completed within due time or minimum lateness possible.
Write a function minimizeLateness (N, jobs) to return the sequence of job ids to be scheduled 
in list of list. jobs is the tuple of (job_id, time_required, due_time), where job_id, 
time_required and due_time are the unique number assigned to job, relative time required to 
complete the job and absolute time before which the job should have completed respectively.
Note:
job_id is given from 0 to m-1, for m jobs.
Lateness = m ΣL(i) id=0 -Time Due(i) L(i) = {if (if Time Delivered(i) > 1 TimeDue(i), 
Time Delivered(i) - Time Due(i)) else, 0 (2)}
For each test case there will be a upper bound of lateness on the second line of input. 
The lateness of your optimum schedule should be less than or equal to the upper bound of lateness.'''

import heapq

def minimizeLateness(N, jobs):
    """
    Schedules jobs on N working lines to minimize total lateness.

    The algorithm uses a greedy approach:
    1. It sorts the jobs in ascending order of their due times (Earliest Due Date rule).
    2. It uses a min-heap to keep track of the completion time of each line, allowing
       for efficient selection of the line that will become available the soonest.
    3. It iterates through the sorted jobs and assigns each job to the line
       with the minimum current completion time.

    Args:
        N (int): The number of independent working lines.
        jobs (list of tuple): A list of jobs, where each tuple is
                              (job_id, time_required, due_time).

    Returns:
        list of list: A list where each inner list represents the sequence
                      of job IDs scheduled on a specific line.
    """
    # Sort the jobs based on their due time in ascending order.
    # The Earliest Due Date (EDD) rule is a well-known heuristic for minimizing
    # lateness, and it is a good starting point for multi-line scheduling.
    jobs.sort(key=lambda x: x[2])

    # Initialize a schedule for each of the N lines.
    # Each element in this list will be a list of job IDs.
    schedule = [[] for _ in range(N)]

    # Use a min-heap to keep track of the current completion time for each line.
    # The heap stores tuples of (completion_time, line_index).
    # This allows us to efficiently find the line that becomes available next.
    # Initialize all lines with a completion time of 0.
    line_completion_heap = [(0, i) for i in range(N)]
    
    # Iterate through the jobs and assign them to the earliest available line.
    for job in jobs:
        job_id, time_required, due_time = job
        
        # Pop the line with the minimum completion time from the heap.
        # This is the line that will be free to take on the next job.
        current_completion_time, line_index = heapq.heappop(line_completion_heap)
        
        # Add the current job to the schedule for the selected line.
        schedule[line_index].append(job_id)
        
        # Calculate the new completion time for this line.
        # It's the previous completion time plus the time required for the new job.
        new_completion_time = current_completion_time + time_required
        
        # Push the updated completion time and line index back to the heap.
        heapq.heappush(line_completion_heap, (new_completion_time, line_index))

    return schedule

def calculate_total_lateness(N, jobs, schedule):
    """
    Calculates the total lateness for a given schedule.

    Args:
        N (int): The number of independent working lines.
        jobs (list of tuple): The original list of jobs.
        schedule (list of list): The schedule to evaluate.

    Returns:
        int: The total lateness.
    """
    # Create a dictionary for quick lookup of job details by ID.
    job_details = {job[0]: job for job in jobs}
    total_lateness = 0
    
    # Track the completion time for each line.
    line_completion_times = [0] * N
    
    # Iterate through each line and its scheduled jobs.
    for i in range(N):
        current_line_time = 0
        for job_id in schedule[i]:
            _, time_required, due_time = job_details[job_id]
            current_line_time += time_required
            
            # Calculate the lateness for the current job.
            lateness = max(0, current_line_time - due_time)
            total_lateness += lateness
            
    return total_lateness

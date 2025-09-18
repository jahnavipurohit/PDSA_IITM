'''You're given a list of tuples Activity for n activities, where in each tuple (activity_name, S, F, P), 
activity activity_name is scheduled to be done from start time s to finish time F and obtains 
a profit of P after the finish.
Find out the maximum profit you can obtained by scheduled activities, but no two activities should
be in the subset with overlapping of time frame. If you choose an activity that finishes at time x 
then another activity can be started at time x, not before that.
Write a function MaxProfit (Activity) that accepts a list of tuples Activity for n activities and 
returns the value of maximum profit that can be obtained by scheduled activities.
Sample Input
[('A',1,2,40), ('B',3,4,5), ('c',0,7,6), ('D',1,2,3), ('E',5,6,8), ('F',5,9,2), 
('G',10,11,9), ('н', 0, 11, 35)]
Output
62
Explanation
Activity schedule [A, B, E, G] gives a profit of 62 which is the maximum in all possible schedules'''

def MaxProfit(activities):
    """
    Calculates the maximum profit from a list of activities that do not overlap.

    Args:
        activities (list of tuples): Each tuple is (activity_name, start, finish, profit).

    Returns:
        int: The maximum profit.
    """
    # Sort activities by their finish times
    activities.sort(key=lambda x: x[2])
    n = len(activities)
    
    # dp[i] stores the max profit considering the first i activities
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        # Profit of the current activity
        current_profit = activities[i-1][3]
        
        # Find the latest non-conflicting activity
        # 'p' is the index of the latest activity that finishes before 
        # or at the same time as the current activity's start time
        j = i - 1
        while j > 0 and activities[j-1][2] > activities[i-1][1]:
            j -= 1
        
        # Max profit is either including the current activity or not
        dp[i] = max(current_profit + dp[j], dp[i-1])

    return dp[n]



L = eval(input())
print (MaxProfit(L))
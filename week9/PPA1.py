'''A thief robbing a store and can carry a maximum weight of w in his bag. There are n items 
in the store with weights (W1, W2, W3...., wn and corresponding values (V1, V2, V3,...,n. 
What items should he select to get maximum value? He cannot break an item, either he picks 
the complete item or doesn't pick it.
Write a function MaxValue(Items, W) that accepts a dictionary Items, where the key of the dictionary 
represents the item number (1 to n) and the corresponding value is a tuple (weight of item, value
of item). The function accepts one more integer w, which represents the maximum weight capacity of
the bag. The function returns the total value of all selected items, which is maximum in all possible selection.
Example Input
8# w - Maximum weight capacity of bag
(1: (2,10),2: (3,20).3: (4,40)} # Items
Output
60 # total value is 60 which is maximum.
Explanation
The thief can pick items 2 and 3 where the total weight of picked items is 3 + 4 = 7 which is 
less than the maximum capacity of the bag, but he gets maximum value (60) for this selection.'''

def MaxValue(Items, W):
    """
    Calculates the maximum value of items that can be placed in a bag 
    with a maximum weight capacity W.

    Args:
        Items (dict): A dictionary where keys are item numbers and 
                      values are tuples (weight, value).
        W (int): The maximum weight capacity of the bag.

    Returns:
        int: The maximum total value of items that can be selected.
    """
    # Extract weights and values from the dictionary and sort by item number
    sorted_items = sorted(Items.items())
    weights = [item[1][0] for item in sorted_items]
    values = [item[1][1] for item in sorted_items]
    n = len(weights)

    # dp[i][j] will be the max value using first i items with weight capacity j
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            current_weight = weights[i - 1]
            current_value = values[i - 1]

            if current_weight <= j:
                # Option 1: Don't include the item
                # Option 2: Include the item
                dp[i][j] = max(dp[i - 1][j], current_value + dp[i - 1][j - current_weight])
            else:
                # Item is too heavy, can't be included
                dp[i][j] = dp[i - 1][j]
    
    # The final answer is in the bottom-right corner of the table
    return dp[n][W]


W = int(input())
Items= eval(input())
print(MaxValue(Items,W))
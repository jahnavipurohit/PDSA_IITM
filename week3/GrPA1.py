'''A restaurant always prepares dishes with the most orders before others 
with a lesser number of orders. Each dish in the restaurant menu has a unique integer ID. 
The restaurant receives n orders in a particular time period. 
The task is to find out the order of dish IDs according to which the restaurant will prepare them. 
Assume that restaurant has the following unique dish IDs in its menu:

[1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009]

Write a function DishPrepareOrder(order_list) that accepts order_list in the form of 
a list of dish IDs and returns a list of dish IDs in the order in which the restaurant will prepare them. 
If two or more dishes have the same number of orders, then the dish which has a smaller ID value will be prepared first.'''

def insertionsort(L): 
    n = len(L)
    if n < 1:
        return(L)
    for i in range(n):
        j = i
        while(j > 0 and L[j][1] > L[j-1][1]):
            (L[j],L[j-1]) = (L[j-1],L[j])
            j = j-1
    return(L)

def DishPrepareOrder(order_list):
    order_count = {}
    R = []
    for order in order_list:
        if order in order_count:
            order_count[order] += 1
        else:
            order_count[order] = 1
    for ID in sorted(order_count.keys()):
        R.append((ID,order_count[ID]))
    R=insertionsort(R)
    Res = []
    for tup in R:
        Res.append(tup[0])
    return Res
nums = eval(input())
print(DishPrepareOrder(nums))
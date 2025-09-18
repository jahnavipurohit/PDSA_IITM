'''The government decides to construct a new railway station. Railway authorities provide a 
list of scheduled trains in a day with arrival time and departure time. Find the minimum number of 
platforms required for the railway station so that no train is kept waiting.
Write a function minimum_platform(train_schedule) that accepts a list of tuples train_schedule, 
where each tuple stores three values in the format (train_no(int), Arrival_time('HH:MM'), 
departure_time('HH:MM')). The function should return the minimum number of platforms required 
for the railway station so that no train is kept waiting.
Sample Input
[(1,'09:00','09:10'), (2, '09:40', '12:00'), (3, '09:50', '11:20'), 
(4,'11:00', '11:30'), (5, '11:40', '12:10'), (6, '12:05', '19:00'), 
(7,'12:06', '13:00'), (8, 13:05', '14:00'), (9'14:05', '15:00'), 
(10,'18:00','20:00')]
Output
3'''

def minimum_platform(train_schedule):
    count = 1
    train_list = []
    for (i,j,k) in train_schedule:
        train_list.append((int(j.replace(':','')),int(k.replace(':','')),i))
    train_list.sort()
    train_at_plateform = []
    for train in train_list:        
        
        t = len(train_at_plateform)-1
        while t >= 0:
            if train[0] > train_at_plateform[t][1]:
                train_at_plateform.pop(t)
            t = t-1        
        t = len(train_at_plateform)-1
        while t >= 0:
            if train[0] < train_at_plateform[t][1]:
                t = t - 1        
            elif train[1] > train_at_plateform[t][1]:
                train_at_plateform.pop(t)
                t = t - 1                
        train_at_plateform.append(train)                    
        if len(train_at_plateform) > count:
            count = len(train_at_plateform)
    return count

schedule = eval(input())           
print(minimum_platform(schedule))
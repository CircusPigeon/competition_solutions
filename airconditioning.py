###
You are the boss of ACM (Air Conditioned Minions), an upstanding company with a single goal of world domination.

The company has minions. Each minion works evilly from early morning until evening inside a super secret bunker in Helsinki. 
After much deliberation, you decided to move your headquarters to Singapore. However, unlike Helsinki, Singapore is very hot, 
so the entire complex must be air conditioned. With strenuous working hours (under minimum wage too), it is imperative that all 
your minions work under optimal work condition. In particular, all minions must like the temperatures of the rooms they are in.

You are planning to construct several rooms in your new hideout, and assign your minions there. You fix the temperature of each 
room to any value you want (different rooms may have different temperatures). After you fix the temperatures, you will assign 
each of your minions to these rooms (a room can hold any number of minions). You want all minions to like the temperatures of 
their assigned rooms. Each minion likes an interval of temperature, and these preferences will be given to you.

Air conditioners are very expensive to maintain. Thus, you want to construct as few rooms as possible. What is the minimum number 
of rooms you need to set up such that it would be possible to assign minions to rooms as discussed earlier?

Input
The first line contains a non-negative integer 2 <= N <= 100, giving the number of minions in your company. The next 
N lines each describe the temperature preferences of all your minions. The i-th line consists of two single space separated integers 
L and U (1 <= L <= U <= 2N), which denotes that the i-th minion likes any temperature between L and U, inclusively.

Output
Print an integer denoting the minimum number of rooms you need to construct.
###

import sys

if __name__ == "__main__":
    lines = sys.stdin.readlines()

    intervals = []
    for x in lines[1:]:
        l = int(x[:(x.find(" "))])
        u = int(x[(x.find(" ")+1):])
        intervals.append((l, u))

    intervals.sort(key = lambda x : x[0])
    
    numRooms = 0
    while (len(intervals)):
        maxT, maxNum = 0, 0
        for x in range(intervals[-1][0], int(intervals[-1][1]) + 1):
            num = 0
            for i in range(len(intervals)):
                for y in range(intervals[i][0], int(intervals[i][1]) + 1):
                    if (x == y):
                        num += 1
            if (num > maxNum):
                maxNum = num
                maxT = x
        
        for i in reversed(range(len(intervals))):
            for x in range(intervals[i][0], int(intervals[i][1]) + 1):
                if (x == maxT):
                    intervals.remove(intervals[i])

        numRooms += 1
    
    print(numRooms)

'''
    input:
        schedule = [(0,2,25), (1,5,40), (6,8,170), (3,7,220)]
        (start time, end time, utility value)
    output:
        WS_topdown(schedule) = 245
'''


def lastNonConflict(index, schedule, isSorted=False):
    # Given the index of the class and the list of schedule,
    # this function returns the last class that does not conflict with this class, if it exists otherwise returns None
    if not isSorted:
        schedule = sorted(schedule, key=lambda tup: tup[1])
    for i in range(index, -1, -1):
        if schedule[index][0] >= schedule[i][1]:
            return i
    return None


def WS_rec_(schedule, n):
    '''
        Solution 1: simple recursion
            time complexity O(n2^n)
    '''
    if n == None or n < 0:
        return 0
    if n == 0:
        return schedule[n][2]

    return max(schedule[n][2] + WS_rec_(schedule, lastNonConflict(n, schedule, isSorted=True)),
               WS_rec_(schedule, n-1))


def WS_rec(schedule):
    schedule = sorted(schedule, key=lambda tup: tup[1])
    return WS_rec_(schedule, len(schedule)-1)


print(WS_rec([(0, 2, 25), (1, 6, 40), (6, 9, 170), (3, 8, 220)]))


def WS_topdown_(schedule, n, memo):
    '''
        Solution 2: top-down approach
            time complexity O(n^2)
            space complexity O(n)
    '''
    if n == None or n < 0:
        return 0
    if n == 0:
        return schedule[n][2]
    if n in memo:
        return memo[n]
    memo[n] = max(schedule[n][2] + WS_topdown_(schedule, lastNonConflict(n, schedule, isSorted=True), memo),
                  WS_topdown_(schedule, n-1, memo))
    return memo[n]


def WS_topdown(schedule):
    schedule = sorted(schedule, key=lambda tup: tup[1])  # sort by end time
    memo = {}
    return WS_topdown_(schedule, len(schedule)-1, memo)


# make sure start and end of any event is not the same
print(WS_topdown([(0, 2, 25), (1, 5, 40), (6, 8, 170), (3, 7, 220)]))
schedule = [(i, i+2, 10) for i in range(100)]
print(WS_topdown(schedule))


def WS_bottomup(schedule):
     '''
        Solution 2: top-down approach
            time complexity O(n^2)
            space complexity O(n)
    '''
    # sort the schedule by end times of events
    schedule = sorted(schedule, key=lambda tup: tup[1])
    dp = [0 for _ in range(len(schedule)+1)]

    for i in range(1, len(schedule) + 1):
        # find the last conflicting event
        index_LC = lastNonConflict(i-1, schedule, isSorted=True)
        if index_LC == None:
            index_LC = -1
        # find the max of either keeping this event or not keeping it
        dp[i] = max(dp[i-1], dp[index_LC+1]+schedule[i-1][2])
    return dp[len(schedule)]


print(WS_bottomup([(0, 2, 25), (1, 5, 40), (6, 8, 170), (3, 7, 220)]))
schedule = [(i, i+2, 10) for i in range(100)]
print(WS_bottomup(schedule))

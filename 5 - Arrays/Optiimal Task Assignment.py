'''
    1) Optimal Task Assignment
        Assign tasks to workers so that the time it takes to complete all the tasks is minimized 
        given a count of workers and an array where each element indicates the duration of a task.
        a.  use greedy approach
            - sort array
            - pair the longest task (element) with the shortest one
'''

A = [6, 3, 2, 7, 5, 5]
A = sorted(A)  # A = [2, 3, 5, 5, 6, 7]

for i in range(len(A)//2):  # i = 0, 1, 2
    print(A[i], A[~i])  # ~ = bitwise complement

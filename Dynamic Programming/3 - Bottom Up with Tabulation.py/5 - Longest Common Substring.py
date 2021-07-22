'''
    input:
        str1 = "hello elf"
        str2 = "hello yourself"
    output: 
        lcs("hello elf", "hello yourself") = 6
        lcs("hel", "elf") = 2
'''


def lcs_rec(str1, str2, i, j, count):
    '''
        Solution 1: simple recursion
            time complexity O(3^(m+n))
    '''
    # base case of when either of string has been exhausted
    if i >= len(str1) or j >= len(str2):
        return count
    # if i and j character matches, increment the count and compare the rest of the strings
    if str1[i] == str2[j]:
        count = lcs_rec(str1, str2, i+1, j+1, count+1)
    # compare str1[1:] with str2, str1 with str2[1:], and take max of current count and these two results
    return max(count, lcs_rec(str1, str2, i+1, j, 0), lcs_rec(str1, str2, i, j+1, 0))


def lcs_rec_main(str1, str2):
    return lcs_rec(str1, str2, 0, 0, 0)


print(lcs_rec_main("hello", "elf"))


def lcs_topdown(str1, str2, i, j, count, memo):
    '''
        Solution 2: top-down approach
            time complexity O(mn^2)
            space complexity O(mn^2)
    '''
    if i >= len(str1) or j >= len(str2):
        return count
    # check if result available in memo
    if (i, j, count) in memo:
        return memo[(i, j, count)]
    c = count
    if str1[i] == str2[j]:
        c = lcs_topdown(str1, str2, i+1, j+1, count+1, memo)
    memo[(i, j, count)] = max(c, lcs_topdown(str1, str2, i+1,
                                             j, 0, memo), lcs_topdown(str1, str2, i, j+1, 0, memo))
    return memo[(i, j, count)]


def lcs_topdown_main(str1, str2):
    memo = {}
    return lcs_topdown(str1, str2, 0, 0, 0, memo)


print(lcs_topdown_main("hel", "elf"))


def lcs_bottomup(str1, str2):
    '''
        Solution 3: bottom-up approach 
            time complexity O(nm)
            space complexity O(nm)
    '''
    n = len(str1)
    m = len(str2)

    # table for tabulation of 2d array with size m x n
    dp = [[0 for j in range(m+1)] for i in range(n+1)]
    maxLength = 0  # to keep track of longest substring seen

    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:  # if characters at this position match,
                # add 1 to the previous diagonal and store it in this diagonal
                dp[i][j] = dp[i-1][j-1] + 1
                # if this substring is longer, replace it in maxlength
                maxLength = max(maxLength, dp[i][j])
            else:
                dp[i][j] = 0
    return maxLength


print(lcs_bottomup("hel", "elf"))


def lcs_bottomup_optimized(str1, str2):
    '''
    Solution 4: bottom-up approach space optimized
        time complexity O(nm)
        space complexity O(n)
    '''
    n = len(str1)
    m = len(str2)

    # table for tabulation, only maintaining state of last row
    dp = [0 for i in range(n+1)]
    maxLength = 0

    for j in range(1, m+1):
        # calculate new row (based on previous row i.e. dp)
        thisrow = [0 for i in range(n+1)]
        for i in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                thisrow[i] = dp[i-1] + 1
                maxLength = max(maxLength, thisrow[i])
            else:
                thisrow[i] = 0
        dp = thisrow  # after evaluating thisrow, set dp equal to this row to be used in the next iteration
    return maxLength


print(lcs_bottomup_optimized("hel", "elf"))

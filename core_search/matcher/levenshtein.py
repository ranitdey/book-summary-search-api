"""
Author: Ranit Dey
Description: String pre processing utilities
"""


def levenshtein_ratio(string1, string2):
    rows = len(string1)+1
    cols = len(string2)+1
    dp = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][0] = i
            dp[0][j] = j
    for col in range(1, cols):
        for row in range(1, rows):
            if string1[row - 1] == string2[col - 1]:
                cost = 0
            else:
                cost = 2
            dp[row][col] = min(dp[row - 1][col] + 1, dp[row][col - 1] + 1, dp[row - 1][col - 1] + cost)
    return ((len(string1) + len(string2)) - dp[row][col]) / (len(string1) + len(string2))

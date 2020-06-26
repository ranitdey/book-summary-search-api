"""
Author: Ranit Dey
Description: Utilities to get text similarity percentage using levenshtein distance
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


def levenshtein_partial_ratio(string1, string2):
    first = len(string1)
    second = len(string2)
    smaller = min(first, second)
    if first < second:
        query = string1
        target = string2
    else:
        query = string2
        target = string1
    substrings = custom_length_substrings(target,smaller)
    ratios = []
    for substring in substrings:
        curr_ratio = levenshtein_ratio(query, substring)
        if curr_ratio > .995:
            return 100
        else:
            ratios.append(curr_ratio)
    return max(ratios)


def custom_length_substrings(target_text, substring_size):
    substrings = [target_text[i: j] for i in range(len(target_text)) for j in range(i + 1, len(target_text) + 1) if
                  len(target_text[i:j]) == substring_size]
    return substrings


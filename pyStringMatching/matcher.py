from Levenshtein import distance, jaro, jaro_winkler

def LCS(str1, str2):
    """
    Returns the longest common subsequence (LCS) and length of LCS
    between string str1 and str2.
    Details of Longest Common Subsequence can be found here:
    https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
    """
    # generate matrix of length of longest common subsequence for substrings of both words
    lengths = [[0] * (len(str2)+1) for _ in range(len(str1)+1)]
    for indx_str1, char_str1 in enumerate(str1):
        for indx_str2, char_str2 in enumerate(str2):
            if char_str1 == char_str2:
                lengths[indx_str1+1][indx_str2+1] = lengths[indx_str1][indx_str2] + 1
            else:
                lengths[indx_str1+1][indx_str2+1] = max(
                    lengths[indx_str1+1][indx_str2],
                    lengths[indx_str1][indx_str2+1]
                )
    # read a substring from the matrix
    result = ""
    len_str2 = len(str2)
    for indx in range(1, len(str1)+1):
        if lengths[indx][len_str2] != lengths[indx-1][len_str2]:
            result += str1[indx-1]
    return (result, len(result))

def LCSubStr(str1, str2):
    """
    Returns the longest common substrings (LCSubStr) and length of LCSubStr
    between string str1 and str2.
    Details on Longest Common SubString can be found here:
    https://en.wikipedia.org/wiki/Longest_common_substring_problem
    """
    # Create a table to store lengths of longest common suffixes of substrings.
    # Note that lc_suff[i][j] contains the length of longest common suffix of
    # str1[0   indx_1-1] and str2[0   indx_2-1].
    len_str1 = len(str1)
    len_str2 = len(str2)
    lc_suff = [[0 for _ in range(len_str2+1)] for _ in range(len_str1+1)]
    # To store the length of longest common substring
    result = 0
    # Following steps build lc_suff in bottom up fashion
    for indx_str1 in range(len_str1 + 1):
        for indx_str2 in range(len_str2 + 1):
            if (indx_str1 == 0 or indx_str2 == 0):
                lc_suff[indx_str1][indx_str2] = 0
            elif (str1[indx_str1-1] == str2[indx_str2-1]):
                lc_suff[indx_str1][indx_str2] = lc_suff[indx_str1-1][indx_str2-1] + 1
                result = max(result, lc_suff[indx_str1][indx_str2])
            else:
                lc_suff[indx_str1][indx_str2] = 0
    return result

def LCS_list(str1, list_strs):
    """
    Get LCS of input string str1 with every string in list_strs.
    Returns a dict with keys belonging to list_strs and values being
    tuples with lcs and length of lcs.
    """
    result = {}
    for itm in list_strs:
        result[itm] = LCS(str1, itm)
    return result

def LCSubStr_list(str1, list_strs):
    """
    Get LCSubStr of input string str1 with every string in list_strs.
    Returns a dict with keys belonging to list_strs and values being
    tuples with length of lcsubstr.
    """
    result = {}
    for itm in list_strs:
        result[itm] = LCSubStr(str1, itm)
    return result

def levenshtein(str1, str2):
    """
    Returns absolute levenshtein distance between 2 strings.
    """
    return distance(str1, str2)

def jaro_similarity(str1, str2):
    """
    Returns jaro similarity between 2 strings.
    """
    similarity = jaro(str1, str2)
    return similarity

def jaro_winkler_similarity(str1, str2):
    """
    Returns jaro winkler similarity between 2 strings.
    """
    similarity = jaro_winkler(str1, str2)
    return similarity
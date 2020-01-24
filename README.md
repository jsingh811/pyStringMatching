# pyStringMatching
Here you will find different string similarity metrics in one place, including Longest Common Subsequence (LCS), Longest Common Substring (LCSubStr), Levenshtein Distance, Jaro Similarity and Jaro Winkler Similarity for usage in python 3.x.  

# Setup 
Clone the project and get it setup

```
git clone git@github.com:jsingh811/pyStringMatching.git
cd pyStringMatching
pip install -e .
pip install -r requirements/requirements.txt
```

# Usage
Examples  
```
from pyStringMatching import matcher

# Longest Common Subsequence (LCS)  
lcs, lcs_len = matcher.LCS("string", "strings")

# Longest Common Sub-string (LCSubStr)
lcsubstr = matcher.LCSubStr("string", "strings")

# Longest Common Subsequence (LCS) against a list of strings
lcs_matches = matcher.LCS_list("string", ["strings", "sting"])

# Longest Common Sub-string (LCSubStr) against a list of strings
lcsubstr_matches = matcher.LCSubStr_list("string", ["strings", "sting"])

# Levenshtein distance between 2 strings 
lev = matcher.levenshtein("string", "strings")

# Jaro similarity between 2 strings 
j_similarity = matcher.jaro_similarity("string", "strings")

# Jaro-Winkler  similarity between 2 strings 
jw_similarity = matcher.jaro_winkler_similarity("string", "strings")
```
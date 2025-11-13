# Napisz funkcję, która znajdzie najdłuższy wspólny prefiks ciągu znaków w 
# tablicy ciągów znaków.

# Jeśli nie ma wspólnego prefiksu, zwróć pusty ciąg znaków „”.

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        min_len = min(len(s) for s in strs)

        common_prefix = ""

        for i in range(min_len):
            char = strs[0][i]

            if all(s[i] == char for s in strs):
                common_prefix += char
            else:
                break
        
        return common_prefix

def main():
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))

main()
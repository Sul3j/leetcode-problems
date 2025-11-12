# Dla danej tablicy liczb całkowitych nums i liczby całkowitej target, zwróć indeksy dwóch liczb, których suma wynosi target.

# Można założyć, że każde dane wejściowe mają dokładnie jedno rozwiązanie i nie można używać tego samego elementu dwukrotnie.

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i


def main():
    s = Solution()
    print(s.twoSum([3,2,4], target=6))

main()




        
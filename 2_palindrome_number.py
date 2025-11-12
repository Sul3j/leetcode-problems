# zadanie nr. 9

# dany jest integer x, zwróć true jezeli jest palindromem, i false jeśli nie.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)

        if(strX[::-1] == strX):
            return True
        else:
            return False
           
        
def main():
    s = Solution()

    print(s.isPalindrome(121))

main()






class Solution:

    @staticmethod
    def __refrence(val:str) -> int:
        ref = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        return ref[val]
    
    def romanToInt(self, s: str) -> int:
        result = 0
        for i in range(len(s) - 1):
            x = self.__refrence(s[i])
            b = self.__refrence(s[i+1])
            
            if x < b:
                result -= x
            else:
                result += x

        result += self.__refrence(s[-1])
        return result

result = Solution().romanToInt("LVIII")
print(result)

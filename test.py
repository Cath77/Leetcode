class Solution:
    def isUgly(self, n: int) -> bool:
      if n <= 0:
        return False

      div = [2, 3, 5]
      for factor in div:
        while n % factor == 0:
          n /= factor
        
      return n == 1

print(Solution.isUgly(Solution, 6))